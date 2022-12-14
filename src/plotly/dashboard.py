
from dash import html 
from dash import dcc
from dash import Dash
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output  
import pandas as pd
from psql_cli import PostgresCli
import os


psql_conn_client = PostgresCli("postgresql+psycopg2://airflow:airflow@postgres:5432/stocks_data")

#df = psql_conn_client.get_all_data()
df = pd.read_csv("stocks_data.csv")

df = df[["Date", "ticker","Close"]]
#df.set_index("Date")
#print(df)

#y = df['Close']
#print(y)
app = Dash()


app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Dashboard - TP Itba - Airflow', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'S&P', 'value':'SPY' },
            {'label': 'Apple', 'value':'AAPL'},
            {'label': 'Microosoft', 'value':'MSFT'},
            ],
        value = 'MSFT'),
        dcc.Graph(id = 'bar_plot')
    ])
    
    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    df_ = df[df["ticker"]==dropdown_value]
    fig = go.Figure([go.Scatter(x = df_['Date'], y = df_['Close'],\
                     line = dict(color = 'blue', width = 1))
                     ])
    
    fig.update_layout(title = 'Stock prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  



if __name__ == '__main__': 
    app.run_server()



#https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4    