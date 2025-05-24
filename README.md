# Deauth Culprit Detection & Localization in a Crowded Network Environment

## 📚 Overview
This project simulates a Deauthentication (Deauth) attack detector for Wi-Fi networks. It estimates the physical proximity of potential attackers using RSSI (signal strength), detects MAC spoofing behavior, and provides real-time alerts.

This is a simulation tool, designed to work even without requiring Wi-Fi cards in monitor mode. Hooks for Scapy integration (monitor mode) are included for future expansion.

## 🚀 Features
✅ Simulated deauthentication frame detection
✅ MAC address, RSSI, and timestamp logging (CSV & JSON)
✅ Proximity alerts for high-risk devices (RSSI > -50 dBm)
✅ MAC spoofing detection via RSSI pattern analysis
✅ Live RSSI graph per MAC (matplotlib-based)
✅ Modular Python code (easy to extend)
✅ Lightweight — runs on VirtualBox, no hardware required
✅ Hooks for future monitor mode integration with Scapy

## 📂 Folder Structure
deauth-detector/
├── main.py               # Entry point: orchestrates the detection system
├── packet_simulator.py   # Generates fake packets for testing the system
├── analyzer.py           # Detects deauth patterns from sniffed packets
├── logger.py             # Logs detected events to CSV/JSON files
├── alerts.py             # Sends terminal alerts
├── visualizer.py         # Visualizes RSSI and attack patterns
├── utils/
│   ├── rssi_distance.py  # Estimates distances using RSSI values
│   └── spoof_detector.py # Detects potential MAC spoofing attempts
├── data/
│   ├── logs.csv          # CSV log file for detected events
│   └── logs.json         # JSON log file for detected events
├── Screenshots/
│   ├── terminal_alerts.png
│   ├── rssi_graph1.png
│   └── rssi_graph2.png
├── README.md             # Project details

## 🛠️ Setup & Installation
1️⃣ Clone the repo or download the files.

2️⃣ Install dependencies:
sudo apt update
sudo apt install python3-matplotlib -y


3️⃣ Run the detector:
cd deauth-detector
python3 main.py

4️⃣ Watch for live alerts in the terminal and RSSI graphs in the popup window.

## 📊 JSON & CSV Logs
CSV Log: data/logs.csv
JSON Export: data/logs.json (saved on exit)

## 🎓 Goals
✔️ Understand Wi-Fi deauthentication attacks
✔️ Learn RSSI-based proximity estimation
✔️ Detect MAC spoofing patterns
✔️ Practice Python modular design
✔️ Build real-time data visualizations

## 📦 Deliverables
✅ Codebase (Python, modular)
✅ README.md (setup + usage instructions)
✅ Sample Screenshots & Logs (alerts, RSSI graph, JSON/CSV logs)
✅ MAC Spoofing Detection logic
✅ Proximity Estimation & Alerts
✅ Optional Scapy Monitor Mode Hook (for real hardware detection)
✅ (Bonus) Triangulation logic stub for future multi-node extensions
