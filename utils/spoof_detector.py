from analyzer import ROLLING_LOG

def detect_spoofing():
    spoofed = []
    macs = list(ROLLING_LOG.keys())
    for i in range(len(macs)):
        for j in range(i + 1, len(macs)):
            mac1, mac2 = macs[i], macs[j]
            rssi1 = [x["rssi"] for x in ROLLING_LOG[mac1]]
            rssi2 = [x["rssi"] for x in ROLLING_LOG[mac2]]
            if len(rssi1) > 3 and len(rssi2) > 3:
                overlap = sum(abs(a - b) < 3 for a, b in zip(rssi1, rssi2))
                if overlap > 3:
                    spoofed.extend([mac1, mac2])
    return list(set(spoofed))
