from sqlalchemy import create_engine
import requests
import pytest
from src.config import CONN_URL


#testeo data conection to db
@pytest.mark.parametrize("conn_url", [CONN_URL])
def test_db(conn_url):
    engine = create_engine(conn_url, echo=False)
    response_db = engine == 200
    return response_db


#testeo api endpoint
@pytest.mark.parametrize("ticker", [("SPY"), ("AAPL"), ("MSFT")])
def test_api(ticker):
    url = f"https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticker}?modules=financialData"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.content != None

#https://query1.finance.yahoo.com/v10/finance/quoteSummary/aapl?modules=financialData