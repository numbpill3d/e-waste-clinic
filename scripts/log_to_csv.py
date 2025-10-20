#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
Chip Identification Logger

Interactive script to create properly formatted CSV logs of chip identifications
for the E-Waste Reverse Engineering Clinic database.

Usage:
    python3 log_to_csv.py

Author: Charlotte Hardware Collective
"""

import csv
import os
from datetime import datetime


def get_input(prompt, default=None):
    """Get input from user with optional default value."""
    if default:
        prompt = f"{prompt} [{default}]"
    
    value = input(prompt + ": ").strip()
    
    if not value and default:
        return default
    
    return value


def get_board_name():
    """Get the board name from user."""
    print("\nBoard Information")
    print("-" * 50)
    print("Enter the make and model of the board.")
    print("Example: Netgear WNR2000")
    print("If unknown, describe it: 'Unknown Router Board'")
    
    while True:
        board_name = get_input("\nBoard name")
        if board_name:
            return board_name
        print("Board name is required. Please enter a description.")


def get_chip_type():
    """Get chip type with suggestions."""
    print("\nCommon chip types:")
    print("  MCU, Memory, Ethernet PHY, USB Controller")
    print("  Power Management, Sensor, ADC, DAC, RTC")
    print("  GPIO Expander, LED Driver, Display Controller")
    print("  Unknown IC")
    
    return get_input("\nChip type")


def get_address_or_id():
    """Get chip address or ID."""
    print("\nExamples:")
    print("  I²C device: 0x50")
    print("  SPI device: CS0 or device ID like 0xEF4015")
    print("  Physical marking: 24C256, STM32F103")
    print("  USB device: VID:1D50 PID:60E6")
    print("  Unknown: unknown")
    
    return get_input("\nAddress or ID")


def get_interface():
    """Get interface type with validation."""
    print("\nInterface types:")
    print("  I2C, SPI, UART, USB, Ethernet")
    print("  PCIe, GPIO, Analog, Unknown")
    
    return get_input("\nInterface")


def get_condition():
    """Get device condition with validation."""
    valid_conditions = ['working', 'dead', 'unknown', 'partial']
    
    while True:
        print("\nCondition options:")
        print("  working - Device powers on and functions")
        print("  dead - Device does not respond")
        print("  unknown - Not tested")
        print("  partial - Some functions work")
        
        condition = get_input("\nCondition", default="unknown").lower()
        
        if condition in valid_conditions:
            return condition
        
        print(f"Please enter one of: {', '.join(valid_conditions)}")


def get_notes():
    """Get optional notes about the chip."""
    print("\nNotes (optional):")
    print("  Package type, pin count, markings, location on board")
    print("  Unusual behavior, datasheet references, etc.")
    print("  Press Enter to skip.")
    
    return get_input("\nNotes", default="")


def collect_chip_data():
    """Collect data for one chip."""
    print("\n" + "=" * 50)
    
    chip_data = {
        'chip_type': get_chip_type(),
        'address_or_id': get_address_or_id(),
        'interface': get_interface(),
        'condition': get_condition(),
        'notes': get_notes()
    }
    
    return chip_data


def generate_filename(board_name):
    """Generate a filename based on date and board name."""
    # Get current date in YYYYMMDD format
    date_str = datetime.now().strftime("%Y%m%d")
    
    # Clean board name for filename
    # Convert to lowercase, replace spaces with hyphens
    clean_name = board_name.lower().replace(' ', '-')
    
    # Remove any characters that aren't alphanumeric or hyphens
    clean_name = ''.join(c for c in clean_name if c.isalnum() or c == '-')
    
    # Remove consecutive hyphens
    while '--' in clean_name:
        clean_name = clean_name.replace('--', '-')
    
    # Remove leading/trailing hyphens
    clean_name = clean_name.strip('-')
    
    # Truncate if too long
    if len(clean_name) > 50:
        clean_name = clean_name[:50]
    
    filename = f"{date_str}_{clean_name}.csv"
    
    return filename


def save_to_csv(board_name, chips, output_dir='data'):
    """Save collected chip data to CSV file."""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename
    filename = generate_filename(board_name)
    filepath = os.path.join(output_dir, filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        overwrite = get_input(f"\nFile {filename} already exists. Overwrite? (y/n)", default="n")
        if overwrite.lower() != 'y':
            # Generate alternative filename with timestamp
            timestamp = datetime.now().strftime("%H%M%S")
            filename = filename.replace('.csv', f'_{timestamp}.csv')
            filepath = os.path.join(output_dir, filename)
            print(f"Saving as: {filename}")
    
    # Prepare rows with board_name
    rows = []
    for chip in chips:
        row = {'board_name': board_name}
        row.update(chip)
        rows.append(row)
    
    # Write CSV file
    fieldnames = ['board_name', 'chip_type', 'address_or_id', 'interface', 'condition', 'notes']
    
    try:
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"\n✓ Data saved successfully to: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"\n✗ Error saving file: {e}")
        return None


def main():
    print("=" * 60)
    print("Chip Identification Logger")
    print("E-Waste Reverse Engineering Clinic")
    print("=" * 60)
    print("\nThis script will guide you through logging chip identifications.")
    print("All fields except notes are required.")
    print("Press Ctrl+C at any time to cancel.")
    
    try:
        # Get board information
        board_name = get_board_name()
        
        # Get number of chips to log
        while True:
            try:
                num_chips_str = get_input("\nHow many chips do you want to log?", default="1")
                num_chips = int(num_chips_str)
                if num_chips > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Collect data for each chip
        chips = []
        for i in range(num_chips):
            print(f"\n{'=' * 60}")
            print(f"Chip {i + 1} of {num_chips}")
            print(f"{'=' * 60}")
            
            chip_data = collect_chip_data()
            chips.append(chip_data)
            
            # Show summary
            print("\nChip recorded:")
            for key, value in chip_data.items():
                if value:
                    print(f"  {key}: {value}")
        
        # Display summary of all chips
        print("\n" + "=" * 60)
        print("Summary")
        print("=" * 60)
        print(f"Board: {board_name}")
        print(f"Chips: {len(chips)}")
        
        for i, chip in enumerate(chips, 1):
            print(f"\n  Chip {i}:")
            print(f"    Type: {chip['chip_type']}")
            print(f"    ID: {chip['address_or_id']}")
            print(f"    Interface: {chip['interface']}")
        
        # Confirm before saving
        save = get_input("\nSave this data? (y/n)", default="y")
        
        if save.lower() == 'y':
            filepath = save_to_csv(board_name, chips)
            
            if filepath:
                print("\nNext steps:")
                print("1. Review the CSV file to verify accuracy")
                print("2. Add the file to git: git add " + filepath)
                print("3. Commit: git commit -m 'Add chip log for " + board_name + "'")
                print("4. Push and create a pull request")
                print("\nSee CONTRIBUTING.md for detailed instructions.")
        else:
            print("\nData not saved.")
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return
    
    except Exception as e:
        print(f"\nError: {e}")
        print("Please report this issue if it persists.")
        return


if __name__ == "__main__":
    main()
