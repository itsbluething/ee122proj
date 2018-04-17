import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DIR_NAME = "./data/"
PROTOCOL_LIST = ['DHCP', 'DNS', 'HTTP', 'HTTP/XML', 'ICMP', 'ICMPv6', 'IGMPv3', 'LLMNR', 'MDNS', 'NBNS', 'OCSP', 'QUIC', 'SSDP', 'SSL', 'SSLv2', 'TCP', 'TLSv1', 'TLSv1.2', 'TLSv1.3', 'UDP', 'ARP']
df = pd.read_csv(DIR_NAME + 'pcap.csv')
df['int_time'] = df['Time'].apply(lambda x:np.floor(x/60))

def group_by(col):
	grouped = df.groupby([col])[col].count().sort(['count'])
	return grouped

def example():
	pass

def dest_recv_most():
	temp=df.groupby(['Destination']).sum().sort_values('Length',ascending=False)
	temp.to_csv('data/dest_recv_most.csv')

def src_send_most():
	temp=df.groupby(['Source']).sum().sort_values('Length',ascending=False)
	temp.to_csv('data/src_send_most.csv')

def count_packet_type():
	temp = df.groupby(['Protocol'])['Length'].agg([np.sum,np.mean,np.std])
	temp.to_csv('data/each_type.csv')
	temp.plot(y='sum',kind='bar',title='Bar graph of Length Sum')
	plt.savefig(DIR_NAME+'Sum.png')
	temp.plot(y='mean',kind='bar',title='Bar graph of Length Mean')
	plt.savefig(DIR_NAME+'Mean.png')
	temp.plot(y='std',kind='bar',title='Bar graph of Length Std')
	plt.savefig(DIR_NAME+'Std.png')

	temp = df.groupby(['Protocol']).count()['Info']
	temp.plot(kind='bar',title='Bar graph of Count Sum')
	plt.savefig(DIR_NAME+'count_sum.png')
	temp.to_csv('data/each_type_count.csv')

def stat_per_minute():
	temp=df.groupby('int_time')['Length'].sum()
	temp.to_csv(DIR_NAME+'bytes_per_minute.csv')
	temp.plot(title='Real time packets statistics')
	plt.savefig(DIR_NAME+'bytes_per_minute_graph.png')

def extract_fin():
	df[df['Info'].str.contains("FIN")].count().to_csv(DIR_NAME+'FIN.csv')

def UDP_stat():
	pass

def main():
	dest_recv_most()
	src_send_most()
	count_packet_type()
	stat_per_minute()
	extract_fin()

if __name__ == '__main__':
	main()
