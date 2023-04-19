import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import mysql.connector
import json

st.title('phonepe')
#years=st.selectbox('Select years', [2018,2019])

#st.button('Click me')

qarter=st.selectbox('select quarter', ['trans_2018_1', 'trans_2018_2','trans_2018_3','trans_2018_4','trans_2019_1','trans_2019_2','trans_2019_3','trans_2019_4'])

st.button('Click')

datas=st.selectbox('Select', ['count', 'amount'])

st.button('ok')


engine = create_engine("mysql+pymysql://root:Ranjith98@localhost:3306/phonepe",pool_size=1000, max_overflow=2000)

#query=f'select * from {years}'

from sqlalchemy import create_engine,text

with engine.begin() as conn:
    query = text(f"SELECT * FROM {qarter}");
    df = pd.read_sql_query(query,conn)
   # result =  con.execute(text(query))




fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color=datas,
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()
