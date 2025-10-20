# Frequently Asked Questions

Common questions about the E-Waste Reverse Engineering Clinic project.

## General Questions

### What is the E-Waste Reverse Engineering Clinic?

A community hardware education project that teaches electronics and digital communication by probing chips on discarded circuit boards. We use open hardware tools like the GreatFET One to identify chips, understand protocols, and learn how devices actually work.

The project is based in Charlotte, North Carolina, but designed to be replicated by any community.

### Who runs this project?

The E-Waste Reverse Engineering Clinic was started by Splicer and is being developed by the Charlotte Hardware Collective (a group that is currently forming). It is a grassroots community effort with no corporate funding.

### Is this really free?

Yes. Workshops are free to attend. All materials, tools, and circuit boards are provided. The documentation and software are open source and freely licensed.

### Do I need experience to participate?

No. Workshops are designed for absolute beginners. If you are curious and willing to learn, you can do this. We start with the basics and work up from there.

### Is this only for engineers?

No. This is for anyone curious about electronics. We explicitly avoid gatekeeping and welcome people from all backgrounds. You do not need an engineering degree, prior electronics knowledge, or expensive equipment.

## Workshop Questions

### How do I find out about workshops?

- Watch the GitHub repository for announcements
- Email splicer@hiddenlayermedia.com to join the announcement list
- Follow on social media (links coming soon)
- Check back at this website regularly

### How long are workshops?

Typically 3 hours. Some may be shorter (2 hours) or longer (4-6 hours) depending on format and content.

### Do I need to bring anything?

No. We provide everything you need:
- Circuit boards and e-waste
- GreatFET One probing tools
- Laptops with scripts
- Reference materials
- Hand tools

Optional to bring:
- Your own laptop
- Notebook for personal notes
- Safety glasses (we have extras)
- Your own e-waste to explore

### What if I have to leave early?

That is fine. We understand people have schedules. Just let the facilitator know. You can catch up on what you missed using the online documentation.

### Can I bring my kids?

It depends on the specific workshop. Some are appropriate for older kids (12+) with supervision. Others are designed for adults only. Check the workshop announcement for age guidance.

Children must be supervised by a parent or guardian at all times.

### Are workshops accessible?

We strive to make workshops accessible to everyone. Venues are chosen for wheelchair accessibility, and we provide accommodations when requested. If you have specific accessibility needs, contact us in advance.

### What if I cannot make it to a workshop?

All our materials are online and open source. You can follow the documentation and try it yourself with your own equipment. Or wait for the next workshop.

### How do I host a workshop in my city?

Great! Everything you need is in this repository:
- Workshop format guide
- Reference materials
- Scripts and tools
- Safety guidelines

Fork the repo, adapt it to your community, and run with it. Let us know how it goes!

## Technical Questions

### What is a GreatFET?

GreatFET One is an open hardware USB tool made by Great Scott Gadgets. It can act as a logic analyzer, protocol sniffer, or general-purpose interface for testing and interacting with electronic devices.

We use it to probe I²C and SPI buses on circuit boards.

Learn more: greatscottgadgets.com/greatfet

### Do I need to buy a GreatFET?

Not for workshops. We provide them. If you want to continue learning at home, you can buy your own (around $100). They are available from Great Scott Gadgets and authorized distributors.

### What is I²C?

I²C (Inter-Integrated Circuit) is a communication protocol used by chips to talk to each other. It uses two wires (SDA and SCL) plus ground. Many chips use I²C including memory, sensors, and real-time clocks.

### What is SPI?

SPI (Serial Peripheral Interface) is another communication protocol. It is faster than I²C but uses more wires (MOSI, MISO, SCK, CS, plus ground). Flash memory and some sensors use SPI.

### Is this like hacking?

In the sense of learning how things work and taking them apart to understand them, yes. In the sense of illegal computer intrusion, no.

We work on discarded electronics that no one is using anymore. We learn how hardware communicates. This is educational and legal.

### Can I learn to repair devices?

Yes! Understanding chip identification and protocols is foundational for repair work. While workshops focus on exploration and learning, the skills transfer directly to repair.

### Will this help me get a job?

Maybe. The skills you learn (chip identification, protocol analysis, reading datasheets, documentation) are valuable in electronics, repair, and engineering. But that is not the main goal. The main goal is learning and community.

### What operating system do I need?

Scripts work on Linux, Windows, and macOS. Installation instructions are provided for Linux and Windows. macOS is similar to Linux.

For workshops, we provide laptops with everything installed.

### Can I use this on my own projects?

Absolutely! That is encouraged. The tools and techniques work on any circuit board. Use them for repair, reverse engineering, development, or learning.

## Safety Questions

### Is this safe?

Yes, when following safety guidelines. We work only on low-voltage circuits (5V or less). No live AC power. No dangerous voltages. Safety briefing at the start of every workshop.

### What about electrocution?

We never work on anything connected to wall power (120V/240V AC). We use battery-powered devices or low-voltage supplies. Following the safety rules keeps everyone safe.

### What about toxic materials?

Some e-waste may contain hazardous materials (lead solder, old capacitors, etc.). We handle these safely:
- Work in ventilated areas
- Wash hands frequently
- No eating/drinking at workbenches
- Proper disposal of waste

### What if I get hurt?

First aid kit is available at every workshop. For minor injuries (small cuts, minor burns), we can handle on-site. For serious injuries, we call 911 immediately.

Following safety guidelines prevents injuries.

## Project Questions

### What is the goal of this project?

Short term: Teach people about electronics through hands-on workshops.

Medium term: Build a community of people interested in hardware.

Long term: Establish a permanent hackerspace in Charlotte where people can access tools, learn skills, and work on projects.

### Is this a business?

No. This is a community education project. There are no fees, no products, no services for sale. It is run by volunteers and supported by the community.

### How is this funded?

Currently, it is self-funded by organizers. As the project grows, we may seek grants, donations, or sponsorships. But it will always remain free for participants.

### Can I donate?

Right now, we are not set up to accept monetary donations. The best ways to support:
- Attend workshops
- Contribute documentation
- Share the project
- Start a clinic in your city
- Donate equipment or e-waste

### Can I volunteer?

Yes! We need help with:
- Co-facilitating workshops
- Collecting e-waste
- Improving documentation
- Writing code
- Creating visual aids
- Spreading the word

Contact splicer@hiddenlayermedia.com to get involved.

### Is there a physical space?

Not yet. Workshops are held at partner venues (libraries, makerspaces, community centers). Long-term goal is to establish a permanent space.

### Can companies sponsor?

Potentially. We want to maintain independence and community ownership. If your company wants to support (donate equipment, provide venue, fund materials), contact us to discuss.

We will not accept sponsorship that comes with advertising, branding requirements, or control over content.

## Data and Privacy

### What happens to the data I collect?

Chip identification logs are contributed to the project database (if you choose to submit them). This helps everyone learn from collective findings.

Your data is:
- Licensed under CC-BY-SA 4.0 (open)
- Attributed to you (if desired)
- Freely accessible to everyone

### Do you collect personal information?

Only what is necessary:
- Workshop registration (name, email, phone)
- Emergency contacts
- Accessibility needs

We do not share or sell personal information. It is used only for workshop coordination and safety.

### Can I remain anonymous?

Yes. You can contribute data and participate in workshops without providing your real name. We respect privacy.

### What about photos and videos?

Photos may be taken at workshops for documentation and promotion. We:
- Ask permission before taking photos
- Offer photo-free workshops if needed
- Blur faces upon request
- Delete photos upon request

You can opt out of photos completely.

## Contribution Questions

### How can I contribute?

Many ways:
- Attend workshops and log data
- Improve documentation
- Write or improve scripts
- Create visual aids
- Translate materials
- Host workshops in your city
- Share the project

See CONTRIBUTING.md for details.

### I am not technical. Can I still help?

Yes! We need:
- Writers (documentation, announcements)
- Designers (visuals, layouts)
- Organizers (logistics, venues)
- Communicators (social media, outreach)
- Connectors (introductions, partnerships)

Not everything requires coding or electronics knowledge.

### Do I need to know Git?

Not required, but helpful. We can guide you through the process. If Git is too complicated, you can email contributions and someone else can commit them.

### What license are contributions under?

- Code: MIT License
- Documentation: CC-BY-SA 4.0

By contributing, you agree to these licenses. Both are very permissive and allow free use and modification.

### Will I get credit?

Yes! Contributors are listed in the repository and can be credited in documentation. You control how you want to be acknowledged.

### Can I fork and modify for my needs?

Absolutely! That is the point of open source. Fork it, change it, improve it. If your improvements benefit others, consider contributing back.

## Equipment Questions

### What e-waste works best?

Good candidates:
- Routers and modems
- Printers (not laser, inkjet is safer)
- USB hubs and peripherals
- Old computers (not monitors)
- Network switches
- External hard drive enclosures

Avoid:
- CRT monitors and TVs (dangerous voltages)
- Microwave ovens (dangerous even when unpowered)
- Power supplies (high voltage capacitors)
- Medical equipment (often protected/regulated)

### Where do you get e-waste?

Sources:
- Donation centers (Goodwill, etc.)
- Repair shops (ask for dead boards)
- Friends and family (old equipment)
- Thrift stores
- E-waste recycling events
- Universities (surplus equipment)

Always get permission before taking things apart.

### What tools do I need?

For workshops: Nothing, we provide everything.

For home learning:
- GreatFET One or similar (~$100)
- Basic hand tools (screwdrivers, tweezers)
- Magnifying glass or USB microscope
- Multimeter (optional but helpful)
- Computer with USB port

### Can I use different hardware?

Yes. While we use GreatFET, you can use:
- Bus Pirate
- Arduino with I²C libraries
- Logic analyzers
- Other protocol sniffers

The principles are the same. You may need to adapt the scripts.

## Learning Questions

### What will I actually learn?

Hard skills:
- Chip identification
- Reading datasheets
- Protocol basics (I²C, SPI, USB)
- Using probing tools
- Documentation practices

Soft skills:
- Problem solving
- Methodical troubleshooting
- Community learning
- Asking good questions

Conceptual understanding:
- How devices communicate
- System architecture
- Repair feasibility
- Hardware design principles

### Is this useful for Arduino projects?

Very much so! Understanding I²C and SPI is crucial for Arduino projects. Many Arduino sensors and peripherals use these protocols. The skills transfer directly.

### Will I learn to program?

Not directly. The Python scripts are provided. But you will use them and see how they work. This can be a gentle introduction to programming concepts.

If you want to learn programming, this is a good motivator.

### Can kids learn this?

Yes, with adaptations. Older kids (12+) can participate in workshops with supervision. The visual chip identification aspects are especially kid-friendly.

We are developing materials specifically for younger learners.

### What is the hardest part?

For most people:
- Reading tiny chip markings (use magnification!)
- Understanding datasheets (they get easier with practice)
- Troubleshooting when things do not work (be patient)

The good news: You get better at all of these with practice.

### What is the most rewarding part?

The "aha!" moments:
- Identifying your first chip
- Understanding how a board works
- Getting a scan to work
- Helping someone else learn
- Realizing you can understand this stuff

## Community Questions

### Is there a Discord/Slack/Forum?

Not yet. As the community grows, we will set up communication channels. For now:
- GitHub Discussions
- Email list
- In-person workshops

### How do I stay updated?

- Watch the GitHub repository
- Join the email list (splicer@hiddenlayermedia.com)
- Attend workshops
- Check back regularly

### Are there other cities doing this?

Not yet, but we hope there will be! This project is designed to be replicated. If you start a clinic in your city, let us know. We would love to connect communities.

### What is the Charlotte Hardware Collective?

The group organizing this project. Currently forming. Goal is to build a community around hardware learning, repair, and making in Charlotte, NC.

Long-term goal: Establish a permanent hackerspace.

### Can I join the core team?

Yes! We need committed volunteers who can:
- Co-facilitate workshops
- Maintain documentation
- Manage community
- Plan events
- Handle logistics

Contact splicer@hiddenlayermedia.com if interested.

## Philosophical Questions

### Why focus on e-waste?

Several reasons:
- Free source of learning materials
- Environmental angle (repair, reuse)
- No one is using these devices anymore
- Real-world hardware is more engaging than toy examples
- Rescues knowledge from landfills

### Why no gatekeeping?

Gatekeeping keeps knowledge locked away in elite groups. It prevents people from learning and growing. It creates artificial barriers based on credentials, not ability.

We believe everyone can learn. Everyone has something to contribute. Creating a welcoming space makes learning better for everyone.

### Why open source?

Knowledge should be free. Tools should be accessible. Communities should be able to build on each other's work without asking permission.

Open source ensures this project survives even if the original organizers move on. It belongs to everyone.

### What about right to repair?

This project strongly supports right to repair. Understanding how devices work and having the tools to fix them is fundamental. We teach skills that enable repair.

But we are also about more than repair. We are about curiosity, learning, community, and reclaiming knowledge.

### Is this political?

Only in the sense that access to knowledge is political. We believe:
- Hardware literacy should be accessible to everyone
- Communities should control their own learning
- Knowledge should not be locked behind credentials or paywalls
- People have the right to understand and repair their devices

If that is political, so be it.

## Still Have Questions?

Ask!
- Email: splicer@hiddenlayermedia.com
- GitHub: Open an issue or discussion
- Workshop: Ask facilitators in person

We would rather answer your questions than have you not participate because you were unsure.

---

This FAQ is CC-BY-SA 4.0
E-Waste Reverse Engineering Clinic
Hidden Layer Media | Neon Maxima 2133
Charlotte Hardware Collective

Questions not answered here? Let us know and we will add them!
