import subprocess
import time
import os
import sys
import random

print("M" * 60)
print("        MAC ADDRESS SPOOFER & IDENTITY STEALTH")
print("M" * 60)

def get_rand():
    return ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])

interface = input("\n[?] Enter Interface Name: ")
new_mac = get_rand()

print(f"\n[*] New MAC Generated: {new_mac}")
time.sleep(1)

try:
    if sys.platform == "win32":
        print("[!] Manual registry update or netsh cycle required on Windows.")
    else:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
        print("[+] MAC Spoofed successfully.")
except Exception as e:
    print(f"[-] Error: {e}")

input("\nPress Enter to exit...")