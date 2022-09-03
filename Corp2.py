#! /bin/env python
from timeit import timeit
import pandas as pd
from pathlib import Path
from datetime import datetime

starttime=datetime.now()
paths = [str(x) for x in Path("/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/nfstream/split/").glob("**/*.csv")]

#source = "/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/nfstream/split/output_done_8.csv"
outputPath = "/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/nfstream/json/"

devicelist = pd.read_csv("/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/unsw_devicelist.csv", sep=',')
device_dict = dict(devicelist.drop(columns=['eth.src', 'Connection','Label']).values)



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

i=1
for y in paths:
       df_ = pd.read_csv(open(y,'r'),delimiter=',',header=None,names=cname)
       df_['category']= df_['device'].map(device_dict)
       df = df_.drop(columns=[
              "id","expiration_id","src_ip","src_mac","src_oui","dst_ip",
              "dst_mac","dst_oui","application_is_guessed","bidirectional_first_seen_ms",
              "bidirectional_last_seen_ms","src2dst_first_seen_ms","src2dst_last_seen_ms",
              "dst2src_first_seen_ms","dst2src_last_seen_ms","user_agent","device","label"
              ]).round(decimals=2)



       print("start tagging...",y)
       df = df.loc[:, df.columns !='category'].astype(str).apply(lambda x : x.name+':'+x)
       
       df1=pd.DataFrame()
       df1['text']=df['sp']+' '+df['dp']+' '+df['ptcl']+' '+df['ipv']+' '+df['vln']+' '+df['tnnl']+' '+df['bi_dur']+' '+df['bi_pkt']+' '+df['bi_byte']+' '+df['s2d_dur']+' '+df['s2d']+' '+df['s2d_byte']+' '+df['d2s_dur']+' '+df['d2s']+' '+df['d2s_byte']+' '+df['bi_min_ps']+' '+df['bi_mean_ps']+' '+df['bi_std_ps']+' '+df['bi_max_ps']+' '+df['s2d_min_ps']+' '+df['s2d_mean_ps']+' '+df['s2d_std_ps']+' '+df['s2d_max_ps']+' '+df['d2s_min_ps']+' '+df['d2s_mean_ps']+' '+df['d2s_std_ps']+' '+df['d2s_max_ps']+' '+df['bi_min_pi_ms']+' '+df['bi_mean_pi_ms']+' '+df['bi_std_pi_ms']+' '+df['bi_max_pi_ms']+' '+df['s2d_min_pi_ms']+' '+df['s2d_mean_pi_ms']+' '+df['s2d_std_pi_ms']+' '+df['s2d_max_pi_ms']+' '+df['d2s_min_pi_ms']+' '+df['d2s_mean_pi_ms']+' '+df['d2s_std_pi_ms']+' '+df['d2s_max_pi_ms']+' '+df['bi_syn']+' '+df['bi_cwr']+' '+df['bi_ece']+' '+df['bi_urg']+' '+df['bi_ack']+' '+df['bi_psh']+' '+df['bi_rst']+' '+df['bi_fin']+' '+df['s2d_syn']+' '+df['s2d_cwr']+' '+df['s2d_ece']+' '+df['s2d_urg']+' '+df['s2d_ack']+' '+df['s2d_psh']+' '+df['s2d_rst']+' '+df['s2d_fin']+' '+df['d2s_syn']+' '+df['d2s_cwr']+' '+df['d2s_ece']+' '+df['d2s_urg']+' '+df['d2s_ack']+' '+df['d2s_psh']+' '+df['d2s_rst']+' '+df['d2s_fin']+' '+df['app_name']+' '+df['app_cat']+' '+df['req_server_name']+' '+df['client_fingerprint']+' '+df['server_fingerprint']+' '+df['content_type']
       
       df1['label']=df_['category']

       output=outputPath+"unsw_corpus_"+str(i)+".json.gz"
       df1.to_json(output,orient='records',lines=True,compression='gzip')

       print("Done: ",y)
       i=i+1
print("Conversion Complete. Time:",datetime.now()-starttime)