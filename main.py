import time
from packet_simulator import generate_fake_deauth
from logger import init_log, log_deauth, export_json
from analyzer import analyze, update_rolling_offenders
from alerts import print_alerts
from visualizer import update_graph
from utils.spoof_detector import detect_spoofing

def main():
    init_log()
    print("🔍 Deauth Detection Running...\n")
    try:
        while True:
            deauth_packets = generate_fake_deauth()
            log_deauth(deauth_packets)
            update_rolling_offenders(deauth_packets)
            high_risk = analyze(deauth_packets)
            spoofed_macs = detect_spoofing()
            print_alerts(high_risk, spoofed_macs)
            update_graph(deauth_packets)
            time.sleep(2)
    except KeyboardInterrupt:
        export_json()
        print("\n🛑 Detection Stopped. JSON log saved.")

if __name__ == "__main__":
    main()
