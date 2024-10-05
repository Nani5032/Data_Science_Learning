# run the command -> streamlit run app.py
import streamlit as st
import pandas as pd
import time
# ************** text utility **************
st.title('startup-dashboard')
st.header('i am learning streamlit')
st.subheader('and i am loving it ')

st.write('this is a normal text')

st.markdown("""
### My favorite movies
- Athadu
- Leader
- Social Network
""")

st.code("""
def foo(input):
        return input**2
x = foo(2)
        """)

st.latex("x^2 + y^2 + 2 = 0")


# ************** Display Elements **************

# dataframes

df = pd.DataFrame({
    'name': ['nitish', 'ankit', 'rahul'],
    'marks': [50,60,70],
    'package': [10,12,14]
})

st.dataframe(df)

# metrics

st.metric('Revenue', 'Rs 3L', '3%')

# JSON

st.json({
    'name': ['nitish', 'ankit', 'rahul'],
    'marks': [50,60,70],
    'package': [10,12,14]
})

# ************** Displaying Media **************

# image

st.image('stew.jpg')

# video

st.video('pre_wedding.mp4')

# ************** Creating Layouts **************

# sidebar
st.sidebar.title('sidebar ka title')

# columns
col1 , col2 = st.columns(2)
with col1:
    st.image('stew.jpg')

with col2:
    st.image('stew.jpg')


# ************** Showing Status **************
# progress bar
bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.01)
    bar.progress(i)
# error message -> success

st.error('this is error')
st.warning('this is warning')
st.info('this is info')
st.success('this is success')

# ************** Taking user input **************
# text input -> number input -> date input

text = st.text_input('enter text')
number = st.number_input('enter number')
st.date_input('enter date')

# button -> baloons
email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['male','female','others'])

btn = st.button('Login Karo')

# if the button is clicked
if btn:
    if email == 'hi@gmail.com' and password == '1234':
        st.success('Login successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')


# dropdown
# file uploader
file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())