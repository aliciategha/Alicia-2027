
import streamlit as st 
import pandas as pd 
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTCnNUKxiK_6WUL2l3_S2MhTWB744cSf9tXzOg1edajF2pjDyeomM6Kz_W9pR6YCx1MgLjVNt_znLqV/pub?output=csv') 
l=voc.shape[0]
i=np.random.choice(range(l))
indices=np.ramdom.choice(l, site=4, replace=false)
st.write(indices)
word_fr=voc["Définition"].values[i]
word_pin=["Pinyin"].values[i]
word_chi=["Hanzi"].values[i]
st.write(word_fr+" "+word_pin+" "+word_chi)
st.button("refresh")
