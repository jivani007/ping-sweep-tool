# Subnet Scanner (Python)

A simple Python tool to scan a given subnet and check which hosts are alive (ICMP ping).

## Features
- Scans any subnet (e.g., `192.168.1.0/24`)
- Uses ICMP ping to find alive hosts
- Supports private & public IP ranges
- Multi-threaded for fast scanning

## Usage
```bash
python scanner.py --subnet 192.168.1.0/24
