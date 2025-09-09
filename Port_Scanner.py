"""
Port_Scanner.py

A fast multithreaded TCP port scanner written in Python.

This script scans a target host (IP address or domain) for open ports.
It uses a thread pool to speed up scanning and can handle:
  • Individual ports (e.g. 22,80,443)
  • Port ranges (e.g. 20-25)
  • Full scans of all 65,535 ports

By default, it scans the well-known port range 1–1024.

⚠️ Note:
- Some ports (especially below 1024) may require administrator/root privileges
  depending on your operating system.
- This tool is for educational and authorized testing purposes only.
  Do not use it against systems without permission.

Usage examples:
---------------
# Scan well-known ports (1–1024) on a host
python Port_Scanner.py --host example.com

# Scan specific ports
python Port_Scanner.py --host example.com --ports 22,80,443

# Scan a range of ports
python Port_Scanner.py --host example.com --ports 20-25

# Scan all ports
python Port_Scanner.py --host example.com --all

# Control number of threads (default=200)
python Port_Scanner.py --host example.com --ports 80,443 --threads 500
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host: str, port: int, timeout: float = 0.5):
    """
    Attempt to connect to a single port on the target host.
    Returns (port, service) if the port is open, otherwise None.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket
    sock.settimeout(timeout)  # Set timeout to avoid long waits
    try:
        result = sock.connect_ex((host, port))  # Try connecting (0 = success)
        if result == 0:
            # Try to resolve the service name (e.g., 80 -> http)
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"
            return port, service
    except Exception:
        # Ignore connection errors, timeouts, etc.
        pass
    finally:
        sock.close()  # Ensure socket is always closed
    return None


def scan_ports(host: str, ports: list[int], max_threads: int = 200):
    """
    Scan multiple ports on a host using a thread pool.
    Prints results as they are discovered.
    """
    print(f"\nScanning {host}...\n")
    open_ports = []  # Store open ports for summary

    # Use a thread pool for concurrent scanning
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Submit one scanning task per port
        futures = [executor.submit(scan_port, host, port) for port in ports]

        # Process results as tasks complete
        for future in as_completed(futures):
            result = future.result()
            if result:  # If port is open
                port, service = result
                print(f"Port {port} is OPEN ({service})")
                open_ports.append(result)

    # Print scan summary
    print("\nScan complete.")
    if not open_ports:
        print("No open ports found.")
    else:
        print("\nSummary of open ports:")
        for port, service in sorted(open_ports):
            print(f"  {port}: {service}")


def parse_ports(port_str: str) -> list[int]:
    """
    Parse user-supplied port input into a list of integers.
    Supports:
      - Comma-separated ports: "22,80,443"
      - Ranges: "20-25"
    """
    ports = set()
    for part in port_str.split(","):
        part = part.strip()
        if "-" in part:  # Handle ranges like "20-25"
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        elif part.isdigit():  # Handle single port
            ports.add(int(part))
    return sorted(ports)


if __name__ == "__main__":
    # Command-line interface setup
    parser = argparse.ArgumentParser(description="Fast threaded port scanner")
    parser.add_argument("--host", help="Target host (IP or domain)", required=True)
    parser.add_argument(
        "--ports",
        help="Comma-separated ports or ranges (e.g. 22,80,443 or 20-25)",
    )
    parser.add_argument(
        "--all", action="store_true", help="Scan all 65,535 ports"
    )
    parser.add_argument(
        "--threads", type=int, default=200, help="Number of threads (default=200)"
    )
    args = parser.parse_args()

    # Decide which ports to scan
    if args.all:
        ports = list(range(1, 65536))  # Full scan of all ports
    elif args.ports:
        ports = parse_ports(args.ports)  # Use user-specified ports
    else:
        ports = list(range(1, 1025))  # Default: well-known ports

    # Run the scan
    scan_ports(args.host, ports, args.threads)

