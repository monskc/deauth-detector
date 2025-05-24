import math

def rssi_to_distance(rssi, tx_power=-40, n=2.0):
    return round(10 ** ((tx_power - rssi) / (10 * n)), 2)
