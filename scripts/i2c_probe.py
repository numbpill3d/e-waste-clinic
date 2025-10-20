#!/usr/bin/env python3
"""
Simple I²C bus scanner using GreatFET One
"""

from greatfet import GreatFET

def scan_i2c():
    dev = GreatFET()
    i2c = dev.i2c
    found = []
    print("Scanning I²C addresses...")
    for address in range(0x03, 0x78):
        try:
            i2c.transmit(address, b'')
            found.append(hex(address))
        except Exception:
            pass
    if found:
        print("Devices found:", ', '.join(found))
    else:
        print("No devices detected.")
    return found

if __name__ == "__main__":
    scan_i2c()
