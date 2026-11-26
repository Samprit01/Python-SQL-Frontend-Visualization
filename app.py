import streamlit as st
from func import display_records,display_charts

st.set_page_config(page_title="App", layout="centered")

st.title("Student Marks Analyzer")

col1, col2 = st.columns(2)

with col1:
    btn1 = st.button("Show All Records", use_container_width=True)

with col2:
    btn2 = st.button("Show Students and Marks visualizer", use_container_width=True)

if btn1:
    df = display_records()
    st.dataframe(df, use_container_width=True,hide_index=True)

if btn2:
    summary = display_charts()
    st.pyplot(summary)