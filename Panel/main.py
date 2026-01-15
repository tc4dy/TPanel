#Developed by @tc4dy, this is a simple and free educational tool for learning algorithms and how they work.

import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("=" * 60)
    print("            TC4DY | MASTER COMMAND CENTER")
    print("=" * 60)
    
    tools = {
        "1": "ARP Spoofer", "2": "Deauth Attack", "3": "Domain to IP",
        "4": "Fake Blue Screen", "5": "File Masking", "6": "Hidden Art Discovery",
        "7": "LAN File Transfer", "8": "Local Network Scanner", "9": "MAC Changer",
        "10": "Network Analyzer", "11": "Network Tester", "12": "Port Scanner",
        "13": "Persistence Script", "14": "Service Grabber", "15": "Traffic Sniffer",
        "16": "SQL Vulnerability Scanner", "17": "Storage Analysis", "18": "System Info",
        "19": "Text Analyst", "20": "Text Base64 Encryptor", "21": "Wi-Fi Explorer"
    }

    files = {
        "1": "arpspoofer.py", "2": "deauthattack.py", "3": "domaintoip.py",
        "4": "fakebs.py", "5": "filexmasq.py", "6": "hiddenartdiscovery.py",
        "7": "lantransfer.py", "8": "localnetworkscanner.py", "9": "macchanger.py",
        "10": "networkanalyzer.py", "11": "networktester.py", "12": "portscanner.py",
        "13": "resistencesoft.py", "14": "servicegrabber.py", "15": "sniffer.py",
        "16": "sqlvuln.py", "17": "storageananalyses.py", "18": "systeminfo.py",
        "19": "textanalyst.py", "20": "textbase64.py", "21": "wifiexplorer.py"
    }

    for key in sorted(tools.keys(), key=int):
        print(f"[{key.zfill(2)}] {tools[key]}")

    print("=" * 60)
    choice = input("[?] Enter tool number (or 'q' to quit): ")

    if choice.lower() == 'q':
        sys.exit()
    
    if choice in files:
        script_name = files[choice]
        
        if os.path.exists(script_name):
            print(f"\n[*] Launching {tools[choice]}...")
            time.sleep(1)
            os.system(f"python {script_name}")
            print("\n" + "-"*45)
            input("Execution finished. Press Enter to return to Master Panel...")
        else:
            print(f"\n[!] Error: File '{script_name}' NOT FOUND in current directory!")
            time.sleep(3)
    else:
        print("\n[!] Invalid Selection!")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        try:
            main_menu()
        except KeyboardInterrupt:
            print("\n\n[!] Exiting...")
            sys.exit()