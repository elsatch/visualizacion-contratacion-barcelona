import streamlit as st
import pandas
import plotly.express as px

st.title("Tipos de contratos públicos")
st.subheader("Visualización de datos abiertos de contratación en Barcelona")

st.write("La administración pública dispone de múltiples mecanismos para contratar bienes y servicios. Idealmente, los contratos públicos deberían ser transparentes y accesibles para todo tipo de entidades. **Este tipo de contratos se denominan abiertos**, ya que están abiertos a que cualquier entidad, que cumpla las debidas garantías, pueda presentar una oferta para la adjudicación del contrato.")
st.write("En la práctica, este tipo de contratos requiere de publicidad y un proceso de licitación entre las distintas ofertas, lo que hace el proceso bastante largo. Por ello la ley establece la existencia de **contratos menores**, con importe limitado, que pueden adjudicarse a la mejor de tres ofertas. El importe de estos contratos es limitado y el límite varía en función de si son suministros, servicios y obras.")

st.subheader("Tipos de contratos en el Ayuntamiento de Barcelona 2021")

st.write('En la siguiente gráfica vamos a ver el número de contratos realizados, agrupados por tipo')
st.plotly_chart(px.bar(df, x="Tipo", y="Número de contratos", color="Tipo", title="Número de contratos por tipo"))
