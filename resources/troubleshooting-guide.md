# Workshop Troubleshooting Guide

Quick solutions to common problems encountered during E-Waste Reverse Engineering Clinic workshops.

## GreatFET Issues

### GreatFET Not Recognized

**Symptoms:**
- Computer does not detect device
- `greatfet_info` returns "device not found"
- USB connection seems dead

**Solutions:**

**Try Different USB Port**
- Some ports have better power/data connections
- Avoid USB hubs when possible
- Try USB 2.0 port instead of 3.0
- Front panel ports may be less reliable

**Check USB Cable**
- Many cables are power-only, no data
- Try a known-good cable
- Shorter cables are more reliable
- Look for damage or kinks

**Restart Computer**
- Clears USB stack issues
- Reloads drivers
- Fresh start often helps

**Linux: Check Permissions**
```bash
# Check if user is in plugdev group
groups

# If not, add user
sudo usermod -a -G plugdev $USER

# Log out and back in
```

**Linux: Reload udev Rules**
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

**Windows: Reinstall Driver**
- Use Zadig to reinstall WinUSB driver
- Run as Administrator
- Select correct device
- Choose WinUSB driver

**Last Resort: Try Different Computer**
- Helps isolate if issue is device or computer

### GreatFET Connects But Scripts Fail

**Symptoms:**
- Device recognized
- Scripts return errors
- I²C scan fails immediately

**Solutions:**

**Update Firmware**
```bash
greatfet_firmware --auto
```

**Check Python Version**
```bash
python3 --version
# Should be 3.7 or newer
```

**Reinstall GreatFET Software**
```bash
pip3 uninstall greatfet
pip3 install --user greatfet
```

**Check for Multiple Python Installations**
```bash
which python3
which pip3
# Should point to same location
```

**Run with Verbose Output**
```bash
python3 scripts/i2c_probe.py -v
# Helps identify specific error
```

## I²C Scanning Issues

### No Devices Found

**Symptoms:**
- Scan completes but finds nothing
- All addresses return errors
- Known-good boards show empty

**Solutions (Try in Order):**

**1. Check Physical Connections**
- Verify SDA wire connected
- Verify SCL wire connected  
- Verify GND connected
- Check for loose connections
- Look for broken wires

**2. Verify Target Board Has Power**
```bash
# Use multimeter
# Check for 3.3V or 5V on VCC pins
# Check that voltage is stable
```

**3. Try Slower Speed**
```bash
python3 scripts/i2c_probe.py --speed 100000
# Default is 400000 (fast mode)
# 100000 is standard mode
```

**4. Check for Pull-Up Resistors**
- I²C requires pull-ups on SDA and SCL
- Typical values: 4.7K ohm
- Check with multimeter (resistance mode)
- Measure between SDA/SCL and VCC
- Should read 4.7K or close

**5. Test with Known-Good Board**
- Helps determine if issue is GreatFET or target
- Use Arduino with I²C chip
- Use proven working board from past workshop

**6. Check Wiring Diagram**
- GreatFET Pin 2 = SDA
- GreatFET Pin 3 = SCL
- GreatFET GND = Target GND
- Double-check pin numbers

**7. Look for Shorts**
```bash
# Disconnect power
# Use multimeter in continuity mode
# Check SDA to GND (should be open)
# Check SCL to GND (should be open)
# Check SDA to SCL (should be open)
```

### Scan Freezes or Hangs

**Symptoms:**
- Scan starts but never completes
- Computer becomes unresponsive
- Must force-quit script

**Solutions:**

**Bus Lockup**
- Power cycle target board
- Disconnect and reconnect GreatFET
- Restart Python script

**Bad Chip on Bus**
- One misbehaving chip can freeze entire bus
- Try scanning smaller address ranges
- Skip problematic addresses manually

**Timing Issues**
- Reduce scan speed
- Add delays between probes
- Use timeout parameter if available

### Wrong Devices Detected

**Symptoms:**
- Finds addresses but wrong chips
- Same address on different boards
- Results do not match physical inspection

**Solutions:**

**Address Confusion**
- Some addresses are very common (0x50, 0x68)
- Multiple chip families use same addresses
- Context matters (near Ethernet = PHY, etc.)

**Address Pin Configuration**
- Check A0, A1, A2 pins on chip
- Calculate actual address based on pins
- Base address + pin values = final address

**Multiple Devices**
- Some boards have multiple chips at 0x50-0x57
- Each has different address pin configuration
- Use visual inspection to confirm count

## USB Enumeration Issues

### Permission Denied

**Linux Only:**

**Symptoms:**
- Script cannot access USB devices
- "Permission denied" errors
- Works with sudo but not without

**Solutions:**

**Add User to Correct Group**
```bash
# For Debian/Ubuntu
sudo usermod -a -G plugdev $USER

# For Fedora/RHEL  
sudo usermod -a -G usbusers $USER

# Log out and back in
```

**Check udev Rules**
```bash
# Verify rules exist
ls /etc/udev/rules.d/*usb*

# If missing, create them
# Then reload
sudo udevadm control --reload-rules
```

### No USB Devices Found

**Symptoms:**
- Script runs but finds nothing
- Even obvious devices missing
- Works on other computers

**Solutions:**

**Install pyusb**
```bash
pip3 install --user pyusb
```

**Install libusb**
```bash
# Debian/Ubuntu
sudo apt install libusb-1.0-0

# Fedora
sudo dnf install libusb

# macOS
brew install libusb
```

**Check USB Subsystem**
```bash
# Linux: Use lsusb
lsusb
# Should show all connected devices

# Windows: Check Device Manager
# Look for USB devices
```

### Incorrect Device Info

**Symptoms:**
- Vendor ID shows as 0000
- Product strings are gibberish
- Device class is wrong

**Solutions:**

**Some Devices Have Minimal Descriptors**
- Cheap devices skimp on USB descriptors
- This is normal for some hardware
- Focus on VID/PID which are more reliable

**Update USB ID Database**
```bash
# Linux
sudo update-usbids

# Or download fresh database from:
# http://www.linux-usb.org/usb.ids
```

## Data Logging Issues

### Script Crashes

**Symptoms:**
- log_to_csv.py throws error
- Cannot save file
- Permission denied

**Solutions:**

**Check data/ Directory Exists**
```bash
mkdir -p data
```

**Check Write Permissions**
```bash
ls -la data/
# Should be writable by user
```

**Try Different Filename**
- Avoid special characters
- Use only letters, numbers, hyphens, underscores
- Keep names short

**Check Disk Space**
```bash
df -h
# Ensure space available
```

### Invalid CSV Format

**Symptoms:**
- CSV will not open in spreadsheet
- Errors when analyzing data
- Columns misaligned

**Solutions:**

**Check for Commas in Data**
- Commas in notes field break CSV
- Use semicolons instead
- Or wrap in quotes (the script should do this)

**Check Line Endings**
- Windows vs Unix line endings
- Use dos2unix or unix2dos to convert
- Most tools handle both now

**Verify Column Count**
- Each row must have same number of columns
- Check for extra commas
- Check for missing columns

## Chip Identification Issues

### Cannot Read Markings

**Symptoms:**
- Text too small to read
- Markings worn off
- Cannot focus on chip

**Solutions:**

**Better Magnification**
- Use USB microscope (20-40x)
- Use phone camera with zoom
- Use magnifying glass with light
- Try different angles and lighting

**Better Lighting**
- Use flashlight or desk lamp
- Try raking light (angle from side)
- Reduce glare with diffuser
- Take photo and enhance contrast

**Clean the Chip**
- Use isopropyl alcohol and cotton swab
- Gently rub markings
- Let dry completely
- Try reading again

**Alternative Methods**
- Use I²C address to narrow down options
- Check board silk screen for clues
- Look up board model number
- Find service manual or schematic

### Datasheet Does Not Match

**Symptoms:**
- Pin count wrong
- Package type wrong
- Part number similar but not exact

**Solutions:**

**Chip Variants**
- Many chips have multiple variants
- Suffix letters indicate differences
- STM32F103C8T6 vs STM32F103C8T7
- Check datasheet carefully

**Compatible Parts**
- Different manufacturers make compatible chips
- W25Q32 vs GD25Q32 (similar but not identical)
- Check "pin-compatible" or "equivalent" parts

**Counterfeit Chips**
- Some chips are remarked or fake
- Markings may be incorrect
- Compare with photos of genuine parts
- Check if board works (fake may not)

### Wrong Chip Type Identified

**Symptoms:**
- Thought it was EEPROM, actually RTC
- Address matches multiple chip types
- Board context does not make sense

**Solutions:**

**Use Context Clues**
- Near Ethernet jack = probably PHY
- Near power input = probably regulator
- Near main processor = probably memory
- Near display = probably display driver

**Check I²C Address Carefully**
- 0x50 = almost always EEPROM
- 0x68 = could be RTC or IMU (check board type)
- 0x76 = usually environmental sensor

**Read Chip Markings**
- Part number is most reliable
- Logo helps identify manufacturer
- Date code confirms age

**Cross-Reference Multiple Sources**
- Check multiple datasheet sites
- Search for board model number
- Look for teardown articles
- Check manufacturer datasheets directly

## Participant Issues

### Participant Is Struggling

**Symptoms:**
- Falling behind group
- Looks confused or frustrated
- Not asking questions

**Solutions:**

**Check In Privately**
- Pull them aside during break
- Ask how they are doing
- Identify specific confusion
- Offer extra help

**Pair with Helper**
- Match with more experienced person
- Encourage peer teaching
- Check back frequently

**Simplify Task**
- Give easier board
- Focus on visual inspection only
- Skip technical details
- Let them work at own pace

**Provide Extra Resources**
- Give printed guides
- Show specific examples
- Draw diagrams
- Use analogies

### Participant Is Bored

**Symptoms:**
- Finished early
- Looking at phone
- Not engaged

**Solutions:**

**Provide Challenge**
- Give more complex board
- Ask to help troubleshoot
- Dive deeper into datasheets
- Introduce advanced techniques

**Leverage Their Skills**
- Ask them to help others
- Have them document findings
- Request their expertise
- Engage in deeper discussion

**Different Activity**
- Start soldering/desoldering
- Explore power supplies
- Reverse engineer protocol
- Work on personal project

### Participant Dominating

**Symptoms:**
- Talking over others
- Answering all questions
- Taking over group work
- Others becoming quiet

**Solutions:**

**Redirect Privately**
- Pull aside during break
- Thank them for enthusiasm
- Ask them to help others instead
- Set expectations for group dynamics

**Facilitate Inclusively**
- "Let's hear from someone who hasn't spoken yet"
- "Good point! Who else has thoughts?"
- "Everyone take 30 seconds to think before sharing"
- Call on quieter participants directly

**Give Them a Job**
- Ask them to document on board
- Have them help with cleanup
- Request they assist struggling participants
- Channel energy productively

### Safety Violation

**Symptoms:**
- Not wearing safety glasses when required
- Working on dangerous voltage
- Horseplay with tools
- Ignoring safety rules

**Solutions:**

**Address Immediately**
- Stop the behavior right away
- Explain the specific danger
- Reiterate safety rules
- Be firm but not harsh

**Private Conversation if Needed**
- Pull them aside
- Explain why rule exists
- Consequences of violations
- Offer to answer questions

**Remove from Workshop if Serious**
- Multiple violations
- Refusal to comply
- Putting others at risk
- Document the incident

## Equipment Issues

### Tool Shortage

**Symptoms:**
- Not enough GreatFET units
- Participants waiting for tools
- Sharing causing delays

**Solutions:**

**Rotate Tools**
- Set time limits per station
- Create schedule for sharing
- Parallel activities (some visual ID while others probe)

**Partner Up**
- Two people per station
- Take turns using tools
- Encourages collaboration

**Prioritize Activities**
- Focus on what tools enable
- Skip optional advanced sections
- Save technical work for smaller groups

### Power Issues

**Symptoms:**
- Not enough outlets
- Circuit breaker trips
- Devices not charging

**Solutions:**

**Bring More Power Strips**
- Always have extras
- Distribute around room
- Check amp rating

**Reduce Load**
- Unplug unused devices
- Turn off extra laptops
- Stagger power usage

**Check Circuit Rating**
- Know venue's electrical limits
- Spread load across multiple circuits
- Have backup plan

### WiFi Problems

**Symptoms:**
- Cannot connect to internet
- Slow or dropped connections
- Too many devices

**Solutions:**

**Use Mobile Hotspot**
- Have backup cellular data
- Limit connected devices
- Prioritize essential connections

**Download Resources Ahead**
- Cache datasheets locally
- Have offline copies of docs
- Prepare USB drives with files

**Adapt Activities**
- Focus on offline tasks
- Use printed materials
- Work from local copies

## Time Management Issues

### Running Behind Schedule

**Symptoms:**
- Still on intro at planned hands-on time
- Will not finish planned activities
- Group is slower than expected

**Solutions:**

**Cut Less Critical Content**
- Skip advanced topics
- Abbreviate intro
- Focus on core skills
- Provide resources for self-study

**Extend Key Activities**
- Give more time for hands-on
- Cut wrap-up short
- Email follow-up instead

**Split Group**
- Fast group continues
- Slower group gets more support
- Reconvene for wrap-up

### Finishing Too Early

**Symptoms:**
- Completed all planned activities
- Still have 30+ minutes
- Group energy still high

**Solutions:**

**Extend Current Activity**
- More boards to explore
- Deeper datasheet analysis
- Advanced techniques
- Open Q&A

**Advanced Topic**
- Introduce soldering
- Discuss repair
- Show advanced tools
- Demonstrate tricky chips

**Project Planning**
- Discuss future workshops
- Brainstorm project ideas
- Plan next steps
- Build community

## Documentation Issues

### Photos Are Bad Quality

**Symptoms:**
- Blurry images
- Too dark
- Cannot see details

**Solutions:**

**Better Lighting**
- Use flash or lamp
- Reduce shadows
- Increase room lighting
- Use ring light if available

**Stabilize Camera**
- Rest on table
- Use tripod
- Press against solid object
- Use timer to reduce shake

**Focus Properly**
- Tap to focus (phone)
- Use macro mode
- Get closer to subject
- Use zoom sparingly

**Clean Lens**
- Wipe camera lens
- Remove protective film
- Check for scratches

### Data Not Uploading

**Symptoms:**
- Cannot push to GitHub
- File too large
- Format errors

**Solutions:**

**Check File Size**
- GitHub limits individual files
- Compress images
- Split large datasets
- Link to external storage

**Check Git Configuration**
```bash
git config --list
# Verify user.name and user.email
```

**Authentication Issues**
```bash
# Use personal access token
# Not password
# Check token permissions
```

**Network Issues**
- Try different network
- Check firewall
- Use mobile hotspot
- Retry later

## Wrap-Up

Most issues have simple solutions. The key is staying calm, methodical troubleshooting, and asking for help when needed.

Keep this guide handy during workshops for quick reference.

## Emergency Contact Information

For serious issues beyond this guide:

**Technical Support:**
- GreatFET Discord/Forums
- GitHub Issues
- Email: greatfet@greatscottgadgets.com

**Community Support:**
- Project Email: [YOUR EMAIL]
- GitHub Discussions
- Workshop attendees (build network!)

---

This guide is CC-BY-SA 4.0
E-Waste Reverse Engineering Clinic
Hidden Layer Media | Neon Maxima 2133
Charlotte Hardware Collective

Update this guide based on real problems you encounter!
