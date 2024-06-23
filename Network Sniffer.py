from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        print(f"Source IP: {packet[IP].src} -> Destination IP: {packet[IP].dst}")

sniff(filter="ip", prn=packet_handler)
