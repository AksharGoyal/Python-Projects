import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
         # My Stock Price App
         ### Also my first Streamlit app
         
         Shown are the stock's **closing price** and **volume** of Google
         
         """)

tickerSymbol = 'GOOGL'
# get data on the specificed ticker
tickerData = yf.Ticker(tickerSymbol)
# print(tickerData)
# get the historical prices
tickerDf = tickerData.history(period = '1d', start = "2012-1-01", end = "2020-1-01")
# print(tickerDf)
st.write("""
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)
st.write("""
         ## Volume Price
         """)
st.line_chart(tickerDf.Volume)