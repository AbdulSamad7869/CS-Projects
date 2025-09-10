# 🔎 Port Scanner

A fast **multithreaded TCP port scanner** written in Python.  
It scans a target host (IP address or domain) for **open TCP ports** using a thread pool for high-speed concurrent scanning.

---

## ✨ Features
- Scan **individual ports** (e.g., `22,80,443`)
- Scan **port ranges** (e.g., `20-25`)
- **Full scan** of all 65,535 ports
- Defaults to scanning **well-known ports** (`1-1024`)
- Adjustable **thread pool size** for performance tuning
- Displays detected **services** (where available)

---

## ⚙️ Installation
Clone the repository and ensure you have Python 3.9+ installed:

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner

```
---

## 🚀 Usage

Basic Scan (well-known ports: 1–1024)
```bash
python3 Port_Scanner.py --host example.com
```
Scan Specific Ports
```bash
python3 Port_Scanner.py --host example.com --ports 22,80,443
```
Scan a range of ports
```bash
python Port_Scanner.py --host example.com --ports 20-25
```
Full Scan
```bash
python Port_Scanner.py --host example.com --all
```
---

## 📖 Example Output 

```bash

Scanning example.com...

Port 22 is OPEN (ssh)
Port 80 is OPEN (http)
Port 443 is OPEN (https)

Scan complete.

Summary of open ports:
  22: ssh
  80: http
  443: https

```
---
