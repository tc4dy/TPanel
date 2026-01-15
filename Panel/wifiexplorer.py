import sys
import time
import os
try:
    from scapy.all import sniff, Dot11Beacon, Dot11, Dot11Elt
except ImportError:
    print("bilgilendirme: 'scapy' kütüpheasnei gerekir")
    sys.exit()

if sys.platform == 'win32':
    os.system('cls')

print("W" * 60)
print("        ADVANCED WI-FI SIGNAL EXPLORER")
print("W" * 60)

found_nets = {}

def handle_packet(pkt):
    if pkt.haslayer(Dot11Beacon):
        bssid = pkt[Dot11].addr2
        if bssid not in found_nets:
            ssid = pkt[Dot11Elt].info.decode(errors="ignore")
            found_nets[bssid] = ssid
            print(f"[+] DISCOVERED: {ssid:<20} | MAC: {bssid}")

interface = input("\n[?] Enter Monitoring Interface (e.g., wlan0): ")
print(f"\n[*] Scanning for wireless beacons on {interface}...")
time.sleep(1)

try:
    sniff(iface=interface, prn=handle_packet, timeout=30, store=0)
except Exception as e:
    print(f"\n[-] Error: {e}")

print(f"\n[*] Scan complete. Total unique networks found: {len(found_nets)}")
input("Press Enter to exit...")