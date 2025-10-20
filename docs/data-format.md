# Data Format Guide

This document explains how to structure chip identification logs for the E-Waste Reverse Engineering Clinic database. Following this format ensures that data from different contributors can be merged and analyzed consistently.

## CSV Structure

All chip logs should be saved as CSV files in the `data/` directory with this format:

```csv
board_name,chip_type,address_or_id,interface,condition,notes
```

### File Naming Convention

Use this pattern: `YYYYMMDD_board-description.csv`

**Examples:**
- `20250115_netgear-wnr2000-router.csv`
- `20250120_hp-laserjet-1020-printer.csv`
- `20250122_linksys-cable-modem.csv`

## Column Definitions

### board_name (Required)

The make and model of the device or circuit board you are examining.

**Format:** `Manufacturer Model-Number`

**Examples:**
- `Netgear WNR2000`
- `HP LaserJet 1020`
- `Linksys BEFCMU10`
- `Generic USB Hub`

If the manufacturer is unknown, use a descriptive name:
- `Unknown Router Board`
- `Generic Power Supply PCB`

### chip_type (Required)

The function or category of the chip.

**Common Types:**
- `MCU` (Microcontroller)
- `Memory` (EEPROM, Flash, SRAM, DRAM)
- `Ethernet PHY`
- `USB Controller`
- `Power Management`
- `Sensor`
- `ADC` (Analog to Digital Converter)
- `DAC` (Digital to Analog Converter)
- `RTC` (Real-Time Clock)
- `GPIO Expander`
- `LED Driver`
- `Display Controller`
- `Unknown IC`

If you are not sure, use `Unknown IC` and describe what you can see in the notes field.

### address_or_id (Required)

The identifying information for the chip. This varies depending on how you identified it.

**For I²C devices:**
- Use the hexadecimal address: `0x50`, `0x68`, `0x76`

**For SPI devices:**
- Use the chip select line: `CS0`, `CS1`
- Or the device ID if you read it: `0xEF4015`

**For chips identified by markings:**
- Use the part number printed on the chip: `24C256`, `STM32F103`, `RTL8211E`

**For USB devices:**
- Use the vendor and product ID: `VID:1D50 PID:60E6`

If you cannot determine any of these, write `unknown` and describe what you can see in the notes field.

### interface (Required)

The communication protocol or interface used by the chip.

**Standard Values:**
- `I2C`
- `SPI`
- `UART`
- `USB`
- `Ethernet`
- `PCIe`
- `GPIO`
- `Analog`
- `Unknown`

If the chip uses multiple interfaces, list the primary one or the one you used to identify it.

### condition (Required)

The working state of the chip or board.

**Standard Values:**
- `working` (Device powers on and functions)
- `dead` (Device does not respond or is obviously damaged)
- `unknown` (Did not test functionality)
- `partial` (Some functions work, others do not)

Be honest if you did not test it. `unknown` is a valid and useful data point.

### notes (Optional but Recommended)

Any additional observations, context, or details that might be useful.

**Include:**
- Physical package type (SOIC, TSSOP, QFN, DIP, etc.)
- Pin count if you counted
- Visible markings or manufacturer logos
- Location on the board ("near USB connector", "next to power input")
- Any unusual behavior during testing
- References to datasheets you found
- Why you think it is a particular chip type

**Examples:**
- `8-pin SOIC package, 24C series EEPROM family`
- `28-pin SSOP, likely Ethernet PHY based on location near RJ45`
- `No markings visible, covered by thermal compound`
- `Responds to I2C scan but does not match standard addresses`

## Example Entries

### Simple I²C EEPROM

```csv
board_name,chip_type,address_or_id,interface,condition,notes
Netgear WNR2000,Memory,0x50,I2C,unknown,8-pin SOIC package marked 24C256
```

### Microcontroller

```csv
board_name,chip_type,address_or_id,interface,condition,notes
TP-Link TL-WR841N,MCU,AR9331,SPI,working,Main processor - 400MHz MIPS - QFN package
```

### USB Device

```csv
board_name,chip_type,address_or_id,interface,condition,notes
Generic USB Hub,USB Controller,VID:05E3 PID:0608,USB,working,Genesys Logic 4-port hub chip
```

### Unknown Chip

```csv
board_name,chip_type,address_or_id,interface,condition,notes
HP Printer Board,Unknown IC,unknown,Unknown,dead,16-pin SOIC with burn marks - no readable markings
```

## Complete Example File

**Filename:** `20250115_netgear-wnr2000.csv`

```csv
board_name,chip_type,address_or_id,interface,condition,notes
Netgear WNR2000,MCU,AR9331,SPI,working,Main MIPS processor - 32MB RAM integrated
Netgear WNR2000,Memory,0x50,I2C,unknown,EEPROM 24C256 - 8-pin SOIC - likely stores MAC and config
Netgear WNR2000,Memory,W25Q32BV,SPI,working,32Mb Flash - 8-pin SOIC - stores firmware
Netgear WNR2000,Ethernet PHY,AR8035,Ethernet,working,Single-port Gigabit PHY - 32-pin QFN
Netgear WNR2000,Power Management,AMS1117,Analog,working,3.3V LDO regulator - SOT-223 package
```

## Extended Fields

You can add custom fields for specific use cases, but keep the core fields consistent. Add new columns to the right of the standard ones.

**Example with custom field:**

```csv
board_name,chip_type,address_or_id,interface,condition,notes,salvage_priority
HP LaserJet 1020,Memory,0x50,I2C,working,256Kb EEPROM,high
HP LaserJet 1020,USB Controller,VID:03F0 PID:0517,USB,working,Standard HP interface,low
```

## Using the log_to_csv.py Script

The repository includes a helper script to create properly formatted logs.

```bash
python3 scripts/log_to_csv.py
```

The script will prompt you for:

1. Board name
2. Number of chips to log
3. For each chip:
   - Chip type
   - Address or ID
   - Interface
   - Condition
   - Notes

It will generate a timestamped CSV file in the `data/` directory.

### Script Example Session

```
Board name: Netgear WNR2000
How many chips to log? 3

Chip 1 of 3
Chip type: MCU
Address or ID: AR9331
Interface: SPI
Condition (working/dead/unknown): working
Notes: Main MIPS processor

Chip 2 of 3
Chip type: Memory
Address or ID: 0x50
Interface: I2C
Condition (working/dead/unknown): unknown
Notes: EEPROM 24C256

Chip 3 of 3
Chip type: Memory
Address or ID: W25Q32BV
Interface: SPI
Condition (working/dead/unknown): working
Notes: 32Mb Flash

Data saved to: data/20250115_netgear-wnr2000.csv
```

## Data Quality Guidelines

### Be Specific

Instead of "chip near the USB port", write "USB controller chip - GL850G - 28-pin SSOP - 2cm from USB-A connector".

### Be Accurate

If you are not sure, say so. "Possibly an EEPROM based on I2C address 0x50" is better than claiming it is definitely a 24C256.

### Be Consistent

Use the same terminology and format as existing logs. This makes the data more useful for analysis.

### Be Complete

Fill in all required fields. A partial log with missing data is harder to work with than a complete log that says "unknown" in some fields.

## Common Mistakes

### Using Quotes in CSV

Do not use quotes unless the field contains a comma:

**Wrong:**
```csv
"Netgear WNR2000","MCU","AR9331","SPI","working","Main processor"
```

**Right:**
```csv
Netgear WNR2000,MCU,AR9331,SPI,working,Main processor
```

**Right (with comma in notes):**
```csv
Netgear WNR2000,MCU,AR9331,SPI,working,"Main processor, 400MHz MIPS"
```

### Inconsistent Terminology

Pick one term and stick with it:

- Use `I2C`, not `I²C`, `i2c`, or `I-squared-C`
- Use `MCU`, not `microcontroller`, `uC`, or `mcu`
- Use `0x` prefix for hex addresses: `0x50`, not `50` or `0x50h`

### Missing Notes

The notes field is optional but incredibly valuable. Even a simple note like "8-pin package" helps the next person identify a similar chip faster.

## Submitting Your Data

Once you have created a CSV file:

1. Test that it loads without errors:
   ```bash
   python3 -c "import csv; list(csv.DictReader(open('data/your-file.csv')))"
   ```

2. Add it to the repository:
   ```bash
   git add data/your-file.csv
   git commit -m "Add chip identification log for [board name]"
   git push
   ```

3. Open a pull request on GitHub

See `CONTRIBUTING.md` for complete instructions on submitting data.

## Analyzing the Data

The CSV format makes it easy to analyze findings with standard tools.

### Count chips by type

```bash
cut -d',' -f2 data/*.csv | sort | uniq -c
```

### Find all I²C devices

```bash
grep ",I2C," data/*.csv
```

### Load into Python

```python
import csv
import glob

chips = []
for filename in glob.glob('data/*.csv'):
    with open(filename) as f:
        chips.extend(list(csv.DictReader(f)))

# Count by chip type
from collections import Counter
print(Counter(chip['chip_type'] for chip in chips))
```

### Load into a spreadsheet

Open any CSV file in LibreOffice Calc, Excel, or Google Sheets. Use the comma as the delimiter.

## Questions?

If you are not sure how to log something or have a case that does not fit this format, open an issue on GitHub or ask at a workshop. We can update this guide based on real-world usage.

The goal is useful data, not perfect data. Do your best and document what you find.
