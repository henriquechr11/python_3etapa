import streamlit as st
import pandas as pd

st.title("Notas 3ª Etapa")

st.subheader("3A1")

nome = st.text_input("Digite o seu nome")

st.write("Olá,", nome, "bem-vindo ao Colégio COTEMIG")

df = pd.DataFrame({'disciplina': ["Python", "Matemática", "Português"], 'nota': [10, 5, 0]})

df

st.write("A Eliza está brava, estude mais Português")
