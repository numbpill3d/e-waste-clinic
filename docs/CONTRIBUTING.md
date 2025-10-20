# Contributing to E-Waste Reverse Engineering Clinic

Thank you for your interest in contributing to this project. We welcome contributions from people of all skill levels. If you can identify a chip, run a script, or write down what you learned, you can contribute here.

## How to Contribute

### 1. Fork and Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/e-waste-clinic.git
cd e-waste-clinic
```

### 2. Create a Branch for Your Work

```bash
git checkout -b add-chip-log-modem-board
```

Use descriptive branch names that explain what you are adding or fixing.

### 3. Make Your Changes

Follow the guidelines below depending on what you are contributing.

### 4. Commit Your Changes

```bash
git add .
git commit -m "Add chip identification log for Netgear modem board"
```

Write clear commit messages that explain what changed and why.

### 5. Push and Create a Pull Request

```bash
git push origin add-chip-log-modem-board
```

Then go to GitHub and open a pull request. Describe what you added and why it is useful.

## What You Can Contribute

### Chip Identification Logs

Add your findings to the `data/` directory. Follow the format specified in `docs/data-format.md`.

File naming convention: `data/YYYYMMDD_board-description.csv`

Example: `data/20250115_netgear-router-wnr2000.csv`

### Python Scripts

Add new scripts to the `scripts/` directory. Include:

- Clear comments explaining what the script does
- Usage instructions at the top of the file
- SPDX license identifier: `# SPDX-License-Identifier: MIT`
- Error handling for common problems
- Example output in a comment block

### Documentation

Improve or add documentation in the `docs/` directory. Documentation should be:

- Written in clear, plain language
- Tested by someone who did not write it
- Free of jargon unless the jargon is explained
- Formatted in Markdown with consistent heading styles

### Workshop Materials

Share your workshop format, presentation slides, or handouts in `resources/workshops/`.

### Datasheets and References

Add useful datasheets or chip reference materials to `resources/datasheets/`. Include a README explaining what each file is and why it is useful.

## Formatting and Style Guidelines

### Code Style

- Use 4 spaces for indentation (no tabs)
- Keep lines under 100 characters when possible
- Use descriptive variable names
- Comment non-obvious logic
- Include error messages that actually help someone fix the problem

### Documentation Style

- Use Markdown formatting
- Keep paragraphs short and focused
- Use bullet points for lists
- Include examples whenever possible
- Write like you are explaining something at a workshop table, not writing a textbook

### File Naming

- Use lowercase letters
- Use underscores instead of spaces
- Use descriptive names: `router_chip_log.csv` not `data1.csv`
- Include dates for time-sensitive files: `20250115_workshop_notes.md`

### Commit Messages

- Start with a verb: "Add", "Fix", "Update", "Remove"
- Be specific: "Add I²C probe script for GreatFET" not "Add script"
- Keep the first line under 72 characters
- Add more detail in the body if needed

## Data Format Standards

When adding chip identification logs, follow the CSV format in `docs/data-format.md`:

```csv
board_name,chip_type,address_or_id,interface,condition,notes
```

### Required Fields

- `board_name`: Make and model of the board or device
- `chip_type`: Chip function (MCU, memory, sensor, etc.)
- `address_or_id`: I²C address, device ID, or chip marking
- `interface`: I²C, SPI, USB, UART, etc.
- `condition`: working, dead, unknown
- `notes`: Any additional observations

### Optional Fields

You can add custom fields if they are useful, but keep the core fields consistent so data can be merged easily.

## Testing Your Changes

Before submitting:

1. Test any scripts you added or modified
2. Check that documentation renders correctly in Markdown
3. Verify that CSV files load without errors
4. Make sure file paths and links work

## Pull Request Process

1. Update the README.md if you added new files or features
2. Add yourself to the contributors list if you want credit
3. Describe what your pull request does and why
4. Reference any related issues
5. Be patient while maintainers review your changes

We will review pull requests as quickly as we can. If changes are requested, please update your pull request rather than opening a new one.

## Community Standards

### Everyone Is Welcome

You do not need to be an engineer, a programmer, or an expert to contribute. Curiosity and a willingness to learn are the only requirements.

### Mistakes Are Part of Learning

If you submit something that needs changes, that is fine. We all learn by trying things and seeing what works. No one will be harsh or dismissive about mistakes.

### No Gatekeeping

Do not tell people they need to learn something else first, read specific books, or have certain credentials before they can participate. If someone asks a question, answer it or point them to a resource that will help.

### Respect All Participants

Be patient, be kind, and assume good intentions. People have different levels of experience and different ways of learning.

### Give Credit

If you use someone else's work, data, or ideas, credit them in your commit message or documentation. This is a community effort and everyone's contributions matter.

## Questions?

If you are not sure how to contribute or have questions about the process, open an issue on GitHub or email splicer@hiddenlayermedia.com.

We would rather answer questions and help you contribute than have you not contribute because you were unsure.

## License Agreement

By contributing to this repository, you agree that your code contributions are licensed under the MIT License and your documentation contributions are licensed under CC-BY-SA 4.0. See LICENSE and LICENSE.docs for details.
