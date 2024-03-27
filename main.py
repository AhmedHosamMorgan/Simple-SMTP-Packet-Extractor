from scapy.all import *

def extract_smtp_packets(pcap_file):
    smtp_packets = []
    try:
        packets = rdpcap(pcap_file)
        for packet in packets:
            if packet.haslayer(TCP) and packet.haslayer(Raw):
                if packet[TCP].dport == 25 or packet[TCP].sport == 25:
                    smtp_packets.append(packet)
    except Exception as e:
        print("Error reading pcap file:", e)
    return smtp_packets

def extract_smtp_content(smtp_packets):
    smtp_contents = []
    for packet in smtp_packets:
        smtp_contents.append(packet[Raw].load.decode('utf-8', 'ignore'))
    return smtp_contents

# Example usage
pcap_file = 'Files\smtp.pcap'
smtp_packets = extract_smtp_packets(pcap_file)
smtp_contents = extract_smtp_content(smtp_packets)

for content in smtp_contents:
    print(content)
