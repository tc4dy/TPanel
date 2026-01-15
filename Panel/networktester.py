import os
import time
import sys

if sys.platform == 'win32':
    os.system('cls')

print("::" * 25)
print("       NETWORK LATENCY & CONNECTIVITY TESTER")
print("::" * 25)
print("\n")

host = input("[?] Enter Target Host (IP or Domain): ")
count = input("[?] Enter Packet Count (Default 4): ")

if not count.isdigit():
    count = 4

print(f"\n[*] Initializing ping sequence to {host}...")
time.sleep(1)
print("[*] Sending ICMP packets...")
time.sleep(1)
print("\n")

if sys.platform == "win32":
    command = f"ping -n {count} {host}"
else:
    command = f"ping -c {count} {host}"

os.system(command)

print("\n[*] Connectivity test completed.")
input("Press Enter to close...")