import sys
try:
    from scapy.all import sniff
except ImportError:
    print("bilgilendirme: 'scapy' kütüpheasnei gerekir")
    sys.exit()

print("N" * 60)
print("        NETWORK TRAFFIC SNIFFER")
print("N" * 60)

def process(pkt):
    if pkt.haslayer("IP"):
        print(f"[*] Traffic: {pkt['IP'].src} -> {pkt['IP'].dst}")

print("\n[*] Sniffing active traffic (Ctrl+C to stop)...")
try:
    sniff(prn=process, store=0)
except Exception as e:
    print(f"[-] Error: {e}")