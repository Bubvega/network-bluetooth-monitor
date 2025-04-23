from flask import Flask, jsonify
import subprocess
import re

app = Flask(__name__)

def scan_network():
    devices = []
    try:
        result = subprocess.run(['nmap', '-sn', '-Pn', '192.168.1.0/24'], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if "Nmap scan report for" in line:
                ip = line.split()[-1]
                devices.append({"ip": ip, "mac": None, "type": "network"})
    except Exception as e:
        print(f"Errore scansione rete: {e}")
    return devices

def scan_bluetooth():
    devices = []
    try:
        result = subprocess.run(['blueutil', '--paired'], capture_output=True, text=True)
        for line in result.stdout.strip().split("\n"):
            match = re.search(r'address: ([0-9A-F:-]+)', line)
            if match:
                mac = match.group(1)
                devices.append({"ip": None, "mac": mac, "type": "bluetooth"})
    except Exception as e:
        print(f"Errore scansione bluetooth: {e}")
    return devices

@app.route("/devices")
def devices():
    return jsonify(scan_network() + scan_bluetooth())

if __name__ == "__main__":
    app.run(debug=True)