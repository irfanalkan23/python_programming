# the scapy package needs to be installed

from scapy.all import *   # to be able to use all the function of scapy

pcap_file_path = "../files/network_sec_monitoring.pcap"  # located the pcap file that I need to analyze

packets = rdpcap(pcap_file_path)  # reading all the packets from pcap file


for packet in packets:  # getting each packet
    print(packet.summary()) # summary of the packet