import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
from streamlit_extras.switch_page_button import switch_page

df_file = "data/yearly_report_bcn_2021.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

df = load_data(df_file)

st.title("Procedimientos y tipos de procedimientos de contratos públicos")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")