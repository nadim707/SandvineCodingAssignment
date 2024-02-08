import sys
from scapy.all import *
import re
from tqdm import tqdm
import os
from scapy.layers.inet import TCP

class PcapReader():
    def __init__(self, pcap_file_path):
        self.pcap_file_path = pcap_file_path

    def pcapreader(self):
        # initialize variables
        host_traffic = dict()
        http_flow_count, http_bytes_count = 0, 0
        
        # read pcap file and get a list of packets
        pkts = rdpcap(self.pcap_file_path)

        # iterate over each packet and check if its TCP and has data traffic
        for pkt in tqdm(pkts):
            if pkt.haslayer(TCP) and pkt.haslayer(Raw):
                data_traffic_object = pkt[Raw].load
                data_traffic = data_traffic_object.decode('utf-8', errors='ignore')
                if 'HTTP' in data_traffic:
                    http_flow_count += 1
                    http_bytes_count += len(pkt)
                    hostname_pattern = r'Host: (.+)\r\n'
                    host_header = re.search(hostname_pattern, data_traffic)
                    if host_header:
                        hostname = host_header.group(1)
                        host_traffic[hostname] = host_traffic.get(hostname, 0) + len(pkt)

        if http_flow_count == 0:
            print("HTTP traffic untraceable, Enter a pcap file with HTTP packet capture.")
        else:
            print(f"HTTP traffic flows: {http_flow_count}")
            print(f"HTTP traffic bytes: {http_bytes_count}")
        if host_traffic:
            top_hostname_by_byte_transmitted = max(host_traffic, key=host_traffic.get)
            print(f"Top HTTP hostname: {top_hostname_by_byte_transmitted}")
        else:
            print("HTTP hostname(s) not found.")

if __name__ == "__main__":
    pcap_file_path = os.getenv("filename")
    if not pcap_file_path:
        print("Please provide the valid pcap path")
    else:
        pcap_reader_obj = PcapReader(pcap_file_path)
        pcap_reader_obj.pcapreader()
