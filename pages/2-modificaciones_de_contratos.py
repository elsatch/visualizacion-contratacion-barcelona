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
st.metric(label="Suma de los imporrtes de los de contratos modificados", value=mc['import_modificacio_sense_iva'].sum())


st.subheader("¿Cuánto se ha modificado el presupuesto de los contratos modificados?")
st.write("Una de las cosas que se podría asumir es que todos los contratos modificados han incrementado su presupuesto con esta modificación, pero si nos fijamos en los datos, observaremos que esto no es siempre así.")

st.plotly_chart(px.histogram(mc, x="variaciò", title="Variación presupuesto de los contratos modificados"))

st.write('Si observamos esta gráfica vemos que la mayor parte de los contratos modificados no han variado su importe o lo han hecho mínimamente. En cuanto a los valores más elevados, vemos que hay más reducciones de precio que aumento de los mismos.')
st.write('Vamos a revisar los totales:')

#col1, col2, col3 = st.columns(3)
# contratos que han reducido su importe (variaciò < 0)
#col1.metric("Reducción de importe", mc[mc['variaciò'] < 0].count())
#col2.metric("Sin cambio de importe", mc[mc['variaciò'] == 0].count())
#col3.metric("Aumento de importe", mc[mc['variaciò'] > 0].count())

st.subheader("¿Qué tipos de contratos sufren más modificaciones?")
st.write("En esta gráfica podemos cuáles son los tipos de contrato que más modificaciones sufren en función del número de modificaciones")

st.plotly_chart(px.histogram(mc, x="tipus_de_contracte_obres_serveis_subministraments", title="Numero de contratos modificados por tipo de contrato"))

st.write("Vamos a verificar ahora si los mayores cambios de importes se corresponden a obras o a otro tipo de contratos.")
st.plotly_chart(px.histogram(mc, x="tipus_de_contracte_obres_serveis_subministraments", y="import_modificacio_sense_iva", title="Importe de las modificaciones por Tipos de contratos"))

st,write("A diferencia de lo que habíamos asumido, los contatos de servicio son los que más modificaciones sufren y los que más importe tienen. Aún así, comprobamos que el importe total de la modificaciones es mínimo respecto al total")