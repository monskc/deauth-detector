import matplotlib.pyplot as plt
from collections import defaultdict

mac_rssi_history = defaultdict(list)
plt.ion()
fig, ax = plt.subplots()

def update_graph(packets):
    ax.clear()
    for pkt in packets:
        mac = pkt['mac']
        rssi = pkt['rssi']
        mac_rssi_history[mac].append(rssi)
        if len(mac_rssi_history[mac]) > 20:
            mac_rssi_history[mac] = mac_rssi_history[mac][-20:]
        ax.plot(mac_rssi_history[mac], label=mac)
    ax.set_title("Live RSSI per MAC")
    ax.set_ylabel("RSSI (dBm)")
    ax.set_xlabel("Time")
    ax.legend(loc="upper right", fontsize="small")
    plt.pause(0.01)
