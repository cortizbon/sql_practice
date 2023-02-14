import streamlit as st
import sqlite3 as sq
import pandas as pd
import re
from streamlit_ace import st_ace

st.set_page_config(layout="wide")

CONN = sq.connect('test_database')

def query_function(query):
    df = pd.read_sql(query, con=CONN)
    return df

def verify_query(query):
    return "SELECT" == query[:6]


st.title('SQL simulation')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.subheader("Clientes")
    st.markdown("`nombre`: nombre del cliente")
    st.markdown("`apellido`: apellido del cliente")
    st.markdown("`edad`: edad del cliente")
    st.markdown("`id_cliente`: identificador único del cliente (primary key)")
    st.markdown("`ciudad`: ciudad de origen del cliente")

with col2:
    st.subheader("Vendedores")
    st.markdown("`nombre`: nombre del vendedor")
    st.markdown("`apellido`: apellido del vendedor")
    st.markdown("`edad`: edad del vendedor")
    st.markdown("`id_vendedor`: identificador único del vendedor (primary key)")
    st.markdown("`tienda`: tienda donde trabaja el vendedor")

with col3:
    st.subheader("Ventas")
    st.markdown("`id_venta`: identificador único de la venta (primary key)")
    st.markdown("`id_vendedor`: identificador del vendedor")
    st.markdown("`id_cliente`: identificador del cliente")
    st.markdown("`fecha`: fecha en que se realizó la compra")
    st.markdown("`forma_pago`: forma de pago de la compra")
    st.markdown("`id_producto`: identificador del producto comprado")
    st.markdown("`cantidad`: cantidad vendida")

with col4:
    st.subheader("Productos")
    st.markdown("`nombre`: nombre del producto")
    st.markdown("`marca`: marca del producto")
    st.markdown("`id_producto`: identificador único del producto (primary key)")
    st.markdown("`costo`: costo del producto")
    st.markdown("`precio`: precio del producto")

with col5:
    st.subheader("Tiendas")
    st.markdown("`ciudad`: ciudad donde está ubicada la tienda")
    st.markdown("`direccion`: dirección de la tienda")
    st.markdown("`id_tienda`: identificador único de la tienda (primary key)")
    st.markdown("`manager`: nombre del administrador de la tienda")


col1, col2 = st.columns(2, [2, 1])
with col1:
    query = st_ace(placeholder='Escriba su query', language='sql', min_lines=15, auto_update=True)
with col2:
    st.code(query, language='sql')

if st.button("Ejecutar query"):
    try:
        if verify_query(query):
            df = query_function(query)
            st.dataframe(df)
        else:
            st.text("Verifique la query. Debe empezar con la palabra SELECT.")
    except:
        st.text("Hay un error con la query. Verifique la sintaxis.")
