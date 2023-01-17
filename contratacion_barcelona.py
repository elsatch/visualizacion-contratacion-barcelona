import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.title("Visualización Contratación en Barcelona (2017-2022")

minor_contracts = "minor_contracts_2017_2022.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file, index_col=0)
    return df

minor_contracts_df = load_data(minor_contracts)

st.write('Esta aplicación visualiza información sobre contratación en Barcelona, a partir de los conjuntos de datos abiertos municipales. En concreto, vamos a explorar los datos correspondientes a los años 2017-2022.')
st.write('Nótese que debido a la fecha en la que se han generado estas visualizaciones, todavía no se han publicado los datos del último triemstre de 2022.')

st.subheader("Contratos agrupados por órgano gestor")

st.write('En primer lugar, vamos a ver la distribución de los contratos por órgano gestor. Para ello, vamos a agrupar los contratos por órgano gestor y vamos a mostrar el número de contratos y el importe total de cada uno de ellos.')
st.write(minor_contracts_df.groupby('organo_gestor').agg({'importe': 'sum', 'id': 'count'}).rename(columns={'id': 'contratos'}).sort_values('contratos', ascending=False))

