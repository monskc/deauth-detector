def print_alerts(high_risk_list, spoofed_macs):
    for mac in high_risk_list:
        print(f"[ALERT] 📡 Device {mac} is too close and sending deauths!")
    for mac in spoofed_macs:
        print(f"[WARNING] 🕵️ Potential spoofing detected for MAC {mac}")
