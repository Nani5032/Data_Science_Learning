import streamlit as st
import pandas as pd

st.title('Hi')
df = pd.read_csv('startup_funding.csv')
df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find startup details')
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('Select Investor', sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.sidebar.button('Find Investor details')
    st.title('Investor Analysis')