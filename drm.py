import pandas as db
df1 = db.read_csv('data/pcap.csv')
temp=df1.groupby(['Source']).sum().sort_values('Length')
temp.to_csv('data/Dest_rec_most.csv')
