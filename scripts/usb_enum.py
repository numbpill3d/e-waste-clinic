#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
USB Device Enumerator

Lists all connected USB devices and displays their descriptors.
Useful for identifying chips and understanding USB device hierarchies.

Usage:
    python3 usb_enum.py [--verbose]

Options:
    --verbose    Show full descriptor details

Author: Charlotte Hardware Collective
"""

import sys
import argparse

try:
    import usb.core
    import usb.util
except ImportError:
    print("Error: pyusb library not found")
    print("\nInstall with:")
    print("  pip3 install pyusb")
    print("\nOn Linux, you may also need:")
    print("  sudo apt install libusb-1.0-0")
    sys.exit(1)


# USB device class codes
USB_CLASS_NAMES = {
    0x00: "Device (defined at interface level)",
    0x01: "Audio",
    0x02: "CDC-Communications",
    0x03: "HID (Human Interface Device)",
    0x05: "Physical",
    0x06: "Image",
    0x07: "Printer",
    0x08: "Mass Storage",
    0x09: "Hub",
    0x0A: "CDC-Data",
    0x0B: "Smart Card",
    0x0D: "Content Security",
    0x0E: "Video",
    0x0F: "Personal Healthcare",
    0x10: "Audio/Video Devices",
    0xDC: "Diagnostic Device",
    0xE0: "Wireless Controller",
    0xEF: "Miscellaneous",
    0xFE: "Application Specific",
    0xFF: "Vendor Specific",
}


def get_class_name(class_code):
    """Convert USB class code to readable name."""
    return USB_CLASS_NAMES.get(class_code, f"Unknown (0x{class_code:02X})")


def get_string_descriptor(device, index):
    """Safely retrieve a string descriptor from a USB device."""
    if index == 0:
        return None
    
    try:
        return usb.util.get_string(device, index)
    except Exception:
        return None


def print_device_info(device, verbose=False):
    """Print information about a USB device."""
    
    # Get basic device information
    vid = device.idVendor
    pid = device.idProduct
    
    # Try to get string descriptors
    manufacturer = get_string_descriptor(device, device.iManufacturer)
    product = get_string_descriptor(device, device.iProduct)
    serial = get_string_descriptor(device, device.iSerialNumber)
    
    # Get device class
    device_class = get_class_name(device.bDeviceClass)
    
    # Print main device info
    print("\n" + "=" * 60)
    print(f"Device: {product or 'Unknown Device'}")
    print("=" * 60)
    print(f"  Vendor ID:       0x{vid:04X}")
    print(f"  Product ID:      0x{pid:04X}")
    
    if manufacturer:
        print(f"  Manufacturer:    {manufacturer}")
    
    if product:
        print(f"  Product:         {product}")
    
    if serial:
        print(f"  Serial Number:   {serial}")
    
    print(f"  Device Class:    {device_class}")
    print(f"  USB Version:     {device.bcdUSB / 256:.1f}")
    print(f"  Device Version:  {device.bcdDevice / 256:.2f}")
    
    # Print verbose information if requested
    if verbose:
        print(f"\n  Configuration Details:")
        print(f"    Max Packet Size: {device.bMaxPacketSize0} bytes")
        print(f"    Configurations:  {device.bNumConfigurations}")
        
        try:
            cfg = device.get_active_configuration()
            print(f"    Interfaces:      {cfg.bNumInterfaces}")
            
            print(f"\n  Interface Details:")
            for interface in cfg:
                print(f"    Interface {interface.bInterfaceNumber}:")
                print(f"      Class:    {get_class_name(interface.bInterfaceClass)}")
                print(f"      Subclass: 0x{interface.bInterfaceSubClass:02X}")
                print(f"      Protocol: 0x{interface.bInterfaceProtocol:02X}")
                print(f"      Endpoints: {interface.bNumEndpoints}")
                
        except Exception as e:
            print(f"    (Could not read configuration: {e})")
    
    # Print lookup suggestion
    print(f"\n  Lookup: https://the-sz.com/products/usbid/index.php")
    print(f"          ?v=0x{vid:04X}&p=0x{pid:04X}")


def main():
    parser = argparse.ArgumentParser(
        description="Enumerate USB devices and display their information"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed descriptor information"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("USB Device Enumerator")
    print("E-Waste Reverse Engineering Clinic")
    print("=" * 60)
    
    # Find all USB devices
    devices = list(usb.core.find(find_all=True))
    
    if not devices:
        print("\nNo USB devices found.")
        print("\nTroubleshooting:")
        print("- Check that devices are connected")
        print("- On Linux, you may need to run with sudo")
        print("- Verify libusb is installed")
        sys.exit(0)
    
    print(f"\nFound {len(devices)} USB device(s):")
    
    # Print information for each device
    for device in devices:
        try:
            print_device_info(device, verbose=args.verbose)
        except Exception as e:
            print(f"\nError reading device: {e}")
            print(f"  Vendor ID:  0x{device.idVendor:04X}")
            print(f"  Product ID: 0x{device.idProduct:04X}")
    
    # Print summary and next steps
    print("\n" + "=" * 60)
    print(f"Enumeration complete. Found {len(devices)} device(s).")
    print("\nNext steps:")
    print("1. Look up vendor and product IDs in USB database")
    print("2. Note any interesting devices for further investigation")
    print("3. Use log_to_csv.py to record your findings")
    print("4. For detailed info, run with --verbose flag")
    print("=" * 60)


if __name__ == "__main__":
    main()
