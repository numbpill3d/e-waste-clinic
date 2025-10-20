#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
I²C Address Scanner for GreatFET One

This script scans the I²C bus for connected devices and reports their addresses.
Useful for identifying chips on circuit boards during reverse engineering workshops.

Usage:
    python3 i2c_probe.py [--speed SPEED]

Options:
    --speed SPEED    I²C clock speed in Hz (default: 400000)
                     Try 100000 for slower devices or noisy connections

Author: Charlotte Hardware Collective
"""

import sys
import argparse
from greatfet import GreatFET
from greatfet.interfaces.i2c_bus import I2CBus

# Common I²C device types by address range
COMMON_DEVICES = {
    range(0x48, 0x50): "ADC or Temperature Sensor",
    range(0x50, 0x58): "EEPROM (24C series)",
    range(0x60, 0x70): "Display or GPIO Expander",
    range(0x68, 0x69): "RTC or IMU Sensor",
    range(0x76, 0x78): "Environmental Sensor (BME/BMP series)",
    range(0x3C, 0x3E): "OLED Display",
}


def get_device_hint(address):
    """Return a hint about what type of device might be at this address."""
    for addr_range, device_type in COMMON_DEVICES.items():
        if address in addr_range:
            return device_type
    return "Unknown device type"


def scan_i2c_bus(gf, speed=400000):
    """
    Scan the I²C bus for devices.
    
    Args:
        gf: GreatFET device instance
        speed: I²C clock speed in Hz
        
    Returns:
        List of discovered device addresses
    """
    print(f"Initializing I²C bus at {speed} Hz...")
    
    try:
        i2c = I2CBus(gf)
        i2c.speed = speed
    except Exception as e:
        print(f"Error initializing I²C: {e}")
        print("\nTroubleshooting tips:")
        print("- Check that GreatFET is connected properly")
        print("- Verify firmware is up to date: greatfet_firmware --auto")
        print("- Try reconnecting the device")
        return []
    
    print("Scanning addresses 0x00 to 0x7F...")
    print("This may take 30-60 seconds...\n")
    
    devices = []
    
    # Scan the full 7-bit address range
    for address in range(0x00, 0x80):
        try:
            # Try to read one byte from the device
            # If it responds without error, a device is present
            i2c.read(address, 1)
            devices.append(address)
            
            # Print immediately when found for better user feedback
            hint = get_device_hint(address)
            print(f"  0x{address:02X} - {hint}")
            
        except Exception:
            # No device at this address, continue scanning
            pass
    
    return devices


def main():
    parser = argparse.ArgumentParser(
        description="Scan I²C bus for connected devices using GreatFET"
    )
    parser.add_argument(
        "--speed",
        type=int,
        default=400000,
        help="I²C clock speed in Hz (default: 400000, try 100000 for difficult boards)"
    )
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("GreatFET I²C Scanner")
    print("E-Waste Reverse Engineering Clinic")
    print("=" * 50)
    print()
    
    # Connect to GreatFET
    try:
        print("Connecting to GreatFET...")
        gf = GreatFET()
        print(f"Connected to GreatFET {gf.serial_number()}")
        print()
    except Exception as e:
        print(f"Error connecting to GreatFET: {e}")
        print("\nTroubleshooting:")
        print("- Is GreatFET plugged in?")
        print("- Do you have permissions? (Linux: check plugdev group)")
        print("- Try: greatfet_info")
        sys.exit(1)
    
    # Perform scan
    devices = scan_i2c_bus(gf, speed=args.speed)
    
    # Print summary
    print()
    print("=" * 50)
    if devices:
        print(f"Scan complete. Found {len(devices)} device(s).")
        print()
        print("Next steps:")
        print("1. Note these addresses in your lab notebook")
        print("2. Physically inspect chips near I²C traces")
        print("3. Look up addresses at: i2cdevices.org/addresses")
        print("4. Use log_to_csv.py to record your findings")
    else:
        print("Scan complete. No devices found.")
        print()
        print("Troubleshooting:")
        print("- Check your wiring (SDA, SCL, GND)")
        print("- Verify target board is powered")
        print("- Try slower speed: --speed 100000")
        print("- Check for pull-up resistors on I²C lines")
        print("- Some boards need 3.3V or 5V from GreatFET")
    print("=" * 50)


if __name__ == "__main__":
    main()
