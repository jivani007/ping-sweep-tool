import subprocess
import ipaddress
import concurrent.futures

def ping_host(ip):
    try:
        # Windows: use "-n 1" ; Linux/Mac: use "-c 1"
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "300", str(ip)],  # -w 300ms timeout
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

# Input subnet
subnet = input("Enter subnet (e.g., 192.168.1.0/24): ").strip()
network = ipaddress.ip_network(subnet, strict=False)

print(f"\nScanning subnet: {network}\n")

# Use ThreadPoolExecutor for concurrency
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = {executor.submit(ping_host, ip): ip for ip in network.hosts()}
    for future in concurrent.futures.as_completed(futures):
        ip = futures[future]
        try:
            if future.result():
                print(f"[+] Host alive: {ip}")
        except Exception:
            pass
