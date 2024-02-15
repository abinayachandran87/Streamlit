# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session


# Write directly to the app
st.title("Weekly sales data")


# Get the current credentials
session = get_active_session()

selection = st.selectbox('Select the year', options=['1993', '1994', '1997', '1998'])

year = int(selection)

sql = f"select WEEK_YEAR, round(WEEKLY_SALES,0) as WEEKLY_SALES from my_db.public.weekly_sales where year={year} order by week_year asc limit 5"
data = session.sql(sql).collect()


st.bar_chart(data, x='WEEK_YEAR', y='WEEKLY_SALES')
