import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json
from streamlit_extras.switch_page_button import switch_page
from streamlit_echarts import st_echarts

st.title("Contratación en Barcelona (2020-2021")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

df_file = "data/yearly_report_bcn_2021.csv"

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

df = load_data(df_file)

st.write('Bienvenido a esta página, en la que podrás descubrir en detalle la contratación del Ayuntamiento de Barcelona, a partir de los de datos abiertos municipales. En concreto, vamos a explorar los datos correspondientes al años 2021, ya que los datos correspondientes a 2022 todavía no están disponibles.')

st.subheader("¿Qué es la contratación pública?")
st.write('La contratación pública es el conjunto de procedimientos que se llevan a cabo para la adquisición de bienes y servicios por parte de las administraciones públicas. En el caso de Barcelona, esta puede realizarse tanto desde el Ayuntamiento como desde una serie de organismos autónomos vinculados al Ayuntameiento')
st.write('El Ayuntamiento de Barcelona está organzado internamente en una serie de gerencias y distritos. Las gerencias son áreas transversales, mientras que los distritos son áreas geográficas. En el siguiente gráfico, podemos ver la estructura de la organización')

# Problemas encontrados al cargar los datos
# Para no variar, dentro del propio fichero aparecen las entidades en mayúsculas y en minúsculas
# Antes de construir el árbol, vamos a pasar todo a mayúsculas, aunque me gustaria retener el formato original

# df["Nombre_entidad"] = df["Nombre_entidad"].str.upper()
# df["Tipo_entidad"] = df["Tipo_entidad"].str.upper()

# Para no variar, los nombres no coinciden entre los años, así que salen multitud de duplicados
# Extraemos la estructura de entidades del Ayuntamiento de Barcelona del año 2021

bcn_structure = df[['Tipo_entidad', 'Nombre_entidad']].drop_duplicates()

# Creamos una visualización tipo sunburst de plotly
st.plotly_chart(px.sunburst(bcn_structure, path=['Tipo_entidad', 'Nombre_entidad'], title='Entidades del Ayuntamiento de Barcelona con capacidad de contratar'))

st.subheader("Importe de los Contratos")

st.write('En primer lugar, vamos a ver explorar el importe total de los contra que se han realizado en Barcelona en los años 2021')
#st.write(minor_contracts_df.groupby('organo_gestor').agg({'importe': 'sum', 'id': 'count'}).rename(columns={'id': 'contratos'}).sort_values('contratos', ascending=False))

importe_total = df['Importe'].sum()
st.metric(label="Importe total", value="3.668.900.917,40€")

st.write('¿Cómo se reparten estos contratos entre los distintos tipos de entidades? En el siguiente gráfico, podemos ver el importe total de los contratos por tipo de entidad')
st.plotly_chart(px.histogram(df, x='Tipo_entidad', y='Importe', color='Tipo_entidad', title='Importe por Tipo de entidad'))

st.write('A continuación vamos a visualizar el número de contratos realizados por entidad, independientemente de su importe')
st.plotly_chart(px.histogram(df, x='Nombre_entidad', y='Número', color='Tipo_entidad', title='Número de contratos por entidad'))

st.write('El Ayuntamiento de Barcelona, es la entidad que realiza mayor número de contratos y por un mayor importe. Aún así, podemos observar que el resto de entidades gestionan un tercio del volumen total de compras (por importe')
st.write('Dado que estamos explorando los distintos contratos te aniamos a explorar el siguiente gráfico interactivo para saber más sobre los contratos realizados por el Ayuntamiento de Barcelona en 2021')

st.plotly_chart(px.treemap(df, path=['Tipo_entidad', 'Nombre_entidad', 'Tipo de contrato'], values='Importe', color='Importe', color_continuous_scale='RdBu', title='Contratos realizados por el Ayuntamiento de Barcelona en 2021'))


