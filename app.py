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

def final_investment_value(initial_investment: float|int, historical_return: float):
    return initial_investment * (1 + historical_return)

###
# streamlit code start here
###

# apa itu historical return
# formula kalkulasi
# contoh perusahaan dan info
# info singkat return dalam bentuk grafik
# grafik historical return
# contoh nilai kembalian untuk 5 tahun
# kesimpulan

# Header
st.header("Kalkulasi *Historical Return* Pada Saham Perusahaan")


# Apa itu Historical Return
st.subheader("Apa itu *Historical Return*")

"""
*Historical return* adalah nilai yang dapat digunakan untuk mengukur performa dari sebuah investasi. 
Analis/investor menggunakan *historical return* untuk mencoba memprediksi *return* di masa depan 
atau memperkirakan bagaimana produk investasi akan bereaksi pada suatu kejadian. Investasi 
yang dapat dikalkulasikan *historical return*-nya:
- Saham
- Reksa Dana
- ETF
- Index
- Komoditas

Namun, investor perlu berhati hati dalam menggunakan *historical return* 
karena nilai pada masa lampau belum tentu dapat memprediksi masa depan bahkan
jika kondisi yang sama terulang. Walaupun begitu, informasi ini adalah salah
informasi yang berguna sebagai salah satu komponen dari analisa komprehensif investor/analis
"""

# Rumus Historical Return
st.subheader("Rumus *Historical Return*")

"""
*Historical return* didapatkan dari kalkulasi data dari masa lampau.
untuk kalkulasi *historical return* dapat menggunakan rumus ini

$$
\\text{historical return} = \\frac{\\text{harga investasi akhir} - \\text{harga investasi awal}}{\\text{harga investasi awal}}
$$

Harga investasi akhir adalah harga investasi pada periode waktu akhir yang dipilih dan 
harga investasi awal adalah harga investasi yang dipilih pada periode waktu awal. Jika 
investasi yang dipilih adalah saham, harga saham dipilih
adalah harga *adjusted close* yaitu harga saham yang sudah dikalkulasikan berdasarkan *stock split*
dan dividen
"""

# Data Perusahaan
st.subheader("Data Perusahaan")


"""
Sebagai demonstrasi, 6 perusahaan dipilih untuk mengkalkulasi dan membandingkan nilai *historical return*-nya.
Berikut profil singkat perusahaan tersebut:

- **Apple Inc.**

  perusahaan teknologi multinasional amerika yang menjual alat elektronik konsumen dan 
  perangkat lunak seperti iPhone, iPad, Mac, Apple Watch, Apple TV, iTunes, iCloud, Apple Music 

- **Amazon**

  perusahaan multinasiona amerika dengan produk e-commerce, komputasi awan,
  streaming konten digital dan kecerdasan buatan

- **Google**
  
  perusahaan multinasional amerika yang bergeriak di bidang mesin pencari,
  kecerdasan buatan, iklan online, perangkat lunak, komputasi awan

- **Meta**

  perusahaan multinasional amerika yang mengoperasikan 
  whatsapp, facebook, instagram. Meta juga bergerak di virtual reality
  setelah membeli perusahaan Oculus (sekarang reality labs)

- **Nvidia**

  perusahaan multinasional amerika yang bergerak di bidang GPU, antaruka
  program untuk *data science* dan *High performance computing* dan supplier
  hardware dan software kecerdasan buatan

- **Microsoft**

  perusahaan multinasional amerika yang terkenal dengan sistem operasi windows dan
  perangkat lunak sepert Microsoft 365 dan edge browser

  
ada 3 alasan kenapa perusahaan ini dipilih dan periodenya 5 tahun dari 2024:
1. 6 perusahaan ini adalah perusahaan teknologi. Dengan AI menjadi trend pada
masa ini (tahun 2024), maka perusahaan ini adalah pilihan yang menarik bagaimana
harga saham mereka bereaksi dengan AI. 6 perusahaan ini menggunakan atau bergerak
dalam bidang AI
2. Walaupun ada perusahaan lain yang juga bergerak dan menggunakan AI. Jumlah
perusahaan yang dianalisa dibatasi menjadi 6 supaya tidak membingungkan
3. Data ini diambil dari API *free tier* Alpha Vantage. Ada batasan dalam menggunakan
*free tier* sehingga tidak bisa mengambil data terlalu banyak
"""

# Analisa
st.subheader("Analisa")

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
    x="Date",
    y="Adjusted Close",
    color=alt.Color('Stocks')
).properties(
    width=704
)

adjusted_close_chart = adjusted_close_chart.configure_axisX(labelAngle=0)

"""
Sebelum kalkulasi nilai historical return, berikut informasi harga 
*adjusted close* perusahaan selama 5 tahun mulai dari 2019
"""

st.altair_chart(adjusted_close_chart)

"""
Sumbu x menampilkan tanggal dan sumbu y menampilkan harga *adjusted close*
berdasarkan tanggal.
"""

historical_return_apple = calculate_historical_return(closing_prices['apple'].iloc[0], closing_prices['apple'].iloc[-1])
historical_return_amazon = calculate_historical_return(closing_prices['amazon'].iloc[0], closing_prices['amazon'].iloc[-1])
historical_return_google = calculate_historical_return(closing_prices['google'].iloc[0], closing_prices['google'].iloc[-1])
historical_return_meta = calculate_historical_return(closing_prices['meta'].iloc[0], closing_prices['meta'].iloc[-1])
historical_return_nvidia = calculate_historical_return(closing_prices['nvidia'].iloc[0], closing_prices['nvidia'].iloc[-1])
historical_return_microsoft = calculate_historical_return(closing_prices['microsoft'].iloc[0], closing_prices['microsoft'].iloc[-1])

hist_ret_raw_table = [
    ('apple', historical_return_apple),
    ('amazon', historical_return_amazon),
    ('google', historical_return_google),
    ('meta', historical_return_meta),
    ('nvidia', historical_return_nvidia),
    ('microsoft', historical_return_microsoft)
]

hist_ret_dataframe = pd.DataFrame(data=hist_ret_raw_table, columns=['Stock', 'Historical Return'])

hist_ret_bar = alt.Chart(hist_ret_dataframe).mark_bar().encode(
    x='Stock',
    y='Historical Return',
    color=alt.Color("Stock")
).properties(
    width=704
)

hist_ret_text = hist_ret_bar.mark_text(
    align="center",
    dy=-5
).encode(text="Historical Return")

hist_res_chart = hist_ret_text + hist_ret_bar

hist_res_chart = hist_res_chart.configure_axisX(labelAngle=0)

hist_res_chart = hist_res_chart.configure_range(
    category={'scheme': 'dark2'}
)

"""
Setelah itu kita kalkulasikan nilai historical return dan menampilkannya
dalam bentuk diagram batang
"""

st.altair_chart(hist_res_chart)

"""
Sumbu x menampilkan nama perusahaan dan sumbu y menampilkan nilai 
*historical return* dari perusahaan
"""

"""
untuk menggunakan nilai dari historical return, misal ingin melakukan
investasi. Nilai investasi akhir didapatkan dengan menggunakan rumus
berikut:
$$
\\text{Nilai Investasi Akhir} = \\text{Nilai Investasi Awal} \\times (1 + \\text{Historical Return})
$$
dengan asumsi investasi dilakukan satu kali pada awal tanggal, tidak
menghitung inflasi dan pajak. Berikut contoh penggunaanya
"""

initial_investment = st.number_input('Nilai Investasi Awal:', value=1000)

final_investment_apple = final_investment_value(initial_investment, historical_return_apple)
numerized_apple = numerize(final_investment_apple)

final_investment_amazon = final_investment_value(initial_investment, historical_return_amazon)
numerized_amazon = numerize(final_investment_amazon)

final_investment_google = final_investment_value(initial_investment, historical_return_google)
numerized_google = numerize(final_investment_google)

final_investment_meta = final_investment_value(initial_investment, historical_return_meta)
numerized_meta = numerize(final_investment_meta)

final_investment_nvidia = final_investment_value(initial_investment, historical_return_nvidia)
numerized_nvidia = numerize(final_investment_nvidia)

final_investment_microsoft = final_investment_value(initial_investment, historical_return_microsoft)
numerized_microsoft = numerize(final_investment_microsoft)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label='Apple', value=numerized_apple)

with col2:
    st.metric(label='Amazon', value=numerized_amazon)

with col3:
    st.metric(label='Google', value=numerized_google)


col4, col5, col6 = st.columns(3)

with col4:
    st.metric(label='Meta', value=numerized_meta)

with col5:
    st.metric(label='Nvidia', value=numerized_nvidia)

with col6:
    st.metric(label='Microsoft', value=numerized_microsoft)

# Kesimpulan
st.subheader("Kesimpulan")

"""
*Historical value* adalah informasi cepat yang investor/
analis bisa dapatkan pada investasi mereka. Walaupun memiliki
banyak kekurangan, informasi ini dapat dipakai sebagai bagian dari
analisis komprehensif atau sebagai filter untuk mencari investasi
yang sesuai dengan kebutuhan investor/analis
"""