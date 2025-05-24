import csv, json
from pathlib import Path

LOG_FILE_CSV = Path("data/logs.csv")
LOG_FILE_JSON = Path("data/logs.json")
ALL_PACKETS = []

def init_log():
    LOG_FILE_CSV.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE_CSV.exists():
        with open(LOG_FILE_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "mac", "rssi"])

def log_deauth(packets):
    ALL_PACKETS.extend(packets)
    with open(LOG_FILE_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        for pkt in packets:
            writer.writerow([pkt["timestamp"], pkt["mac"], pkt["rssi"]])

def export_json():
    with open(LOG_FILE_JSON, "w") as f:
        json.dump(ALL_PACKETS, f, indent=2)
