# Workshop Guide

This guide explains how to host your own E-Waste Reverse Engineering Clinic.

## Setup

1. Find a local venue (library, school, or community center).  
2. Collect e-waste from recyclers or friends.  
3. Bring anti-static mats, power strips, and lighting.  
4. Install GreatFET utilities on your laptops.  
5. Print the chip anatomy posters from the `/resources` folder.

## How the Clinic Works

- Start by showing people how to identify I²C headers and test points.  
- Demonstrate a probe using `i2c_probe.py`.  
- Discuss what the results mean (address ranges, bus conflicts, common devices).  
- Let participants try on their own boards.  
- Record findings in the shared log spreadsheet.

The event should feel casual, collaborative, and curious, not like a lecture. People learn better when they are free to experiment and fail safely.

## Cleanup and Data Sharing

- Collect working components in labeled bins (MCUs, EEPROMs, sensors).  
- Upload logs to the shared Google Sheet using `upload_to_sheets.py`.  
- Encourage participants to stay in touch or host their own mini-clinic.
