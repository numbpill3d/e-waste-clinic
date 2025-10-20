#!/usr/bin/env python3
"""
USB descriptor lister using GreatFET One as host
"""

from greatfet import GreatFET

def list_usb_devices():
    dev = GreatFET()
    print("Enumerating USB devices...")
    devices = dev.usb.enumerate()
    for d in devices:
        print(f"{d.vendor_id}:{d.product_id} - {d.manufacturer} - {d.product}")

if __name__ == "__main__":
    list_usb_devices()
