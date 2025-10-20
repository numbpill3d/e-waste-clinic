# Datasheets and Reference Materials

This directory contains datasheets, application notes, and reference materials for chips commonly found in e-waste electronics.

## Organization

Files are organized by chip family or manufacturer to make them easy to find during workshops.

```
datasheets/
├── README.md (this file)
├── memory/
│   ├── eeprom/
│   │   ├── 24C256_datasheet.pdf
│   │   └── AT24C_series.pdf
│   └── flash/
│       ├── W25Q32_datasheet.pdf
│       └── MX25L_series.pdf
│
├── microcontrollers/
│   ├── arm/
│   │   ├── STM32F103_datasheet.pdf
│   │   └── LPC1768_datasheet.pdf
│   └── mips/
│       └── AR9331_datasheet.pdf
│
├── networking/
│   ├── ethernet/
│   │   ├── RTL8211E_datasheet.pdf
│   │   └── KSZ8081_datasheet.pdf
│   └── wifi/
│       └── ESP8266_datasheet.pdf
│
├── power/
│   ├── regulators/
│   │   ├── AMS1117_datasheet.pdf
│   │   └── LM7805_datasheet.pdf
│   └── pmic/
│       └── TPS65217_datasheet.pdf
│
├── sensors/
│   ├── environmental/
│   │   ├── BME280_datasheet.pdf
│   │   └── DHT22_datasheet.pdf
│   └── motion/
│       └── MPU6050_datasheet.pdf
│
├── interfaces/
│   ├── usb/
│   │   ├── FT232_datasheet.pdf
│   │   └── CH340_datasheet.pdf
│   └── serial/
│       └── MAX232_datasheet.pdf
│
├── reference_guides/
│   ├── i2c_address_list.pdf
│   ├── usb_device_classes.pdf
│   ├── chip_package_types.pdf
│   └── pin_numbering_guide.pdf
│
└── app_notes/
    ├── i2c_bus_debugging.pdf
    ├── spi_protocol_basics.pdf
    └── chip_identification_tips.pdf
```

## Adding Datasheets

### Before You Add

1. **Check if it already exists** - Search the folder first
2. **Use official sources** - Get datasheets from manufacturer websites when possible
3. **Verify the version** - Make sure it matches the chip revision you have
4. **Check file size** - Optimize PDFs if they are over 5MB

### File Naming Convention

Use this format: `PARTNUMBER_description.pdf`

**Good examples:**
- `STM32F103_datasheet.pdf`
- `24C256_eeprom_datasheet.pdf`
- `RTL8211E_ethernet_phy.pdf`
- `AMS1117_3.3V_regulator.pdf`

**Bad examples:**
- `datasheet.pdf` (not specific)
- `DS-STM32F103-Rev3.pdf` (manufacturer naming)
- `stm32 datasheet.pdf` (spaces in filename)

### Where to Put It

Place datasheets in the most specific folder that applies:

- Memory chips → `memory/eeprom/` or `memory/flash/`
- Microcontrollers → `microcontrollers/arm/` or `microcontrollers/mips/`
- Ethernet PHYs → `networking/ethernet/`
- Voltage regulators → `power/regulators/`
- Sensors → `sensors/environmental/` or `sensors/motion/`
- USB chips → `interfaces/usb/`

If unsure, put it in the top-level category folder.

### Add a Reference Entry

After adding a datasheet, update the index at the bottom of this README:

```
- **STM32F103**: 32-bit ARM Cortex-M3 MCU, common in cheap dev boards
  Location: microcontrollers/arm/STM32F103_datasheet.pdf
```

## Finding Datasheets

### Official Sources (Best)

1. **Manufacturer websites**
   - Go directly to chip maker's site
   - Look for "Products" or "Documentation" section
   - Download official PDF

2. **Distributor sites**
   - DigiKey: digikey.com
   - Mouser: mouser.com
   - Search by part number, download from product page

### Aggregator Sites (Good)

1. **Octopart**: octopart.com
   - Aggregates from many sources
   - Shows multiple datasheet versions

2. **Alldatasheet**: alldatasheet.com
   - Large PDF collection
   - Sometimes outdated versions

3. **Datasheetspdf**: datasheetspdf.com
   - PDF archive
   - Watch for broken links

### Search Engines (Okay)

Google: `PARTNUMBER datasheet filetype:pdf`

Be careful:
- Verify source is legitimate
- Check file for malware
- Compare multiple sources if uncertain

## What NOT to Include

Do not add:
- Copyrighted materials without permission
- Marketing brochures (not technical docs)
- User manuals for complete devices
- Files over 10MB (link instead)
- Proprietary internal documents
- Files with unclear licensing

## Optimizing PDF Files

If a datasheet is huge, compress it:

```bash
# Using Ghostscript
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH \
   -sOutputFile=output.pdf input.pdf

# Or use online tools
# pdfresize.com
# ilovepdf.com/compress_pdf
```

Aim for under 2MB when possible.

## Reference Materials

### I²C Address Quick Reference

Common addresses you will see in workshops:

```
0x20-0x27  GPIO Expanders (PCF8574, MCP23008)
0x48-0x4F  ADC / Temperature Sensors (ADS1115, LM75)
0x50-0x57  EEPROM Memory (24C series)
0x60-0x6F  Display Drivers / LED Controllers
0x68-0x69  Real-Time Clocks (DS1307, DS3231) / IMU (MPU6050)
0x76-0x77  Environmental Sensors (BME280, BMP180)
0x3C-0x3D  OLED Displays (SSD1306)
```

### Common Chip Families

**Memory:**
- 24Cxx: I²C EEPROM (xx = size in Kbits)
- 25xxx: SPI EEPROM
- W25Qxx: SPI Flash (xx = size in Mbits)
- MX25Lxx: SPI Flash

**Microcontrollers:**
- STM32: ARM Cortex-M series by ST
- ATmega: AVR series by Atmel/Microchip
- ESP8266/ESP32: WiFi-enabled MCUs
- PIC: Microchip's PIC series

**Ethernet PHY:**
- RTL82xx: Realtek Ethernet controllers
- KSZ80xx: Microchip Ethernet PHY
- LAN87xx: Microchip/SMSC Ethernet

**USB:**
- FT232: FTDI USB-to-serial
- CH340: Chinese USB-to-serial
- CP210x: Silicon Labs USB-to-UART

**Power:**
- AMS1117: Low-dropout regulator (3.3V common)
- LM78xx: Linear voltage regulators
- TPS: Texas Instruments power management

### Package Types

Common chip packages you will encounter:

**Through-Hole:**
- DIP (Dual Inline Package): Easy to identify and desolder
- SIP (Single Inline Package): Less common

**Surface Mount:**
- SOIC (Small Outline IC): 8-28 pins, 1.27mm pitch
- TSSOP (Thin Shrink Small Outline): Thinner than SOIC
- QFN (Quad Flat No-leads): Very small, difficult to probe
- QFP (Quad Flat Package): 32+ pins with visible leads
- BGA (Ball Grid Array): Balls underneath, cannot see pins

### Reading Chip Markings

Most chips have these markings:

```
Line 1: Manufacturer logo or code
Line 2: Part number
Line 3: Date code (YYWW = year + week)
Line 4: Batch/revision code
```

Example marking:
```
[M logo]        → Manufacturer: STMicroelectronics
STM32F103C8     → Part number
CHN 936         → Made in China, week 36 of 2009 (or 2019)
```

Date codes vary:
- YYWW: 2136 = year 2021, week 36
- YWW: 936 = year 2009 or 2019, week 36
- Julian: Some use day of year

## Using Datasheets in Workshops

### Quick Chip ID Process

1. **Find the chip physically**
   - Look near connectors and power inputs
   - Check for chips with many pins

2. **Read the markings**
   - Use magnification if needed
   - Write down everything visible
   - Take photos if markings are unclear

3. **Look up the part number**
   - Search this folder first
   - Use chip_lookup.py script
   - Download if not present

4. **Verify the match**
   - Compare pin count
   - Check package type
   - Look at application notes
   - Verify voltage ratings

5. **Document it**
   - Add to log with notes
   - Share interesting findings
   - Add datasheet if useful

### What to Look for in Datasheets

When reading a datasheet during a workshop:

**Page 1: Overview**
- What does the chip do?
- Key features and specifications

**Pinout Diagram:**
- Which pins are power?
- Where are I²C/SPI pins?
- Any special function pins?

**Electrical Characteristics:**
- Operating voltage
- Current consumption
- Communication speeds

**Application Notes:**
- Example circuits
- Common uses
- Troubleshooting tips

## Contributing Datasheets

### Via Pull Request

1. Add the PDF to appropriate folder
2. Update this README with an index entry
3. Commit with message: "Add datasheet for [PARTNUMBER]"
4. Open pull request

### Include This Info

In your pull request description:

```
Chip: STM32F103C8T6
Family: ARM Cortex-M3 Microcontroller
Source: st.com (official)
Revision: Rev 18
File size: 1.8MB
Use case: Found in cheap "Blue Pill" dev boards and many routers

Notes: This is the most common variant. Other STM32F103 models
have similar specs but different memory sizes.
```

### License Considerations

Most datasheets are freely available but copyrighted:

- Manufacturer datasheets: Usually free to redistribute
- Third-party guides: Check license first
- Application notes: Usually okay to share
- Proprietary docs: Do not share without permission

When in doubt, link to the source instead of hosting.

## Quick Reference Index

Add your contributed datasheets here alphabetically:

### Memory

**EEPROM (I²C):**
- **24C256**: 256Kbit I²C EEPROM, 0x50-0x57 address range
- **AT24C series**: Atmel/Microchip I²C EEPROM family

**Flash (SPI):**
- **W25Q32**: 32Mbit SPI Flash, common in routers
- **MX25L series**: Macronix SPI Flash family

### Microcontrollers

**ARM:**
- **STM32F103**: 32-bit ARM Cortex-M3, extremely common in cheap boards

**MIPS:**
- **AR9331**: Atheros WiFi SoC, used in many routers

### Networking

**Ethernet PHY:**
- **RTL8211E**: Realtek Gigabit Ethernet PHY
- **KSZ8081**: Microchip 10/100 Ethernet PHY

### Power Management

**Regulators:**
- **AMS1117**: 1A LDO regulator, very common (3.3V variant)
- **LM7805**: Classic 5V linear regulator

### USB

- **FT232**: FTDI USB-to-serial converter
- **CH340**: Chinese USB-to-serial, very cheap and common

### Sensors

**Environmental:**
- **BME280**: Combined humidity, pressure, temperature sensor

**Motion:**
- **MPU6050**: 6-axis IMU (accelerometer + gyroscope)

(Add more as datasheets are contributed)

## Workshop Tips

### Pre-Workshop Prep

Print or have ready:
- I²C address reference (one page)
- Common chip family guide (one page)
- Package type identification sheet
- Pin numbering guide for different packages

### During Workshop

Keep laptops available for:
- Searching this folder
- Looking up unfamiliar chips
- Downloading new datasheets
- Cross-referencing specifications

### After Workshop

Add any useful datasheets you downloaded to this folder for next time.

## Maintenance

### Regular Tasks

- Remove broken/dead links
- Update to newer datasheet revisions
- Reorganize if folders get messy
- Keep index up to date

### File Cleanup

Every few months:
- Check for duplicates
- Remove rarely-used files
- Verify links still work
- Optimize large PDFs

## External Resources

### Online Databases

- **I²C Device Database**: i2cdevices.org/addresses
- **USB ID Database**: the-sz.com/products/usbid
- **Pinout Directory**: pinouts.org

### Communities

- **EEVblog Forums**: eevblog.com/forum
- **r/AskElectronics**: reddit.com/r/AskElectronics
- **Hackaday**: hackaday.io

### Learning Resources

- **SparkFun Tutorials**: learn.sparkfun.com
- **Adafruit Learning**: learn.adafruit.com
- **All About Circuits**: allaboutcircuits.com

## Questions?

If you need help finding a datasheet or understanding how to read one:

- Ask in GitHub issues
- Email: splicer@hiddenlayermedia.com
- Bring questions to workshops
- Search online electronics forums

Remember: Learning to read datasheets is a skill. Start with the sections you need (pinout, voltage) and gradually learn to parse the rest.

## License

The datasheets themselves are copyrighted by their respective manufacturers. This README and the organizational structure are licensed under CC-BY-SA 4.0.

When sharing datasheets, always credit the original manufacturer and link to official sources when possible.
