import socket
import os
import sys
import time

def start_server(port=5005):
    # Initialize server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    
    print("=" * 50)
    print("       STATUS: LISTENING FOR INCOMING FILE")
    print("=" * 50)
    print(f"[*] Local IP Address: {socket.gethostbyname(socket.gethostname())}")
    print(f"[*] Listening on Port: {port}")
    print("[*] Waiting for connection...")

    try:
        conn, addr = server_socket.accept()
        print(f"[+] Connection established from: {addr}")

        # Receive filename first
        filename = conn.recv(1024).decode()
        print(f"[*] Receiving: {filename}")

        # Open file and write incoming data
        with open(f"received_{filename}", "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        
        print(f"\n[SUCCESS] File saved as 'received_{filename}'")
    except Exception as e:
        print(f"\n[ERROR] Transfer failed: {e}")
    finally:
        conn.close()
        server_socket.close()

def start_client(target_ip, file_path, port=5005):
    if not os.path.exists(file_path):
        print("[!] ERROR: File not found in the specified path.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"[*] Connecting to {target_ip}...")
        client_socket.connect((target_ip, port))
        
        # Send filename
        filename = os.path.basename(file_path)
        client_socket.send(filename.encode())
        
        time.sleep(1) # Small delay for synchronization

        # Read and send file data
        with open(file_path, "rb") as f:
            print(f"[*] Sending '{filename}'...")
            client_socket.sendall(f.read())
        
        print("\n[SUCCESS] Data transmission complete!")
    except Exception as e:
        print(f"\n[ERROR] Connection failed: {e}")
    finally:
        client_socket.close()

# Main UI
print("F" * 60)
print("        REMOTE FILE COMMAND CENTER (v1.0)")
print("F" * 60)

print("\n[1] RECEIVER MODE (Listen)")
print("[2] SENDER MODE (Transmit)")
choice = input("\n[?] Select Operation Mode: ")

if choice == '1':
    start_server()
elif choice == '2':
    ip = input("[?] Enter Receiver IP: ")
    path = input("[?] Enter File Name/Path: ")
    start_client(ip, path)
else:
    print("[!] Invalid selection.")