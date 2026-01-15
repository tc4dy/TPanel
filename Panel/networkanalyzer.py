import subprocess
import time
import sys
import os

if sys.platform == 'win32':
    os.system('cls')

print("=" * 60)
print("          WIRELESS NETWORK SIGNAL ANALYZER")
print("=" * 60)
print("\n[*] Initializing wireless adapter...")
time.sleep(1.5)
print("[*] Scanning for available networks...")
time.sleep(2)
print("\n")

try:
    if sys.platform == "win32":
        data = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"]).decode("utf-8", errors="ignore")
        print(data)
    else:
        print("[-] This tool is optimized for Windows systems.")

except subprocess.CalledProcessError:
    print("[-] Error: Could not execute wireless scan.")
except Exception as e:
    print(f"[-] Unexpected Error: {e}")

print("=" * 60)
print("[*] Scan complete.")
input("Press Enter to refresh or close...")