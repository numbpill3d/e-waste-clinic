# GreatFET Setup Instructions

This guide will help you install and use GreatFET tools for probing chips and collecting data at E-Waste Reverse Engineering Clinic workshops.

## What is GreatFET?

GreatFET One is an open hardware USB tool for testing and interacting with electronic devices. It can act as a logic analyzer, protocol sniffer, or general-purpose interface for talking to chips. We use it to probe I²C and SPI buses on circuit boards and identify chips.

## What You Need

- GreatFET One hardware (available from Great Scott Gadgets)
- USB cable (usually included)
- Computer running Linux or Windows
- Python 3.7 or newer
- Basic command line knowledge

## Installation on Linux

### Step 1: Install Python and pip

Most Linux distributions come with Python installed. Check your version:

```bash
python3 --version
```

If you need to install Python:

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

### Step 2: Install GreatFET Software

```bash
pip3 install --user greatfet
```

This installs the GreatFET Python library and command line tools.

### Step 3: Add Your User to the plugdev Group

This lets you access USB devices without root permissions:

```bash
sudo usermod -a -G plugdev $USER
```

Log out and log back in for this to take effect.

### Step 4: Install udev Rules

Create a file at `/etc/udev/rules.d/54-greatfet.rules` with this content:

```
SUBSYSTEM=="usb", ATTR{idVendor}=="1d50", ATTR{idProduct}=="60e6", MODE="0660", GROUP="plugdev"
```

Reload udev rules:

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### Step 5: Test the Installation

Plug in your GreatFET and run:

```bash
greatfet_info
```

You should see information about your device including serial number and firmware version.

If you get a "device not found" error, try:

- Unplugging and replugging the device
- Checking that you are in the plugdev group (run `groups` to verify)
- Rebooting your computer

## Installation on Windows

### Step 1: Install Python

Download Python from python.org. Make sure to check the box that says "Add Python to PATH" during installation.

Open Command Prompt and verify:

```cmd
python --version
```

### Step 2: Install GreatFET Software

```cmd
pip install greatfet
```

### Step 3: Install Zadig Driver

Windows needs a special USB driver for GreatFET.

1. Download Zadig from zadig.akeo.ie
2. Run Zadig as Administrator
3. Plug in your GreatFET
4. In Zadig, select Options > List All Devices
5. Select "GreatFET One" from the dropdown
6. Choose "WinUSB" as the driver
7. Click "Install Driver" or "Replace Driver"

### Step 4: Test the Installation

```cmd
greatfet_info
```

You should see device information. If not, try restarting your computer and running the command again.

## Using the Workshop Scripts

The E-Waste Clinic repository includes Python scripts for common tasks. Clone the repository:

```bash
git clone https://github.com/splicer/e-waste-clinic.git
cd e-waste-clinic
```

### I²C Probe Script

This script scans for I²C devices on a circuit board and reports their addresses.

```bash
python3 scripts/i2c_probe.py
```

**Example Output:**

```
GreatFET I²C Scanner
Scanning addresses 0x00 to 0x7F...

Found devices:
  0x50 - EEPROM (likely 24C series)
  0x68 - Real-time clock or sensor
  0x76 - Pressure sensor (BME280 or similar)

Scan complete. Found 3 devices.
```

**Common I²C Addresses:**

- 0x50-0x57: EEPROMs
- 0x68: Real-time clocks, IMU sensors
- 0x76-0x77: Environmental sensors
- 0x3C-0x3D: OLED displays
- 0x48-0x4F: ADCs, temperature sensors

### USB Enumeration Script

This script reads USB device descriptors and identifies connected devices.

```bash
python3 scripts/usb_enum.py
```

**Example Output:**

```
USB Device Enumerator

Device: Keyboard
  Vendor ID: 0x046d
  Product ID: 0xc31c
  Manufacturer: Logitech
  Product: USB Keyboard

Device: GreatFET One
  Vendor ID: 0x1d50
  Product ID: 0x60e6
  Manufacturer: Great Scott Gadgets
  Product: GreatFET One

Found 2 devices.
```

### Data Logging Script

This script converts your probe findings into a properly formatted CSV file.

```bash
python3 scripts/log_to_csv.py
```

The script will prompt you for information about the board and chips you found. It saves the data to the `data/` directory with a timestamped filename.

## Interpreting Results

### I²C Address Meanings

When you find an I²C device, the address gives you a clue about what kind of chip it is:

- Multiple devices at 0x50-0x57 usually means EEPROM memory chips
- A device at 0x68 is often a real-time clock or motion sensor
- Addresses 0x20-0x27 are often GPIO expanders or LED drivers

Look up the address in datasheets or online I²C address databases to narrow down possibilities. Then physically inspect the chip to confirm the part number.

### USB Device Classes

USB devices report a class code that indicates their function:

- Class 03: HID (keyboard, mouse, gamepad)
- Class 08: Mass storage (flash drive, hard drive)
- Class 0A: CDC (serial port, modem)
- Class 0E: Video (webcam)
- Class 01: Audio (speakers, microphone)

The vendor ID and product ID can be looked up in USB ID databases to find the exact manufacturer and model.

## Troubleshooting

### Device Not Found

**Linux:**
- Check that you are in the plugdev group: `groups`
- Verify udev rules are installed: `ls /etc/udev/rules.d/54-greatfet.rules`
- Try running with sudo (not recommended for regular use): `sudo greatfet_info`

**Windows:**
- Check Device Manager for the GreatFET device
- Reinstall the WinUSB driver using Zadig
- Try a different USB port

### Permission Denied

**Linux:**
- Make sure you logged out and back in after adding yourself to plugdev
- Check udev rules are correct and loaded
- Run `sudo udevadm trigger` to reload

### No I²C Devices Found

- Check your wiring connections to the board
- Verify the board is powered on
- Try slower I²C speeds (add `--speed 100000` flag)
- Some boards need pull-up resistors on SDA and SCL lines

### Script Errors

If a script fails with an import error:

```bash
pip3 install --user greatfet pyserial
```

If you get "command not found" for greatfet_info:

```bash
# Linux
export PATH="$HOME/.local/bin:$PATH"

# Windows
# Add %APPDATA%\Python\Python3X\Scripts to your PATH in System Environment Variables
```

## Wiring Guide

### I²C Connection

Connect GreatFET pins to the target board:

- GreatFET Pin 2 (SDA) to board's SDA line
- GreatFET Pin 3 (SCL) to board's SCL line
- GreatFET GND to board's GND

If the board is not powered, you may also need to connect:

- GreatFET 3.3V or 5V to board's power input

**Always check the voltage requirements of your target board before connecting power.**

### SPI Connection

For SPI probing:

- GreatFET MOSI to board's MOSI
- GreatFET MISO to board's MISO
- GreatFET SCK to board's SCK
- GreatFET CS to board's CS
- GreatFET GND to board's GND

## Safety Notes

- Never connect GreatFET to powered circuits above 5V without level shifters
- Check polarity before connecting power
- Disconnect power before changing wiring
- Use a current-limited power supply when testing unknown boards
- Do not short VCC to GND
- Watch out for capacitors that may hold charge even when power is disconnected

## Next Steps

Once you have GreatFET working:

1. Practice on a known-good board to verify your setup
2. Start with simple devices like USB keyboards or mice
3. Work up to more complex boards like routers or printers
4. Document your findings using the data logging script
5. Share your results in the project repository

## Additional Resources

- GreatFET documentation: greatscottgadgets.com/greatfet
- I²C address database: i2cdevices.org/addresses
- USB ID database: the-sz.com/products/usbid
- Chip identification guides: In `resources/datasheets/` directory

## Getting Help

If you run into problems:

1. Check this troubleshooting section
2. Search the GreatFET GitHub issues
3. Ask in the E-Waste Clinic repository discussions
4. Email splicer@hiddenlayermedia.com
5. Bring your device to a workshop for hands-on help

Remember: Getting stuck is part of the learning process. Everyone goes through this. Ask for help when you need it.
