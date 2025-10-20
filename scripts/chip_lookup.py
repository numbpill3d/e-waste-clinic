#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
Chip Datasheet Lookup Tool

Search for chip datasheets by part number using common datasheet resources.
Generates URLs for manual lookup since automated scraping is unreliable.

Usage:
    python3 chip_lookup.py PART_NUMBER

Example:
    python3 chip_lookup.py STM32F103
    python3 chip_lookup.py 24C256

Author: Charlotte Hardware Collective
"""

import sys
import urllib.parse


DATASHEET_SOURCES = [
    {
        'name': 'Octopart',
        'url': 'https://octopart.com/search?q={query}',
        'description': 'Aggregates datasheets from many sources'
    },
    {
        'name': 'Alldatasheet',
        'url': 'https://www.alldatasheet.com/datasheet-pdf/search/search.html?sWord={query}',
        'description': 'Large collection of manufacturer datasheets'
    },
    {
        'name': 'Datasheetspdf',
        'url': 'https://www.datasheetspdf.com/datasheet/{query}',
        'description': 'PDF datasheet archive'
    },
    {
        'name': 'DigiKey',
        'url': 'https://www.digikey.com/en/products/result?keywords={query}',
        'description': 'Component distributor with datasheets'
    },
    {
        'name': 'Mouser',
        'url': 'https://www.mouser.com/c/?q={query}',
        'description': 'Component distributor with datasheets'
    },
    {
        'name': 'Google Search',
        'url': 'https://www.google.com/search?q={query}+datasheet+filetype:pdf',
        'description': 'Direct PDF search'
    }
]


def search_chip(part_number):
    """Generate datasheet search URLs for a chip part number."""
    
    # Clean up part number
    part_number = part_number.strip().upper()
    
    # URL encode the part number
    encoded = urllib.parse.quote_plus(part_number)
    
    print("=" * 60)
    print(f"Datasheet Search: {part_number}")
    print("=" * 60)
    print("\nSearch URLs:")
    print()
    
    for i, source in enumerate(DATASHEET_SOURCES, 1):
        url = source['url'].format(query=encoded)
        print(f"{i}. {source['name']}")
        print(f"   {source['description']}")
        print(f"   {url}")
        print()
    
    print("=" * 60)
    print("Tips:")
    print("  - Start with Octopart for an overview")
    print("  - Check manufacturer websites for official datasheets")
    print("  - Compare pin counts and package types with your chip")
    print("  - Look for 'datasheet' or 'specifications' in results")
    print("  - Some chips have multiple revisions, check carefully")
    print("=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 chip_lookup.py PART_NUMBER")
        print()
        print("Examples:")
        print("  python3 chip_lookup.py STM32F103")
        print("  python3 chip_lookup.py 24C256")
        print("  python3 chip_lookup.py RTL8211E")
        print()
        print("This tool generates datasheet search URLs.")
        print("Open the URLs in your browser to find datasheets.")
        sys.exit(1)
    
    # Join all arguments in case part number has spaces
    part_number = ' '.join(sys.argv[1:])
    
    search_chip(part_number)


if __name__ == "__main__":
    main()
