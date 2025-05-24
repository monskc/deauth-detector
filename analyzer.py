from collections import defaultdict
from time import time

ROLLING_LOG = defaultdict(list)
OFFENDER_COUNT = defaultdict(int)

def analyze(packets):
    high_risk = []
    now = time()
    for pkt in packets:
        mac = pkt['mac']
        rssi = pkt['rssi']
        timestamp = pkt['timestamp']
        ROLLING_LOG[mac] = [p for p in ROLLING_LOG[mac] if now - p['timestamp'] < 60]
        ROLLING_LOG[mac].append(pkt)
        if rssi > -50:
            high_risk.append(mac)
    return list(set(high_risk))

def update_rolling_offenders(packets):
    for pkt in packets:
        OFFENDER_COUNT[pkt['mac']] += 1
