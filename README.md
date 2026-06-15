# Security-Assessment-Scanne

A terminal-based Python application that automates Nmap scans through an interactive menu-driven interface.

## Overview

ScanForge simplifies network reconnaissance by allowing users to select common Nmap scan options from a menu instead of manually typing command-line arguments. Multiple scan options can be combined to create customized scans.

## Features

* Interactive terminal interface
* Stealth Scan (`-sS`)
* Service Version Detection (`-sV`)
* OS Detection (`-O`)
* Aggressive Scan (`-A`)
* UDP Scan (`-sU`)
* Custom Nmap option support
* Multiple option selection
* Real-time scan output

## Technologies Used

* Python 3
* Nmap
* Subprocess Module

## Requirements

* Python 3.x
* Nmap installed and available in PATH

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ScanForge.git
cd ScanForge
```

Run the application:

```bash
python main.py
```

## Example Usage

1. Enter a target IP address or domain.
2. Select one or more scan options from the menu.
3. Start the scan.
4. View the results directly in the terminal.

Example combined scan:

```bash
nmap -sV -O target.com
```

## Project Structure

```text
ScanForge/
│
├── main.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Always obtain proper permission before scanning networks or systems that you do not own or manage.

## Future Improvements

* Report export to TXT files
* Scan history
* Port range selection
* Host discovery scans
* Timing template support
* Colored terminal output

## License

This project is licensed under the MIT License.
