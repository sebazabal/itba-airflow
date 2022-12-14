import yfinance as yf
import pandas as pd
import datetime 

import os
import json
ticker = ["SPY","MSFT","AAPL"]
root_dir = os.getcwd()



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
        print(data_.head(2))
        data_ = pd.concat([data_,data])
        print(data_.head(3))
        data_.to_csv(full_dir, index = False)
        print(data_.head(4))



def get_data(ticker: str, root_dir: str, **context):
    #for tick in ticker:
    df = yf.download(ticker ,period='ytd')#start = start, end = end )
    df['ticker'] = ticker
    print(df.head(2))
    df = df.reset_index()
    print(df.head(5))
        
    #df_json = df_final.reset_index(drop=True).to_json()
    #print(df_json)
    write_file(os.path.join(root_dir, "testeo"), "stocks_data.csv", df)




for tick in ticker:
    get_data(tick, root_dir)

