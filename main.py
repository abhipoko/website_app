import pandas
import streamlit as st
import pandas as pd

data_table=pandas.read_csv("data.csv")
st.title("This is company website")

st.text('''
Hey guys this is a company we=bsite where people write all kind of hypothetical things that they 
want to do or achieve in reality they all are bums and just waiting for some miracle to happen a
which doesnt usually happen and unfortunately they fail but i am not that this is my company website and i 
am going to make it awesome because i am the real winner''')

c1,c2,c3 = st.columns(3)

with c1:
    for index, row  in data_table[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with c2:
    for index, row  in data_table[5:9].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with c3:
    for index, row  in data_table[10:12].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

