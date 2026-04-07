import streamlit as st
import pandas as pd
import numpy as np

# Demo de Streamlit: Análisis Rápido de Ventas
st.title("Demo de Streamlit: Evaluación de Ventas y Márgenes")
st.write("""
Esta app sencilla permite:
- Ingresar ingresos y costos de un producto o proyecto
- Calcular beneficio bruto y margen
- Simular el efecto de un descuento sobre los ingresos
- Visualizar comparaciones en un gráfico de barras
""")

# 1) Ingresar ingresos y costos
st.header("1. Ingresar Datos de Ventas")
ingresos = st.number_input("Ingresos (€)", min_value=0.0, value=1000.0, step=100.0)
costos = st.number_input("Costos (€)", min_value=0.0, value=600.0, step=50.0)

# 2) Cálculo de beneficio y margen
st.header("2. Cálculo de Beneficio y Margen")
if st.button("Calcular Beneficio"):
    beneficio = ingresos - costos
    margen = (beneficio / ingresos * 100) if ingresos > 0 else 0
    st.metric(label="Beneficio (€)", value=f"{beneficio:.2f}")
    st.metric(label="Margen (%)", value=f"{margen:.1f}")

# 3) Simulación de descuento
st.header("3. Simulación de Descuento")
descuento = st.slider("% de descuento aplicado a ingresos", min_value=0, max_value=50, value=10)
ingresos_desc = ingresos * (1 - descuento/100)
if st.button("Simular Descuento"):
    beneficio_desc = ingresos_desc - costos
    margen_desc = (beneficio_desc / ingresos_desc * 100) if ingresos_desc > 0 else 0
    st.write(f"Ingresos tras descuento: €{ingresos_desc:.2f}")
    st.write(f"Beneficio tras descuento: €{beneficio_desc:.2f}")
    st.write(f"Margen tras descuento: {margen_desc:.1f}%")

# 4) Gráfico de comparación
st.header("4. Gráfico Comparativo")
if st.checkbox("Mostrar gráfico de barras"):
    data = pd.DataFrame({
        "Categoría": ["Ingresos", "Costos", "Beneficio"],
        "Valor (€)": [ingresos, costos, ingresos - costos]
    })
    st.bar_chart(data.set_index("Categoría"))

# Pie de página
st.write("---")
st.write("Ejecuta: `streamlit run comparador.py` desde tu terminal para probar.")
# Script para analizar abandono de clientes
#cambio para la rama de pruebas