import streamlit as st

def calcular_tdee(sexo, idade, peso, altura, nivel_atividade, objetivo):
    """
    Calcula o TDEE e sugere consumo calórico para emagrecimento ou ganho de massa.
    """
    if sexo == 'Masculino':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    
    fatores_atividade = {
        'Sedentário': 1.2,
        'Leve (1-3 dias/semana)': 1.375,
        'Moderado (3-5 dias/semana)': 1.55,
        'Intenso (6-7 dias/semana)': 1.725,
        'Atleta (muito intenso)': 1.9
    }
    
    tdee = tmb * fatores_atividade[nivel_atividade]
    
    if objetivo == 'Emagrecer':
        calorias_recomendadas = tdee - 500
    elif objetivo == 'Ganhar Massa':
        calorias_recomendadas = tdee + 500
    else:
        calorias_recomendadas = tdee
    
    return round(tmb, 2), round(tdee, 2), round(calorias_recomendadas, 2)

st.title("Calculadora de Calorias - TDEE")
st.write("Descubra quantas calorias você precisa consumir para emagrecer ou ganhar massa.")

sexo = st.selectbox("Selecione seu sexo", ["Masculino", "Feminino"])
idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
altura = st.number_input("Altura (cm)", min_value=100, max_value=250, step=1)
nivel_atividade = st.selectbox("Nível de atividade física", [
    "Sedentário",
    "Leve (1-3 dias/semana)",
    "Moderado (3-5 dias/semana)",
    "Intenso (6-7 dias/semana)",
    "Atleta (muito intenso)"
])
objetivo = st.selectbox("Objetivo", ["Manter Peso", "Emagrecer", "Ganhar Massa"])

if st.button("Calcular"):
    tmb, tdee, calorias = calcular_tdee(sexo, idade, peso, altura, nivel_atividade, objetivo)
    st.success(f"Sua TMB é: {tmb} kcal")
    st.success(f"Seu TDEE é: {tdee} kcal")
    st.success(f"Para {objetivo.lower()}, você deve consumir {calorias} kcal por dia.")
