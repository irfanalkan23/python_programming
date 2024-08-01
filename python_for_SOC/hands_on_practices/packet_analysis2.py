from scapy.all import *  # to be able to use all the function of scapy

pcap_file_path = "../files/network_sec_monitoring2.pcap"  # located the pcap file that I need to analyze

packets = rdpcap(pcap_file_path)  # reading all the packets from pcap file

for packet in packets:  # getting each packet
    print(packet.summary())

print("--------------------------------")

total_packets = len(packets)
tcp_packets = 0
udp_packets = 0
icmp_packets = 0
arp_packets = 0

for packet in packets:
    if packet.haslayer("TCP"):
        tcp_packets += 1
    elif packet.haslayer("UDP"):
        udp_packets += 1
    elif packet.haslayer("ICMP"):
        icmp_packets += 1
    elif packet.haslayer("ARP"):
        arp_packets += 1

print(f"Total Packets: {total_packets}")
print(f"TCP Packets: {tcp_packets}")
print(f"UDP Packets: {udp_packets}")
print(f"ICMP Packets: {icmp_packets}")
print(f"ARP Packets: {arp_packets}")


print("--------------------------------")

for packet in packets:
    if packet.haslayer("ARP"):
        print(packet.summary())