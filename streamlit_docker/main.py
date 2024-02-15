import streamlit as st

st.title("Welcome to Streamlit App")
conn = st.connection("snowflake")

df = conn.query("SELECT * FROM FLIGHTS;")

for row in df.itertuples():
    st.write(f"{row.ROUTEID} has the fare :{row.FARE}:")