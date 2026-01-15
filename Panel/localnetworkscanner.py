import socket
import sys
import time
import os

if sys.platform == 'win32':
    os.system('cls')

print("+" * 50)
print("       LOCAL AREA NETWORK (LAN) SCANNER")
print("+" * 50)
print("\n")

base_ip = input("[?] Enter Base IP (e.g., 192.168.1): ")
range_start = 1
range_end = 20 

print(f"\n[*] Initializing scan on {base_ip}.{range_start} to {base_ip}.{range_end}")
print("[*] Checking active hosts (ICMP/TCP)...")
time.sleep(1)
print("\n")

active_hosts = []

try:
    for i in range(range_start, range_end + 1):
        target = f"{base_ip}.{i}"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target, 135))
        
        if result == 0:
            print(f"[+] HOST ONLINE: {target}")
            active_hosts.append(target)
        else:
            # Optional: Print offline hosts or keep silent for clean output
            pass
        s.close()

except KeyboardInterrupt:
    print("\n[-] Scan stopped by user.")
    sys.exit()
except socket.error:
    print("[-] Network error.")

print("\n" + "+" * 50)
print(f"[*] Scan complete. Found {len(active_hosts)} active devices.")
input("Press Enter to exit...")