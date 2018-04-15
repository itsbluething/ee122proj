import pandas as pd

DIR_NAME = "./data"
df = pd.read_csv(DIR_NAME + 'pcap.csv')
"""
protocol_list=['DHCP', 'DNS', 'HTTP', 'HTTP/XML', 'ICMP', 'ICMPv6', 'IGMPv3', 'LLMNR', 'MDNS', 'NBNS', 'OCSP', 'QUIC', 'SSDP', 'SSL', 'SSLv2', 'TCP', 'TLSv1', 'TLSv1.2', 'TLSv1.3', 'UDP', 'ARP']
for i in protocol_list:
     temp=df[df['Protocol']==i]
     if i=='HTTP/XML':
         temp[['Destination','Length']].groupby(['Destination']).count().to_csv('HTTP_XML.csv')
     else:
         temp[['Destination','Length']].groupby(['Destination']).count().to_csv(i+'.csv')
"""

def main():
    pass

if __name__ == '__main__':
    print "test"
    pass
