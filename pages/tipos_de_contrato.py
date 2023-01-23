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

st.title("Tipos de contratos públicos")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

st.write("La administración pública dispone de múltiples mecanismos para contratar bienes y servicios. Idealmente, los contratos públicos deberían ser transparentes y accesibles para todo tipo de entidades. **Este tipo de contratos se denominan abiertos**, ya que están abiertos a que cualquier entidad, que cumpla las debidas garantías, pueda presentar una oferta para la adjudicación del contrato.")
st.write("En la práctica, este tipo de contratos requiere de publicidad y un proceso de licitación entre las distintas ofertas, lo que hace el proceso bastante largo. Por ello la ley establece la existencia de **contratos menores**, con importe limitado, que pueden adjudicarse a la mejor de tres ofertas. El importe de estos contratos es limitado y el límite varía en función de si son suministros, servicios y obras.")

st.subheader("Tipos de contratos en el Ayuntamiento de Barcelona 2021")

st.write('En la siguiente gráfica vamos a ver el número de contratos realizados, agrupados por tipo')
st.plotly_chart(px.bar(df, x="Tipo de contrato", y="Número", color="Tipo de contrato", title="Número de contratos por tipo"))