import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
from streamlit_extras.switch_page_button import switch_page

df_file = "data/contractor_companies_2021.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

contractors = load_data(df_file)

st.title("Contratistas del Ayuntamiento de Barcelona")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

st.write("En esta página vamos a ver los datos de los contratistas del Ayuntamiento de Barcelona en 2021.")
st.write("En esta visualización sólo vamos a incluir aquellos contratistas que son personas jurídicas. Para evitar la compartición de los datos personales, hemos ommitido aquellos datos que pudieran identificar a una persona física.")

st.metric("Número total de entidades contratistas", df["contractor_name"].nunique())

st.subheader('¿Qué contratistas han conseguido mayores importes de contratos?')
st.write('A continuación se muestran los 10 contratistas que han conseguido mayores importes de contratos en 2021.')

# Extraemos el top 10 de contratistas por 'total_import_iva_inclos'
contractors_top10 = contractors.sort_values(by='total_import_iva_inclos', ascending=False).head(10)

# Visualizamos los top 10 de contratistas en un gráfico de barras horizontal, mostrando el nombre del contratista y el importe total de contratos. Usamos plotly express para crear el gráfico.
st.plotly_chart(px.bar(contractors_top10, x='total_import_iva_inclos', y='contractor_name', orientation='h', title='Top 10 de contratistas por importe total de contratos'))

st.subheader('¿Qué contratistas han conseguido más contratos?')
