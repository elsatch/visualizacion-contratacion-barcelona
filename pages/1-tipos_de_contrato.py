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

fig = px.bar(df, x="Procedimiento", y="Número", color="Procedimiento", title="Número de contratos por procedimiento")
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside', textangle=45)
fig.update_layout(barmode='group', xaxis_tickangle=-45)

st.title("Procedimientos y tipos de procedimientos de contratos públicos")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

st.write("La administración pública dispone de múltiples mecanismos para contratar bienes y servicios. Idealmente, los contratos públicos deberían ser transparentes y accesibles para todo tipo de entidades. **Este tipo de contratos se denominan abiertos**, ya que están abiertos a que cualquier entidad, que cumpla las debidas garantías, pueda presentar una oferta para la adjudicación del contrato.")
st.write("En la práctica, este tipo de contratos requiere de publicidad y un proceso de licitación entre las distintas ofertas, lo que hace el proceso bastante largo. Por ello la ley establece la existencia de **contratos menores**, con importe limitado, que pueden adjudicarse a la mejor de tres ofertas. El importe de estos contratos es limitado y el límite varía en función de si son suministros, servicios y obras.")

st.subheader("Tipos de contratos en el Ayuntamiento de Barcelona 2021")
st.write('En la siguiente gráfica vamos a ver el número de contratos realizados, agrupados por tipo')

# Personalizamos el formato de las gráficas para que se vean mejor
# fig = px.bar(df, x="Procedimiento", y="Número", color="Procedimiento", title="Número de contratos por procedimiento")

st.plotly_chart(px.bar(df, x="Procedimiento", y="Número", color="Procedimiento", title="Número de contratos por procedimiento"))

st.write('En la siguiente gráfica vamos a ver importe de los contratos realizados, agrupados por procedimiento')
st.plotly_chart(px.bar(df, x="Procedimiento", y="Importe", color="Procedimiento", title="Número de contratos por tipo"))

st.write('Podemos comprobar que aunque el número de contratos menores es mayor, el importe de los contratos abiertos es mayor. Esto se debe a que los contratos menores tienen un importe limitado, mientras que los abiertos no.')

st.subheader("Tipos de contratos en el Ayuntamiento de Barcelona 2021")
st.write('Otra forma importante de organizar los contratos tiene que ver con el tipo de contrato. Estos pueden ser de suministro, servicios o obras, etc.')
st.write('A continuación vamos a ver cuales son los tipos de contrato que han gestionado mayor importe en el Ayuntamiento de Barcelona en 2021')

st.plotly_chart(px.bar(df, x="Tipo de contrato", y="Importe", color="Tipo de contrato", title="Importe de contratos por tipo", text="Importe"))