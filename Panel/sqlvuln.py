import requests
import time
import sys

print("-" * 60)
print("        SQL INJECTION (SQLi) VULNERABILITY SCANNER")
print("-" * 60)

target_url = input("\n[?] Enter Target URL: ")
payload = "'"

print(f"\n[*] Injecting test payload...")
time.sleep(1.5)

try:
    res1 = requests.get(target_url)
    res2 = requests.get(target_url + payload)
    if res1.text != res2.text:
        print("\n[+] VULNERABILITY DETECTED: SQL Injection potential.")
    else:
        print("\n[-] No immediate vulnerability found.")
except Exception as e:
    print(f"[-] Error: {e}")

input("\nPress Enter to exit...")