# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:51:50 2022

@author: atipirneni
"""

import sys
sys.path.append('../')

import os
import pandas as pd
import re
import numpy as np
from logparser import Spell, Drain
from tqdm import tqdm
#from logdeep.dataset.session import sliding_window
import glob

########
# count anomaly
########
# count_anomaly(data_dir + log_file)
# sys.exit()

import glob

tqdm.pandas()
pd.options.mode.chained_assignment = None  # default='warn'
hresult_dict = {'0x00000000': 1,'0x800f080d':2,'0x800f0805':3, '0x80070490':4, '0x80004005':5, '0x80070001':6, '0x80071a2d':7, '0x80070216':8, '0x80070bc2':9, '0x800f0816':10, '0x800f0806':11, '0x800f0902':12, '0x80070002':13, '0x80070013':14}


# In the first column of the log, "-" indicates non-alert messages while others are alert messages.
def count_anomaly(log_path):
    total_size = 0
    normal_size = 0
    with open(log_path, errors='ignore') as f:
        for line in f:
            total_size += 1
            if line.split('')[0] == '-':
                normal_size += 1
    print("total size {}, abnormal size {}".format(total_size, total_size - normal_size))


def deeplog_file_generator(filename, df, features):
    with open(filename, 'w') as f:
        for _, row in df.iterrows():
            for val in zip(*row[features]):
                f.write(','.join([str(v) for v in val]) + ' ')
            f.write('\n')




def sample_raw_data(data_file, output_file, sample_window_size, sample_step_size):
    # sample 1M by sliding window, abnormal rate is over 2%
    sample_data = []
    labels = []
    idx = 0

    # spirit dataset can start from the 2Mth line, as there are many abnormal lines gathering in the first 2M
    with open(data_file, 'r', errors='ignore') as f:
        for line in f:
            labels.append(line.split()[0] != '-')
            sample_data.append(line)

            if len(labels) == sample_window_size:
                abnormal_rate = sum(np.array(labels)) / len(labels)
                print(f"{idx + 1} lines, abnormal rate {abnormal_rate}")
                break

            idx += 1
            if idx % sample_step_size == 0:
                print(f"Process {round(idx/sample_window_size * 100,4)} % raw data", end='\r')

    with open(output_file, "w") as f:
        f.writelines(sample_data)

    print("Sampling done")

def parse_log(input_dir, output_dir, log_file, parser_type):
    #log_format = '<Label> <Id> <Date> <Admin> <Month> <Day> <Time> <AdminAddr> <Content>'
    log_format = '<Date> <Time>, <Type>             <Admin>  <Content>'
    regex = [
        r'(0x)[0-9a-fA-F]+',  # hexadecimal
        r'\d+\.\d+\.\d+\.\d+',
        r'(?<=Warning: we failed to resolve data source name )[\w\s]+',
        r'\d+'
    ]
    keep_para = False
    if parser_type == "drain":
        # the hyper parameter is set according to http://jmzhu.logpai.com/pub/pjhe_icws2017.pdf
        st = 0.3  # Similarity threshold
        depth = 3  # Depth of all leaf nodes

        # Drain is modified
        parser = Drain.LogParser(log_format,
                                 indir=input_dir,
                                 outdir=output_dir,
                                 depth=depth,
                                 st=st,
                                 rex=regex,
                                 keep_para=keep_para, maxChild=1000)
        parser.parse(log_file)

    elif parser_type == "spell":
        tau = 0.35
        parser = Spell.LogParser(indir=data_dir,
                                 outdir=output_dir,
                                 log_format=log_format,
                                 tau=tau,
                                 rex=regex,
                                 keep_para=keep_para)
        parser.parse(log_file)
        
        
        ##File parser


def matchfunc(line):
    # Capture one-or-more characters of non-whitespace after the initial match
    match = re.search(r'HRESULT = (\S+)', line)

    # Did we find a match?
    if match:
        # Yes, process it
        weather = match.group(1)
        return(hresult_dict[weather])
    return(0)


def fileexport():
    a = glob.glob(output_dir +"/*_structured.csv") 
    file_list=[os.path.basename(list_item) for list_item in a]
    
    #print(file_list)
    
    
    ##################
    # Transformation #
    ##################
    for file in file_list:
        print("\nTransforming", file)
        df = pd.read_csv(f'{output_dir}{file}')
        df['Label'] = 0
    
        #df.loc[df['Content'].str.contains("HRESULT"), "Label"] = 1
        df['Label'] = df.apply(lambda row: matchfunc(row['Content']), axis = 1)
        df.to_excel(f'{output_dir}{file}_labeled.xlsx')  
        
    
    
    
    # csv files in the path
    file_list = glob.glob(output_dir + "*_labeled.xlsx")
     
    # list of excel files we want to merge.
    # pd.read_excel(file_path) reads the excel
    # data into pandas dataframe.
    excl_list = []
     
    for file in file_list:
        excl_list.append(pd.read_excel(file))
     
    # create a new dataframe to store the
    # merged excel file.
    excl_merged = pd.DataFrame()
     
    for excl_file in excl_list:
         
        # appends the data into the excl_merged
        # dataframe.
        excl_merged = excl_merged.append(
          excl_file, ignore_index=True)
     
    # exports the dataframe into excel file with
    # specified name.
    excl_merged.to_csv('total_output.csv', index=False)
    print("done!!")

if __name__ == "__main__":
    data_dir = os.path.expanduser("../dataset/Windows")
    output_dir = "../output/windows/"
    raw_log_file = "xaa.txt"
    sample_log_file = "xaa.txt"
    sample_window_size = 2*10**7
    sample_step_size = 10**4
    window_name = ''
    log_file = sample_log_file
    
    parser_type = 'drain'
    #mins
    window_size = 1
    step_size = 0.5
    train_ratio = 6000
    
    
    fileexport()