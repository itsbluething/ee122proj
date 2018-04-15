import pandas as pd

DIR_NAME = "./data/"
PROTOCOL_LIST = ['DHCP', 'DNS', 'HTTP', 'HTTP/XML', 'ICMP', 'ICMPv6', 'IGMPv3', 'LLMNR', 'MDNS', 'NBNS', 'OCSP', 'QUIC', 'SSDP', 'SSL', 'SSLv2', 'TCP', 'TLSv1', 'TLSv1.2', 'TLSv1.3', 'UDP', 'ARP']
df = pd.read_csv(DIR_NAME + 'pcap.csv')

"""
for i in protocol_list:
     temp=df[df['Protocol']==i]
     if i=='HTTP/XML':
         temp[['Destination','Length']].groupby(['Destination']).count().to_csv('HTTP_XML.csv')
     else:
         temp[['Destination','Length']].groupby(['Destination']).count().to_csv(i+'.csv')
"""

def example():

def main():
    print "test"

if __name__ == '__main__':
    main()
    pass
