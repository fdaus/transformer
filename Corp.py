#! /bin/env python
import pandas as pd
import glob, os

source = "/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/nfstream/split/output_done_8.csv"
outputPath = "/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/nfstream/corpus/unsw_corpus8.csv"

cname=['id', 'expiration_id','src_ip', 'src_mac', 'src_oui','sp',
       'dst_ip', 'dst_mac', 'dst_oui','dp', 'ptcl', 'ipv', 
       'vln','tnnl', 'bidirectional_first_seen_ms',
       'bidirectional_last_seen_ms', 'bi_dur',
       'bi_pkt', 'bi_byte', 'src2dst_first_seen_ms',
       'src2dst_last_seen_ms', 's2d_dur', 's2d',
       's2d_byte', 'dst2src_first_seen_ms', 'dst2src_last_seen_ms',
       'd2s_dur', 'd2s', 'd2s_byte', 'bi_min_ps', 'bi_mean_ps',
       'bi_std_ps', 'bi_max_ps', 's2d_min_ps',
       's2d_mean_ps', 's2d_std_ps', 's2d_max_ps',
       'd2s_min_ps', 'd2s_mean_ps', 'd2s_std_ps',
       'd2s_max_ps', 'bi_min_pi_ms',
       'bi_mean_pi_ms', 'bi_std_pi_ms',
       'bi_max_pi_ms', 's2d_min_pi_ms',
       's2d_mean_pi_ms', 's2d_std_pi_ms', 's2d_max_pi_ms',
       'd2s_min_pi_ms', 'd2s_mean_pi_ms', 'd2s_std_pi_ms',
       'd2s_max_pi_ms', 'bi_syn',
       'bi_cwr', 'bi_ece',
       'bi_urg', 'bi_ack',
       'bi_psh', 'bi_rst',
       'bi_fin', 's2d_syn',
       's2d_cwr', 's2d_ece', 's2d_urg',
       's2d_ack', 's2d_psh', 's2d_rst',
       's2d_fin', 'd2s_syn', 'd2s_cwr',
       'd2s_ece', 'd2s_urg', 'd2s_ack',
       'd2s_psh', 'd2s_rst', 'd2s_fin',
       'app_name', 'app_cat', 'application_is_guessed',
       'req_server_name', 'client_fingerprint', 'server_fingerprint',
       'user_agent', 'content_type', 'device', 'label']

df = pd.read_csv(open(source,'r'),delimiter=',',header=None,names=cname)

df=df.drop(columns=["id","expiration_id","src_ip","src_mac","src_oui","dst_ip","dst_mac","dst_oui","application_is_guessed","bidirectional_first_seen_ms","bidirectional_last_seen_ms","src2dst_first_seen_ms","src2dst_last_seen_ms","dst2src_first_seen_ms","dst2src_last_seen_ms","device","label"])

df=df.round(decimals=2)
print("start tagging...")
df1=df.astype(str).apply(lambda x : x.name+':'+x)
df1.to_csv(outputPath, index=False, sep=' ',header=False)
print("Done.")