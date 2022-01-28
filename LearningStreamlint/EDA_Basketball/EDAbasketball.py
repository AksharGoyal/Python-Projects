import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import base64

st.title('NBA Player Stats Explorer') 

st.markdown("""
            This app performs simple webscrapping of NBA player stats data
            * **Python libraries:** base64, pandas, streamlit   
            * **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/)
            """)
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(range(2019,1949,-1))) # A dropdown menu of descending years

# We now begin web scrapping
@st.cache # Accessing data from temporary location makes the app run faster
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0) # Get the data
    df = html[0]
    # print(html)
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    # Converting some columns to float types else they will cause error
    raw['FG%'] = raw['FG%'].astype(float)
    raw['3P%'] = raw['3P%'].astype(float)
    raw['2P%'] = raw['2P%'].astype(float)
    raw['eFG%'] = raw['eFG%'].astype(float)
    raw['FT%'] = raw['FT%'].astype(float)
    playerstats = raw.drop(['Rk'], axis = 1)
    
    return playerstats
playerstats = load_data(selected_year)

# Sidebar team selection
sorted_unique_team = sorted(playerstats.Tm.unique()) # Get the unique teams
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar position selection
# print(type(playerstats.Pos.unique()))
unique_pos = playerstats.Pos.unique().tolist()
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
# print(df_selected_team.dtypes)
st.dataframe(df_selected_team)

def filedownload(df):
    csv = df.to_csv(index=False) # Get the CSV file
    b64 = base64.b64encode(csv.encode()).decode() # converting it to bytes
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv', index=False)
    df = pd.read_csv('output.csv')
    # We read the file again because the original file doesn't show correlation between all the columns
    corr = df.corr() # Generate a correlation
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True # Upper triangle is now blank
    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(5,5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True) # generate the correlation visualization
    st.pyplot(fig)
    st.write("We observe that column FG shows high correlation with many attributes.")
    