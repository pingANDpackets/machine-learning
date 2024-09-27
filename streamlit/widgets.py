import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age:" , 0, 100, 25)

st.write(f"your age is ", age )

## select box 
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")


# create the df
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

#display df
st.write("Here is the dataframe")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)




