import random
import time

def generate_fake_deauth():
    mac_prefixes = ["00:11:22", "AA:BB:CC", "DE:AD:BE"]
    deauths = []
    for _ in range(random.randint(1, 5)):
        mac = f"{random.choice(mac_prefixes)}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}"
        rssi = random.randint(-80, -30)
        timestamp = time.time()
        deauths.append({
            "mac": mac,
            "rssi": rssi,
            "timestamp": timestamp
        })
    return deauths
