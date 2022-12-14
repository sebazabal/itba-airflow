from sqlalchemy import create_engine, text
import pandas as pd



class PostgresCli:
    def __init__(self, conn_url):
        self.conn_url = conn_url
        self.engine = create_engine(self.conn_url, echo=False)



    def get_all_data(self):
        q = text("SELECT date,ticker,open,close,high,low,volume,adj_close from stocks_info_ytd")
        result = self.engine.execute(q)
        df_from_records = pd.DataFrame.from_records(
            result, columns=["date", "ticker", "open", "close", "high", "low", "volume", "adj_close"]
        )
        return df_from_records