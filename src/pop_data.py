import csv
import os
import json
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
import pandas as pd
from numpy import genfromtxt


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

def populate_table(table_name: str, root_dir: str, conn_url: str):
    
    
    engine = create_engine(conn_url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    meta = MetaData()
    meta.reflect(bind=engine)
    mytable = meta.tables[table_name]
    full_dir = os.path.join(root_dir, "tmp", "stocks_data.csv")
    csv_data = pd.read_csv(full_dir)
    csv_data=csv_data.values.tolist()
    conn=engine.connect()
    conn.execute(f"TRUNCATE TABLE {mytable}")
    conn.close()
    #conn.close()
    for row in csv_data:
        
        #Each element in the list is an attribute for the table class
        #Iterating through rows and inserting into table
        ins= mytable.insert().values(
        date = row[0],open =row[1], high =row[2], low =row[3],close = row[4], adj_close = row[5], volume = row[6], ticker = row[7])
        conn=engine.connect()
        try:
            conn.execute(ins)
        except:
            pass

    session.close()
    conn.close()



