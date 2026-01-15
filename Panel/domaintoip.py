import socket
import time
import sys
import os

if sys.platform == 'win32':
    os.system('cls')

print("#" * 50)
print("        DOMAIN NAME SYSTEM (DNS) RESOLVER")
print("#" * 50)
print("\n")

domain = input("[?] Enter the website/domain (e.g., google.com): ")

print("\n[*] Connecting to DNS server...")
time.sleep(1)
print("[*] Querying database...")
time.sleep(1.5)

try:
    ip_address = socket.gethostbyname(domain)
    print("\n" + "-" * 30)
    print(f"TARGET  : {domain}")
    print(f"ADDRESS : {ip_address}")
    print("-" * 30)
except socket.gaierror:
    print("\n[-] Error: Invalid Domain or Network Issue.")
except Exception as e:
    print(f"\n[-] Unexpected Error: {e}")

print("\n[*] Operation finished.")
input("Press Enter to continue...")