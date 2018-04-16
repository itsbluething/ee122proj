import pandas as pd
import numpy as np

DIR_NAME = "./data/"
PROTOCOL_LIST = ['DHCP', 'DNS', 'HTTP', 'HTTP/XML', 'ICMP', 'ICMPv6', 'IGMPv3', 'LLMNR', 'MDNS', 'NBNS', 'OCSP', 'QUIC', 'SSDP', 'SSL', 'SSLv2', 'TCP', 'TLSv1', 'TLSv1.2', 'TLSv1.3', 'UDP', 'ARP']
df = pd.read_csv(DIR_NAME + 'pcap.csv')

def group_by(col):
    grouped = df.groupby([col])[col].count().sort(['count'])
    return grouped

def example():
    pass

def dest_recv_most():
    temp=df.groupby(['Source']).sum().sort_values(['Length'])
    temp.to_csv('data/src_send_most.csv')
    
def src_send_most():
    temp=df.groupby(['Destination']).sum().sort_values(['Length'])
    temp.to_csv('data/dest_recv_most.csv')

def count_packet_type():
    temp = df.groupby(['Protocol'])['Length'].agg([np.sum,np.mean,np.std])
    temp.to_csv('data/each_type.csv')

def stat_per_minute():
	temp=df.groupby('Time')['Time'].aggregate(lambda x:np.floor(x/60))
	temp.to_csv('test.csv')
def main():
    dest_recv_most()
    src_send_most()
    count_packet_type()
    stat_per_minute()

if __name__ == '__main__':
    main()
