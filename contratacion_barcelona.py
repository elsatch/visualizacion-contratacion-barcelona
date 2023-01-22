import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.title("Contratación en Barcelona (2017-2022")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

df_file = "data/yearly_report_bcn_2020_2021.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

df = load_data(df_file)

st.write('Esta aplicación visualiza información sobre contratación en Barcelona, a partir de los conjuntos de datos abiertos municipales. En concreto, vamos a explorar los datos correspondientes a los años 2017-2022.')
st.write('Nótese que debido a la fecha en la que se han generado estas visualizaciones, todavía no se han publicado los datos del último triemstre de 2022.')

st.subheader("Contratos anuales del Ayuntamiento de Barcelona")

st.write('En primer lugar, vamos a ver cuántos contratos se han realizado en Barcelona en los años 2020 y 2021')
#st.write(minor_contracts_df.groupby('organo_gestor').agg({'importe': 'sum', 'id': 'count'}).rename(columns={'id': 'contratos'}).sort_values('contratos', ascending=False))

st.write(df.head())

# Extract the number of contracts per year, adding the column 'Número' per year
contratos_2020 = df[df['año'] == 2020]['Número'].sum()
contratos_2021 = df[df['año'] == 2021]['Número'].sum()

st.write(contratos_2020)
st.write(contratos_2021)

col1, col2 = st.columns(2)
col1.metric(label="Num. Contratos 2021", value=contratos_2020, delta='4%')
col2.metric(label="Num. Contratos 2020", value=contratos_2021, delta='7$')

st.plotly_chart(px.histogram(df, x='año', title='Número de contratos por año'))