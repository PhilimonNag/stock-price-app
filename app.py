import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write(
    """
# Stock Price App
"""
)
data_options = st.selectbox('Select Data', ['GOOGLE','MICROSOFT','APPLE'])
actual_stock_of='GOOGL'
if data_options == 'GOOGLE':
    actual_stock_of='GOOGL'
elif data_options == 'MICROSOFT':
    actual_stock_of='MSFT'
elif data_options == 'APPLE':
    actual_stock_of='AAPL'       
st.write(
    f'''
shown are stock **closing price** and **volume** of {data_options}!
'''
)
tickerSymbol=actual_stock_of
tickerData=yf.Ticker(tickerSymbol)
start_date = st.date_input('Start Date', datetime.date(2010, 1, 1))
end_date=st.date_input('End Date', datetime.date(2020, 1, 1))
tickerDf=tickerData.history(period='id',start=start_date,end=end_date)
st.write('## Closing Price')
st.line_chart(tickerDf.Close)
st.write('## volume')
st.line_chart(tickerDf.Volume)