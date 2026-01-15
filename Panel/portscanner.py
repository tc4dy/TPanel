import socket
import sys
import time
from datetime import datetime

os_type = sys.platform
if os_type == 'win32':
    import os
    os.system('cls')
else:
    import os
    os.system('clear')

print("-" * 50)
print("     NETWORK PORT SCANNER v2.0")
print("-" * 50)
print("\n")

target = input("[?] Enter Target Domain or IP: ")

print("\n")
print(f"[*] Resolving host: {target}")
time.sleep(1.5)

try:
    target_ip = socket.gethostbyname(target)
    print(f"[*] Target IP: {target_ip}")
except socket.gaierror:
    print("[-] Error: Hostname could not be resolved.")
    sys.exit()

print(f"[*] Scan started at: {datetime.now()}")
print("-" * 50)
time.sleep(1)

ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port:<5} : OPEN")
        s.close()
        
except KeyboardInterrupt:
    print("\n[-] Exiting program...")
    sys.exit()
except socket.error:
    print("\n[-] Server not responding.")
    sys.exit()

print("-" * 50)
print("[*] Scan completed successfully.")
input("\nPress Enter to exit...")