import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

def get_appl_monthly_stock_data():
    stocks = pd.read_csv('aapl/static_3_years_monthly_stock_adjusted.csv')
    # stocks = stocks.set_index(pd.DatetimeIndex(stocks['date'].values))
    # stocks.drop(['date'], inplace=True)
    return stocks

def get_sp500_monthly_stock_data():
    stocks = pd.read_csv('static_3_years_sp500_monthly.csv')
    return stocks

stocks = get_appl_monthly_stock_data()

stocks_adjusted_close_chart = alt.Chart(stocks).mark_line().encode(
    x='date',
    y='adjusted close'
).configure_axisX(labelAngle=0)

st.altair_chart(stocks_adjusted_close_chart)