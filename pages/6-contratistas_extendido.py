import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
from streamlit_extras.switch_page_button import switch_page

df_file = "data/contractor_ext_companies_2021.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    df = df.dropna()
    # Filtramos las filas con importe cero
    df = df[df['import_adjudicacio_iva'] > 0]
    return df

contractors_ext_df = load_data(df_file)

st.title("Analisis extendido de contratistas del Ayuntamiento de Barcelona")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

st.write("En esta página vamos a poder explorar en más detallos los datos de los contratistas del Ayuntamiento de Barcelona en 2021.")

# Dibujamos un treemap con los datos de los contratistas extendidos
st.plotly_chart(px.treemap(contractors_ext_df, path=['tipus_contractes','nom_adjudicatari'], values='import_adjudicacio_iva', color='import_adjudicacio_iva', color_continuous_scale='RdBu', title='Analisis extendido de los contratistas por tipo de contrato e importe total'))