
import streamlit as st 
import pandas as pd 
voc=pd.need_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTCnNUKxiK_6WUL2l3_S2MhTWB744cSf9tXzOg1edajF2pjDyeomM6Kz_W9pR6YCx1MgLjVNt_znLqV/pub?output=csv") 
st.dataframe(voc)
