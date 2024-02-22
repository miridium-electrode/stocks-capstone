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

apple = get_appl_monthly_stock_data()

sp500 = get_sp500_monthly_stock_data()

return_percentage_apple = (apple['adjusted close'].iloc[-1] - apple['adjusted close'].iloc[0]) / apple['adjusted close'].iloc[0]
return_percentage_sp500 = (sp500['Adj Close'].iloc[-1] - sp500['Adj Close'].iloc[0]) / sp500['Adj Close'].iloc[0]



# streamlit code start here


st.title("Perbandingan Return Historical Saham Apple dan S&P 500 pada Tahun 2021 - 2024")

st.header("Pendahuluan")

st.write("""
    Return historical adalah nilai return dari sekuritas atau index pada masa lampau. Analisa
    return historical adalah salah satu data yang dapat digunakan untuk memprediksi performa sekuritas
    pada masa depan. Pada laporan ini, terdapat 1 sekuritas dan 1 index yang akan dibandingkan nilai
    return historikalnya, apple dan s&p 500
""")


apple_adjusted_close_chart = alt.Chart(apple).mark_line().encode(
    x='date',
    y='adjusted close',
).configure_axisX(labelAngle=0)

st.altair_chart(apple_adjusted_close_chart)

sp500_adjusted_close_chart = alt.Chart(sp500).mark_line().encode(
    x='Date',
    y='Adj Close'
).configure_axisX(labelAngle=0)

st.altair_chart(sp500_adjusted_close_chart)

nilai_investasi = st.number_input('Nilai investasi awal', value=1000)
st.write('jumlah uang terakhir apple setelah selesai dalam $', (nilai_investasi + (nilai_investasi * return_percentage_apple)))
st.write('jumlah uang terakhir s&p 500 setelah selesai dalam $', (nilai_investasi + (nilai_investasi * return_percentage_sp500)))