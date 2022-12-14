import yfinance as yf
import pandas as pd
import datetime 

import os
import json
from src.config import ticker

def write_file(target_path: str, target_file: str, data):
    # if directory doesn't exist, create it
    full_dir = os.path.join(target_path, target_file)

    # if directory doesn't exist, create it
    full_dir = os.path.join(target_path, target_file)
    #print("full path")
    #print(full_dir)

    if not os.path.exists(full_dir):
        data.to_csv(full_dir, index = False)
        
    else:
        data_ = pd.read_csv(full_dir)
        data_ = pd.concat([data_,data])
        data_.to_csv(full_dir, index = False)

def get_data(ticker: str, root_dir: str, **context):
    df_final = pd.DataFrame()
    #for tick in ticker:
    df = yf.download(ticker ,period='ytd')#start = start, end = end )
    df['ticker'] = ticker
    df_final = pd.concat([df_final,df])
    df_final.reset_index(inplace = True)
        
    #df_json = df_final.reset_index(drop=True).to_json()
    #print(df_json)
    write_file(os.path.join(root_dir, "tmp"), "stocks_data.csv", df_final)


