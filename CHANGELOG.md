# Changelog

All notable changes to the E-Waste Reverse Engineering Clinic project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Planned
- First public workshop
- Photo documentation from workshops
- Video tutorials
- More chip identification logs
- Advanced curriculum tracks
- Soldering workshop materials
- Repair-focused content

## [0.1.0] - 2025-01-XX

### Added
- Initial repository structure
- MIT License for code
- CC-BY-SA 4.0 license for documentation
- README with project overview
- CODE_OF_CONDUCT with no-gatekeeping policy
- CONTRIBUTING guidelines
- GitHub Pages website with Windows 98 aesthetic
- Complete workshop format guide
- Safety guide for workshops
- Facilitator checklist
- Workshop announcement templates
- Troubleshooting guide

### Documentation
- GreatFET setup instructions for Linux and Windows
- Data format specification for CSV logs
- I²C address quick reference
- Chip package identification guide
- Common chip families reference
- Datasheet organization system
- FAQ document

### Scripts
- i2c_probe.py - I²C bus scanner
- usb_enum.py - USB device enumerator
- log_to_csv.py - Interactive data logger
- chip_lookup.py - Datasheet search helper

All scripts include:
- SPDX-License-Identifier: MIT
- Comprehensive error handling
- Detailed help text
- Troubleshooting sections

### Infrastructure
- GitHub Pages configuration
- Automated setup script
- Example data templates
- Directory structure for expansion

### Resources
- Workshop materials
- Reference guides (printable)
- Safety procedures
- Accessibility guidelines

## Version History Notes

### Pre-Release Development

The E-Waste Reverse Engineering Clinic project began in early 2025 as a community hardware education initiative in Charlotte, North Carolina. Initial work focused on:

- Developing workshop formats through small test sessions
- Creating documentation that would be genuinely useful
- Building tools that actually solve real problems
- Establishing community guidelines centered on accessibility

The project was developed with these core principles:
- No gatekeeping
- Practical, hands-on learning
- Open source everything
- Community ownership
- Environmental consciousness

### Design Philosophy

Key design decisions made during initial development:

**Windows 98 Aesthetic Website:**
- Chosen to be distinctive and memorable
- Represents DIY/underground tech culture
- Accessible without complex frameworks
- Easy to customize and maintain

**No Em Dashes:**
- Personal style preference of project founder
- Enforced throughout all documentation
- Uses hyphens, commas, colons instead

**Complete Code, No Placeholders:**
- Every script is fully functional
- No "TODO" comments left for users
- Real error handling, not stubs
- Tested with actual hardware

**Documentation-First Approach:**
- Lower barrier to entry
- Enable replication by other cities
- Create lasting educational value
- Teach while building

### Future Directions

The project roadmap includes:

**Short Term (Next 3 Months):**
- Host first public workshops
- Gather feedback from participants
- Document real-world experiences
- Improve based on actual usage
- Build initial chip database

**Medium Term (3-12 Months):**
- Establish regular workshop schedule
- Grow community of regular participants
- Develop advanced curriculum
- Build partnerships with local organizations
- Expand to related topics (soldering, repair)

**Long Term (1-3 Years):**
- Secure permanent hackerspace location
- Support other cities starting clinics
- Create comprehensive repair curriculum
- Build extensive chip database
- Establish sustainable operation model

### Contributing to Changelog

When making significant changes:

1. Add entry under [Unreleased]
2. Use categories: Added, Changed, Deprecated, Removed, Fixed, Security
3. Include brief description
4. Reference issue/PR numbers if applicable
5. When releasing, move [Unreleased] items to new version

### Version Numbering

This project uses [Semantic Versioning](https://semver.org/):

- MAJOR version: Breaking changes to workshop format or tools
- MINOR version: New features, scripts, or significant documentation
- PATCH version: Bug fixes, typos, minor improvements

Example:
- 0.1.0 - Initial release
- 0.2.0 - Added soldering curriculum
- 0.2.1 - Fixed typos in safety guide
- 1.0.0 - First workshop series completed, format proven

### Change Categories Explained

**Added:**
New features, documentation, or resources.

Example: "Added troubleshooting guide for common workshop issues"

**Changed:**
Modifications to existing functionality.

Example: "Changed workshop duration from 2 to 3 hours based on feedback"

**Deprecated:**
Features that will be removed in future versions.

Example: "Deprecated old CSV format, will be removed in 2.0.0"

**Removed:**
Features or files that have been deleted.

Example: "Removed redundant reference guide, consolidated into main guide"

**Fixed:**
Bug fixes or corrections.

Example: "Fixed I²C probe script crash on Windows"

**Security:**
Security-related changes.

Example: "Updated dependencies to patch vulnerability"

### Release Process

When creating a new release:

1. Update CHANGELOG with version number and date
2. Move items from [Unreleased] to new version section
3. Update version numbers in relevant files
4. Create git tag: `git tag -a v0.1.0 -m "Release version 0.1.0"`
5. Push tag: `git push origin v0.1.0`
6. Create GitHub release with notes from CHANGELOG
7. Announce on relevant channels

### Notable Decisions

**Why No Automated Changelog:**
We manually maintain this changelog because:
- Gives opportunity to write clear, user-focused notes
- Can group related changes logically
- Allows editorial voice and context
- More readable than raw commit messages

**Why Track Planned Items:**
The [Unreleased] Planned section helps:
- Communicate project direction
- Invite contributions
- Set expectations
- Track ideas

**Why Detailed Version History:**
Documenting design decisions and philosophy helps:
- New contributors understand project values
- Future maintainers know why choices were made
- Community sees transparent process
- Preserve institutional knowledge

### Questions About Changelog

**Should I add my contribution here?**
Yes! When submitting a pull request, add a brief entry under [Unreleased]. The maintainers will refine it during release.

**How detailed should entries be?**
Brief but clear. One line per change is usually enough. Link to issues or PRs for more context.

**What if I am not sure what category?**
Use your best judgment. Maintainers will adjust if needed. When in doubt, use "Added" or "Changed".

**Can I suggest planned features?**
Yes! Open an issue to discuss, then add to Planned section if consensus is reached.

### Acknowledgments

This changelog format is inspired by [Keep a Changelog](https://keepachangelog.com/), which advocates for:
- Human-readable changelog
- Group changes by category
- Include version and date
- Distinguish between changes and releases

We adapted it to fit community project needs:
- More context and explanation
- Design decision documentation
- Philosophy and values included
- Accessible to non-technical contributors

---

This changelog is part of the E-Waste Reverse Engineering Clinic project, initiated by Hidden Layer Media with help from Neon Maxima 2133. 
Licensed under CC-BY-SA 4.0.

[Unreleased]: https://github.com/numbpill3d/e-waste-clinic/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/numbpill3d/e-waste-clinic/releases/tag/v0.1.0
