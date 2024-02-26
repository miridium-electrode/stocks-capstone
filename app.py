import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from numerize.numerize import numerize

apple = pd.read_csv('aapl/price_data.csv')

amazon = pd.read_csv('amzn/price_data.csv')

google = pd.read_csv('googl/price_data.csv')

meta = pd.read_csv('meta/price_data.csv')

microsoft = pd.read_csv('msft/price_data.csv')

nvidia = pd.read_csv('nvda/price_data.csv')

def calculate_historical_return(starting_price: float, ending_price: float):
    return (ending_price - starting_price) / starting_price

def final_investment_value(initial_investent: float|int, historical_return: float):
    return initial_investent * (1 + historical_return)

###
# streamlit code start here
###

# Header
st.header("Perbandingan *historical return* Saham Perusahaan dan Index")


# Pendahuluan
st.subheader("Pendahuluan")

"""
- *Historical return* adalah performa masa lampau dari sekuritas/index.
- *Historical return* digunakan sebagai salah satu data yang digunakan analis dan investor untuk 
memperkirakan return sekuritas/index pada masa depan. 
- Investor dapat memperkirakan *historical return*  dari investasi apapun, seperti: 
    - sekuritas
    - rumah
    - real estate
    - reksa dana
    - etf
    - komoditasi
      - emas
      - bahan pangan
      - minyak
      - listrik
      - air
"""

# Saham dan Index
st.subheader("Saham")

"""
Berikut adalah Saham yang dipilih untuk dianalisa *historical return*-nya
- apple
- amazon
- google
- meta
- nvidia
- microsoft
"""

closing_prices = pd.DataFrame({
    'date': apple['date'],
    'apple': apple['adjusted close'],
    'amazon': amazon['adjusted close'],
    'google': google['adjusted close'],
    'meta': meta['adjusted close'],
    'nvidia': nvidia['adjusted close'],
    'microsoft': microsoft['adjusted close']
})

melted = closing_prices.melt(id_vars='date', value_vars=['apple', 'amazon', 'google', 'meta', 'nvidia', 'microsoft'])

melted = melted.rename(
    columns={
        'date': 'Date',
        'value': 'Adjusted Close',
        'variable': 'Stocks'
    })

# https://altair-viz.github.io/gallery/line_chart_with_custom_legend.html
adjusted_close_chart = alt.Chart(melted).mark_line().encode(
    x='Date',
    y='Adjusted Close',
    color='Stocks'
).properties(
    width=704,
)

adjusted_close_chart = adjusted_close_chart.configure_axisX(labelAngle=0)

st.altair_chart(adjusted_close_chart)

roi_apple = calculate_historical_return(closing_prices['apple'].iloc[0], closing_prices['apple'].iloc[-1])
roi_amazon = calculate_historical_return(closing_prices['amazon'].iloc[0], closing_prices['amazon'].iloc[-1])
roi_google = calculate_historical_return(closing_prices['google'].iloc[0], closing_prices['google'].iloc[-1])
roi_meta = calculate_historical_return(closing_prices['meta'].iloc[0], closing_prices['meta'].iloc[-1])
roi_nvidia = calculate_historical_return(closing_prices['nvidia'].iloc[0], closing_prices['nvidia'].iloc[-1])
roi_microsoft = calculate_historical_return(closing_prices['microsoft'].iloc[0], closing_prices['microsoft'].iloc[-1])

roi_raw_table = [
    ('apple', roi_apple),
    ('amazon', roi_amazon),
    ('google', roi_google),
    ('meta', roi_meta),
    ('nvidia', roi_nvidia),
    ('microsoft', roi_microsoft)
]

roi_dataframe = pd.DataFrame(data=roi_raw_table, columns=['stock', 'roi'])

st.bar_chart(data=roi_dataframe, x='stock', y='roi')

# Analisa
st.subheader("Analisa")

initial_investment = st.number_input('Nilai investasi awal', value=1000)

final_investment_apple = final_investment_value(initial_investment, roi_apple)
numerized_apple = numerize(final_investment_apple)

st.metric(label='Apple', value=numerized_apple)

# Kesimpulan
st.subheader("Kesimpulan")




