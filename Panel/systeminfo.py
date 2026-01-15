import platform
import socket
import os
import sys
import time

if sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')

print("=" * 60)
print("          SYSTEM DIAGNOSTICS & INFO TOOL")
print("=" * 60)
print("\n[*] Analyzing system hardware and software...")
time.sleep(2)
print("[*] Fetching network configuration...")
time.sleep(1.5)
print("\n")

try:
    info = {
        "OS System": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Python Version": platform.python_version()
    }

    for key, value in info.items():
        print(f"{key:<20} : {value}")
        time.sleep(0.2)

except Exception as e:
    print(f"[-] An error occurred: {e}")

print("\n" + "=" * 60)
print("[*] Diagnostics complete.")
input("\nPress Enter to return to menu...")