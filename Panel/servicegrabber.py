import socket
import time
import sys
import os

if sys.platform == 'win32':
    os.system('cls')

print("B" * 60)
print("        SERVICE BANNER GRABBER & FINGERPRINTING")
print("B" * 60)

target = input("\n[?] Enter Target IP or Domain: ").strip().replace("'", "").replace('"', "")
port_input = input("[?] Enter Port to Audit (e.g., 21, 22, 80): ")

try:
    port = int(port_input)
    print(f"\n[*] Probing service on {target}:{port}...")
    time.sleep(1.5)

    s = socket.socket()
    s.settimeout(3)
    s.connect((target, port))
    
    # Triggering the banner response
    s.send(b'Hello\r\n')
    banner = s.recv(1024).decode(errors='ignore').strip()
    
    print("\n" + "=" * 45)
    print(f"[+] SERVICE DATA: {banner if banner else 'No banner returned (Stealth)'}")
    print("=" * 45)
    
except Exception as e:
    print(f"\n[-] Audit failed. Connection error or invalid address.")

finally:
    try: s.close()
    except: pass

input("\nPress Enter to return to menu...")