from sqlalchemy import create_engine, Column, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def create_table(conn_url, table_name):
    engine = create_engine(conn_url, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    # Create table class that will inherit from Base class
    class stocks(Base):
        __tablename__ = table_name
        #id = Column(int, primary_key = True)
        date = Column(Date , primary_key=True)        
        open = Column(Float)
        high = Column(Float)
        low = Column(Float)
        close = Column(Float)
        adj_close = Column(Float)
        volume = Column(Float)
        ticker = Column(String(5)) #, primary_key=True)

        def __init__(
            self, ticker, date, open, high, low, close, adj_close,volume
        ):
            self.ticker = ticker
            self.date = date
            self.open = open
            self.high = high
            self.low = low
            self.close = close
            self.adj_close = adj_close
            self.volume = volume
    # creates table into database if not exists
    Base.metadata.create_all(engine, checkfirst=True)
