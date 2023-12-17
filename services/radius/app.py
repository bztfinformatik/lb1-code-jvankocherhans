import socket
import requests
from scapy.all import IP, ICMP

# Eingehende Pakete bearbeiten
def handlePacket(packet):
    if ICMP in packet and packet[ICMP].type == 8:  # ICMP Echo Request
        # ICMP Paket extrahieren
        payload = str(packet[ICMP].payload)
        
        # Speicherung des Switch Status in der Lsogging/Reactions Datenbank
        api_url = "http://backend/actvities"
        headers = {'Content-Type': 'application/json'}
        data = {'payload': payload}

        response = requests.post(api_url, json=data, headers=headers)

        # Ausgabe API-Response im Terminal
        print("API-response:", response.text)

# ICMP-Socket Listener für eingehende Pakete
def startListener():
    print("Starting RADIUS Service...")
    # Reagiert nur auf ICMP / Port 1508 Anfragen
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as icmp_socket:
        while True:
            data, addr = icmp_socket.recvfrom(1508) 
            packet = IP(data)
            handlePacket(packet)

startListener()
