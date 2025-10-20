# Workshop Safety Guide

Safety guidelines for E-Waste Reverse Engineering Clinic workshops. These procedures protect participants, equipment, and the workspace.

## Before Every Workshop

### Workspace Preparation

**Electrical Safety Check:**
- Verify all power strips have working circuit breakers
- Check power cables for damage or fraying
- Test GFCI outlets if available
- Keep liquids away from electronics work areas
- Mark emergency shutoff locations

**Ventilation:**
- Open windows if soldering
- Set up fans for air circulation
- Position soldering stations near ventilation
- Keep fire extinguisher accessible
- No soldering in unventilated spaces

**First Aid:**
- First aid kit visible and accessible
- Know location of nearest medical facility
- Have emergency contact numbers posted
- Ice packs available for minor burns
- Eyewash station if using chemicals

**Tool Inspection:**
- Check soldering irons for damaged tips or cords
- Verify multimeters are working
- Inspect wire strippers and cutters for damage
- Test GreatFET units before workshop
- Remove any unsafe or broken tools

## Electrical Safety

### Working with Circuit Boards

**NEVER:**
- Connect to live AC power (wall outlets)
- Work on powered devices without knowing voltage
- Touch capacitors immediately after power removal
- Short circuit batteries
- Connect reversed polarity without checking first

**ALWAYS:**
- Use current-limited power supplies
- Check voltage with multimeter first
- Discharge capacitors before handling
- Keep one hand behind back when probing live circuits
- Assume all capacitors are charged until verified

### Voltage Guidelines

**Safe to Handle:**
- Under 5V DC (USB, logic level signals)
- Battery-powered devices under 12V
- Verified dead circuits

**Use Caution:**
- 12-48V DC (can cause shock)
- Any AC voltage (more dangerous than DC)
- Unknown voltage circuits

**DO NOT WORK ON:**
- Line voltage AC (120V/240V)
- High voltage power supplies
- CRT monitors (up to 25kV!)
- Microwave ovens (lethal voltages)
- Anything connected to wall power

### Capacitor Safety

Large capacitors can hold dangerous charge for hours or days.

**Discharge Procedure:**
1. Disconnect all power
2. Wait at least 5 minutes
3. Use insulated screwdriver across terminals
4. Verify with multimeter
5. Short with wire to be sure

**Warning Signs:**
- Bulging or leaking electrolytic capacitors
- Hissing sounds
- Burnt smell
- Discoloration

Do not handle damaged capacitors.

## Battery Safety

### Lithium Battery Hazards

Lithium batteries can catch fire or explode if:
- Punctured or crushed
- Short-circuited
- Overheated
- Charged incorrectly

**Safe Handling:**
- Inspect for swelling, damage, or leaks
- Never puncture or disassemble
- Store in fire-safe container
- Tape terminals to prevent shorts
- Keep away from metal objects

**If Battery Swells:**
- Stop using immediately
- Move to non-flammable surface
- Keep away from people
- Contact hazardous waste disposal

**If Battery Catches Fire:**
- DO NOT use water
- Use Class D fire extinguisher or sand
- Evacuate area
- Call fire department

### Other Battery Types

**NiMH/NiCd:**
- Less dangerous than lithium
- Can still short-circuit and heat up
- Tape terminals when storing

**Lead-Acid:**
- Contains corrosive acid
- Can produce hydrogen gas
- Ventilate well
- Wear eye protection

## Soldering Safety

### Before Soldering

**Personal Protection:**
- Tie back long hair
- Remove dangling jewelry
- Wear safety glasses
- Consider fume extraction mask for extended work

**Workspace Setup:**
- Use soldering mat or ceramic tile
- Keep iron in proper stand
- Have damp sponge for cleaning tip
- Keep flammable materials away
- Work in well-ventilated area

### During Soldering

**Safe Practices:**
- Always use a stand when not actively soldering
- Never touch tip or hot metal
- Assume iron is hot until verified
- Keep cord away from hot tip
- Clean tip regularly to prevent buildup

**Fume Management:**
- Solder produces lead fumes (even lead-free solder has flux fumes)
- Position face away from fumes
- Use fume extractor if available
- Take breaks for fresh air
- Wash hands after soldering

**Common Injuries:**
- Burns from touching tip (up to 400°C/750°F)
- Burns from hot solder splashing
- Burns from touching freshly soldered joints
- Eye irritation from fumes

### After Soldering

- Let iron cool completely before storing
- Unplug immediately when done
- Never leave running unattended
- Clean work area of solder scraps
- Wash hands before eating

## Sharp Objects and Tools

### Wire Cutters and Strippers

**Safe Use:**
- Cut away from body
- Wear safety glasses (wire ends can fly)
- Check for spring-loaded snap back
- Keep fingers clear of cutting edges

**Storage:**
- Store with cutting edges protected
- Keep blades closed when not in use
- Replace dull or damaged tools

### PCB Edges

Circuit board edges are surprisingly sharp.

**Precautions:**
- Sand sharp edges with file or sandpaper
- Wear gloves when handling for extended periods
- Bandaids available for minor cuts
- Be especially careful with freshly cut boards

### Chip Pins

IC pins can puncture skin.

**Handling:**
- Hold chips by the body, not pins
- Bend pins carefully and slowly
- Watch for springback when bending
- Dispose of broken pins safely

## Chemical Safety

### Flux and Solder

**Hazards:**
- Skin irritation
- Eye irritation
- Fume inhalation

**Safe Handling:**
- Wash hands after contact
- Do not eat while soldering
- Ventilate work area
- Keep away from face

### Isopropyl Alcohol (IPA)

Used for cleaning flux and boards.

**Hazards:**
- Flammable
- Skin drying
- Fume inhalation

**Safe Use:**
- Use in ventilated area
- Keep away from open flames
- Keep container closed when not in use
- Wash hands after use

### Thermal Paste

**Hazards:**
- Skin irritation
- Some older types contain metals

**Safe Use:**
- Minimize skin contact
- Wash hands immediately if contact occurs
- Do not ingest
- Dispose of properly

## Physical Safety

### Heavy Objects

E-waste can be heavy and awkward.

**Lifting:**
- Bend knees, not back
- Get help with heavy items
- Clear path before carrying
- Set down gently to avoid pinched fingers

**Storage:**
- Heavy items on lower shelves
- Secure stacks to prevent falling
- Keep aisles clear

### Workspace Ergonomics

**Prevent Fatigue:**
- Sit at proper height
- Good lighting to reduce eye strain
- Take breaks every 30-45 minutes
- Stretch hands and wrists
- Adjust magnification to avoid hunching

### Trip Hazards

**Prevention:**
- Route cables along walls
- Tape down cables crossing walkways
- Keep bags and belongings under tables
- Clean up dropped parts immediately
- Adequate lighting in all areas

## Eye Protection

### When to Wear Safety Glasses

**Required:**
- Cutting wires or leads
- Drilling or grinding
- Working with chemicals
- Desoldering (hot solder can splash)
- Anytime eye injury is possible

**Recommended:**
- General electronics work
- When using magnification creates risk

### Avoiding Eye Strain

- Use proper lighting
- Take regular breaks (20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds)
- Use magnification appropriate for task
- Adjust contrast and brightness of displays

## ESD (Electrostatic Discharge) Safety

ESD can damage sensitive chips.

### ESD Protection Basics

**Prevent Damage:**
- Touch grounded metal before handling chips
- Use ESD wrist strap if available
- Work on ESD mat if available
- Avoid synthetic clothing
- Increase humidity if very dry

**When ESD Matters:**
- Handling bare chips (especially CMOS)
- Modern microcontrollers
- Memory chips
- RF components

**When ESD Is Less Critical:**
- Chips still on circuit boards
- Older technology
- Power components
- Passive components (resistors, capacitors)

### Simple ESD Prevention

Without expensive equipment:
- Touch grounded metal first
- Work on wooden table (not plastic)
- Avoid carpeted areas
- Store chips in anti-static foam or bags
- Handle by edges, not pins

## Environmental Hazards

### Dust and Particles

Old electronics contain dust, dirt, and sometimes mold.

**Protection:**
- Dust mask for very dirty items
- Work in well-ventilated area
- Wipe down with damp cloth before handling
- Wash hands frequently

### Unknown Substances

**Do Not Touch:**
- Crystalline deposits (could be corrosion)
- Sticky residues (could be capacitor leakage)
- Discolored areas (heat damage, chemicals)
- Anything that smells unusual

**If Found:**
- Set aside in separate container
- Label clearly
- Dispose of properly
- Wash hands thoroughly

## Fire Safety

### Fire Prevention

**Good Practices:**
- Never leave soldering iron unattended
- Keep flammable materials away from heat sources
- Use proper fuse ratings
- Check for overheating components
- Monitor battery charging

**Fire Extinguisher:**
- Class C for electrical fires
- Know location
- Know how to use (PASS: Pull, Aim, Squeeze, Sweep)
- Call fire department for any fire that cannot be immediately extinguished

### If Fire Occurs

1. Alert everyone immediately
2. Evacuate if fire is spreading
3. Use extinguisher only if safe
4. Never use water on electrical fires
5. Call 911 if fire is not immediately contained

## Medical Emergencies

### Minor Injuries

**Burns (Soldering):**
- Run under cool water for 10-15 minutes
- Apply burn gel or aloe
- Cover with clean bandage
- Do not pop blisters
- Seek medical attention if severe

**Cuts:**
- Apply pressure to stop bleeding
- Clean with water
- Apply antibiotic ointment
- Bandage
- Seek medical attention if deep or won't stop bleeding

**Eye Irritation:**
- Flush with water for 15 minutes
- Do not rub eyes
- Remove contact lenses if present
- Seek medical attention if pain persists

### Electrical Shock

Even low voltage can be dangerous.

**If Someone Is Shocked:**
1. Do not touch them if still in contact with power
2. Shut off power immediately
3. If cannot shut off, use non-conductive object to separate
4. Call 911 immediately
5. Begin CPR if needed and trained
6. Keep person still and warm

**After Shock:**
- Seek medical attention even if feeling fine
- Electrical shock can cause delayed effects
- Document what happened

## Personal Protective Equipment (PPE)

### Minimum Required

For every workshop:
- Closed-toe shoes
- Long pants (protect legs from dropped items)
- Hair tied back if long

### Recommended

- Safety glasses (especially when cutting)
- ESD wrist strap (when handling sensitive chips)
- Nitrile gloves (when handling very dirty items)

### Optional

- Dust mask (very dirty or moldy items)
- Heat-resistant gloves (handling hot items)
- Fume extraction mask (extended soldering)

## Workspace Rules

### General Rules

**Always:**
- Clean as you go
- Return tools to proper place
- Report unsafe conditions
- Ask if unsure
- Stop work if feeling unwell

**Never:**
- Work when fatigued
- Rush or take shortcuts
- Disable safety features
- Work alone on dangerous tasks
- Bring food or drink to work area

### Eating and Drinking

**Strict Rules:**
- No eating at workbenches
- No drinking at workbenches (except water with sealed lid)
- Wash hands before eating
- Designated break area separate from work area
- Never touch mouth, eyes, or nose during work

## Special Hazards in E-Waste

### CRT Monitors and TVs

**EXTREME DANGER:**
- Can hold 25,000 volts for months
- Can kill instantly
- Implosion hazard if glass breaks
- Lead in glass

**DO NOT:**
- Open CRT devices
- Touch internal components
- Break CRT glass
- Work on powered CRT

Leave CRT work to trained professionals.

### Microwave Ovens

**EXTREME DANGER:**
- High voltage capacitor (2000V+)
- Magnetron can produce dangerous microwaves
- Beryllium oxide hazard in some components

**DO NOT:**
- Open microwave ovens
- Remove any components
- Power up outside of case

### Laser Printers

**Hazards:**
- Toner dust (respiratory irritant)
- High voltage power supply
- Hot fuser (up to 200°C)
- Laser can damage eyes

**Precautions:**
- Work in ventilated area
- Do not breathe toner dust
- Let cool before handling
- Do not look into laser aperture

### Power Supplies

**Hazards:**
- High voltage (120V-400V AC internally)
- Stored charge in capacitors
- Heavy transformers

**Precautions:**
- Unplug and wait 10 minutes before opening
- Discharge capacitors
- Use insulated tools
- Work with one hand when probing

## Child Safety

If children attend workshops:

**Additional Requirements:**
- Parental supervision required
- No soldering for children under 12
- Modified voltage limits (under 5V only)
- No sharp tools without direct supervision
- Simplified projects with less risk

**Age-Appropriate Activities:**
- Visual chip identification (safe)
- Using multimeter on batteries (safe)
- Taking notes and photos (safe)
- Software/computer work (safe)

## Accessibility Considerations

Make workshops safe for everyone:

**Physical Accessibility:**
- Clear wide aisles for wheelchairs
- Adjustable height work surfaces
- Tools accessible without reaching
- Adequate seating and rest areas

**Sensory Considerations:**
- Bright work lights for low vision
- Written and verbal instructions
- Quiet area available if needed
- Fragrance-free environment

## Emergency Procedures

### Emergency Contacts

Post this information visibly:

```
EMERGENCY: 911

Fire Department: ___________
Poison Control: 1-800-222-1222
Nearest Hospital: ___________
Workshop Leader: ___________
Building Manager: ___________
```

### Evacuation Plan

- Know exit routes
- Know meeting point outside
- Help others evacuate
- Do not re-enter building
- Account for all participants

### Incident Reporting

If any injury or near-miss occurs:

1. Ensure person is safe and treated
2. Document what happened
3. Identify root cause
4. Update procedures to prevent recurrence
5. Share lessons learned

## Safety Training

### Before First Workshop

All facilitators should:
- Read this entire guide
- Practice using fire extinguisher
- Know first aid basics
- Understand electrical safety
- Identify all hazards in workspace

### Participant Briefing

At start of every workshop:

1. Point out emergency exits
2. Show location of first aid kit
3. Demonstrate fire extinguisher
4. Explain voltage limits
5. Cover basic safety rules
6. Answer safety questions

### Ongoing Training

- Review safety after any incident
- Update procedures based on experience
- Share new hazards discovered
- Practice emergency procedures annually

## Safety Culture

### Encouraging Safe Behavior

**Do:**
- Praise people who follow safety rules
- Make it easy to report hazards
- Take all concerns seriously
- Update procedures when needed
- Lead by example

**Don't:**
- Rush or skip safety steps
- Pressure people to work unsafely
- Dismiss safety concerns
- Punish people for reporting issues
- Treat safety as optional

### Speaking Up

**If You See Something Unsafe:**
- Say something immediately
- Do not assume someone else will
- Be specific about the hazard
- Suggest a solution if possible
- Thank people for listening

**If Someone Corrects You:**
- Thank them
- Stop the unsafe action
- Ask questions to understand
- Adjust behavior going forward
- No ego, just safety

## Cleanup Procedures

### End of Workshop

**Electrical:**
- Unplug all soldering irons
- Disconnect all power supplies
- Verify all equipment is off
- Coil cables neatly

**Tools:**
- Clean and return to storage
- Report any damaged tools
- Restock supplies as needed
- Lock tool storage

**Waste:**
- Dispose of cut wires and leads
- Empty solder waste
- Recycle properly when possible
- Clean work surfaces

**Final Check:**
- Walk through entire space
- Check for hazards
- Verify all equipment off
- Lock up when leaving

## Legal and Insurance

### Liability Waivers

Consider having participants sign waivers acknowledging:
- They understand the risks
- They will follow safety rules
- They have no medical conditions preventing participation
- They release organizers from liability

Consult a lawyer for your specific situation.

### Insurance

Consider:
- General liability insurance
- Property insurance for equipment
- Accident insurance for participants

Check with insurance provider about workshop activities.

## Resources

### Safety Information

- OSHA Guidelines: osha.gov
- Electronics Safety: eevblog.com/wiki/EEVblog:Safety
- Soldering Safety: sparkfun.com/tutorials/5
- Battery Safety: batteryuniversity.com

### First Aid Training

- Red Cross: redcross.org/take-a-class
- CPR/AED certification recommended for leaders

### Equipment Recommendations

- Fire extinguisher: Class C electrical
- First aid kit: ANSI compliant
- Safety glasses: ANSI Z87.1 rated
- Fume extractor: Hakko FA-400 or similar

## Remember

Safety is not negotiable. It is not optional. It is not "extra."

No circuit board, chip, or piece of knowledge is worth an injury.

If something feels unsafe, stop and reassess.

When in doubt, ask for help.

Take care of yourself and each other.

---

This safety guide is CC-BY-SA 4.0
E-Waste Reverse Engineering Clinic
Hidden Layer Media | Neon Maxima 2133
Charlotte Hardware Collective

Review and update this guide regularly based on real-world experience.
