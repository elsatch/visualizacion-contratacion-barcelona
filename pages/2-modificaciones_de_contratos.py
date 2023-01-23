import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
from streamlit_extras.switch_page_button import switch_page

mc_file = "data/modified_contracts_2021.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

mc = load_data(mc_file)

st.title("Modificaciones de los contratos")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

st.write("En esta página vamos a ver las modificaciones de los contratos realizados por el Ayuntamiento de Barcelona en 2021.")
st.write("En el año 2021 el número de contratos que se han modificado es de:")

st.metric(label="Número de contratos modificados", value=len(mc.index))

st.subheader("¿Cuánto se ha modificado el presupuesto de los contratos modificados?")
st.write("Una de las cosas que se podría asumir es que todos los contratos modificados han incrementado su presupuesto con esta modificación, pero si nos fijamos en los datos, observaremos que esto no es siempre así.")

st.plotly_chart(px.histogram(mc, x="variaciò", title="Variación presupuesto de los contratos modificados"))

st.write('Si observamos esta gráfica vemos que la mayor parte de los contratos modificados no han variado su importe o lo han hecho mínimamente. En cuanto a los valores más elevados, vemos que hay más reducciones de precio que aumento de los mismos. Vamos a revisar los totales:')

col1, col2, col3 = st.columns(2)
# contratos que han reducido su importe (variaciò < 0)
col1.metric("Reducción de importe", mc[mc['variaciò'] < 0].count())
col2.metric("Sin cambio de importe", mc[mc['variaciò'] == 0].count())
col3.metric("Aumento de importe", mc[mc['variaciò'] > 0].count())