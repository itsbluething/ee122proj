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
	pass
def Dest_rece_most():
	temp=df1.groupby(['Source']).sum().sort_values('Length',ascending=False)
	temp.to_csv('data/Src_send_most.csv')
def Src_send_most():
	temp=df1.groupby(['Destination']).sum().sort_values('Length',ascending=False)
	temp.to_csv('data/Dest_rec_most.csv')
def Count_packet_type():
	for i in PROTOCOL_LIST:
		temp =df[df['Protocol']==i]
		if i=='HTTP/XML':
			temp.groupby(['Protocol']).count().to_csv('HTTP_XML.csv')
		else:
			temp.groupby(['Protocol']).count().to_csv(i+'.csv')
def main():
    Count_packet_type()


if __name__ == '__main__':
    main()
