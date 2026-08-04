import socket
import sys

UDP_IP = "0.0.0.0" # Listen on all local interfaces inside the VM boundary
UDP_PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"[+] SECOND PIANO RUNNING (VM-SIDE): Listening natively on port {UDP_PORT}...")
print("------------------------------------------------------------------")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        payload = data.decode('ascii', errors='ignore')
        print(f"[Hyper-V Boundary Collision] -> {payload}", flush=True)
except KeyboardInterrupt:
    print("\n[-] Second piano disconnected from Hyper-V pipeline.")
finally:
    sock.close()
