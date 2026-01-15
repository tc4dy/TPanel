import base64
import sys
import time
import os

if sys.platform == 'win32':
    os.system('cls')

print("X" * 60)
print("       CRYPTOGRAPHIC TEXT ENGINE (BASE64 ENCODER)")
print("X" * 60)
print("\n")

print("[1] Encrypt Text (Make unreadable)")
print("[2] Decrypt Text (Restore original)")
choice = input("\n[?] Select Mode: ")

if choice == '1':
    raw_data = input("\n[?] Enter text to encrypt: ")
    print("\n[*] Processing encryption algorithm...")
    time.sleep(1)
    encoded_bytes = base64.b64encode(raw_data.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")
    print("-" * 40)
    print(f"RESULT: {encoded_str}")
    print("-" * 40)

elif choice == '2':
    enc_data = input("\n[?] Enter text to decrypt: ")
    print("\n[*] Processing decryption algorithm...")
    time.sleep(1)
    try:
        decoded_bytes = base64.b64decode(enc_data)
        decoded_str = decoded_bytes.decode("utf-8")
        print("-" * 40)
        print(f"RESULT: {decoded_str}")
        print("-" * 40)
    except:
        print("\n[-] Error: Invalid format or corrupted data.")

else:
    print("[-] Invalid selection.")

input("\nPress Enter to return to main menu...")