# SMTP Packet Extractor.

This Python script utilizes the scapy library to extract SMTP packets and their contents from a pcap file. It is particularly useful for analyzing SMTP traffic captured in pcap format. SMTP (Simple Mail Transfer Protocol) is a widely used protocol for sending emails over the internet.

## Usage.
    - Ensure you have scapy installed.
    - Provide the path to your pcap file in the pcap_file variable.
    - Run the script.

## Description.

    The script defines two main functions:
       - extract_smtp_packets(pcap_file): This function reads the pcap file and filters out SMTP packets based on their TCP ports (port 25).
       - extract_smtp_content(smtp_packets): This function extracts the content of SMTP packets.
    After extracting the SMTP contents, the script prints them out.

## Note.

    - Make sure to replace 'Files\smtp.pcap' with the path to your actual pcap file.
    - This script only extracts SMTP packets and their contents. If you need more advanced analysis or processing, you may need to extend it accordingly.


## Developer.

    Developed by: Ahmed Hossam Morgan
    Email: ahmedhossammorgan@gmail.com
    Linkedin: https://www.linkedin.com/in/ahmedhossameldeen/
