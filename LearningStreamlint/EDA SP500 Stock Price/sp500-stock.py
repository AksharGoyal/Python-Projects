from importlib_metadata import unique_everseen
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import yfinance as yf 

st.title('S&P 500 App')
st.markdown("""
            This app retrieves the list of the **S&P 500** from Wikipedia.
            * **Python libraries:** base64, pandas, streamlit, matplotlib
            * **Data sources:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
            """)

st.sidebar.header('User Input Features')

@st.cache # Accessing data from temporary location makes the app run faster
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies" #scrap data
    html = pd.read_html(url, header = 0) # Get the dataframe
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# for sidebar - sector selection
unique_sorted_sector = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector',unique_sorted_sector,\
    unique_sorted_sector)
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)] # Filetering the data

# Presenting the dataframe
st.header('Display Companies in Selected Sector')
st.write('Data Dimention: '+str(df_selected_sector.shape[0])+' rows and ' + \
    str(df_selected_sector.shape[1]) + "columns.")
st.dataframe(df_selected_sector)

# Downloading the data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# download the S&P Stock Price data
data = yf.download(tickers=list(df_selected_sector[:10].Symbol),
                   period="ytd", interval='1d', group_by='ticker',
                   auto_adjust=True, prepost = True, threads = True,
                   proxy = None)

def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index 
    plt.figure(figsize=(4,4))
    plt.fill_between(df.Date, df.Close, color='green', alpha=0.3)
    plt.plot(df.Date, df.Close, color='green', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date', fontweight='bold')
    plt.ylabel('Closing Price', fontweight='bold')
    return st.pyplot(plt)

num_company = st.sidebar.slider("Number of companies",1,7)

if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in df_selected_sector.Symbol[:num_company]:
        price_plot(i)