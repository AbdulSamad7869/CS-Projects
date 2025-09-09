# Port_Scanner.py

A fast **multithreaded TCP port scanner** written in Python.  
This tool can scan a target host for open ports using threading for speed.  


---

## Features
- Scan **individual ports** (e.g. `22,80,443`)
- Scan **port ranges** (e.g. `20-25`)
- Scan the **default well-known range** (1–1024)
- Scan **all 65,535 ports**
- Multithreaded for faster results
- Automatically detects common service names (e.g. 80 → http)

---

## Requirements
- Python **3.9+** recommended (uses type hints and `concurrent.futures`)

No external libraries are required. It only uses Python’s standard library.

---

## Usage

### Basic Scan (well-known ports 1–1024)
```bash
python Port_Scanner.py --host example.com
