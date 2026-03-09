import streamlit as st
import pandas as pd
import joblib

# charger le modèle
model = joblib.load("notebooks/house_price_model.pkl")

st.title("🏠 House Price Prediction AI")

st.write("Entrez les caractéristiques de la maison")

# Inputs utilisateur
bedrooms = st.slider("Nombre de chambres", 1, 10, 3)
bathrooms = st.slider("Nombre de salles de bain", 1, 5, 2)
sqft_living = st.number_input("Surface habitable (sqft)", 500, 10000, 1500)
grade = st.slider("Qualité de la maison (grade)", 1, 13, 7)
sqft_above = st.number_input("Surface au-dessus du sol", 500, 10000, 1500)
view = st.slider("Qualité de la vue", 0, 4, 0)
waterfront = st.selectbox("Maison au bord de l'eau ?", [0, 1])

# bouton de prédiction
if st.button("Estimer le prix"):

    house = pd.DataFrame(
        [[
            bedrooms,
            bathrooms,
            sqft_living,
            grade,
            sqft_above,
            view,
            waterfront
        ]],
        columns=[
            "bedrooms",
            "bathrooms",
            "sqft_living",
            "grade",
            "sqft_above",
            "view",
            "waterfront"
        ]
    )

    prediction = model.predict(house)

    price = int(prediction[0])

    st.success(f"Prix estimé : ≈ {price:,} $")