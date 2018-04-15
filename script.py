import pandas as pd
df = pd.read_csv('pcap.csv')
protocol_list=['DHCP', 'DNS', 'HTTP', 'HTTP/XML', 'ICMP', 'ICMPv6', 'IGMPv3', 'LLMNR', 'MDNS', 'NBNS', 'OCSP', 'QUIC', 'SSDP', 'SSL', 'SSLv2', 'TCP', 'TLSv1', 'TLSv1.2', 'TLSv1.3', 'UDP', 'ARP']
for i in protocol_list:
     temp=df[df['Protocol']==i]
     if i=='HTTP/XML':
             temp[['Destination','Length']].groupby(['Destination']).count().to_csv('HTTP_XML.csv')
     else:
             temp[['Destination','Length']].groupby(['Destination']).count().to_csv(i+'.csv')
