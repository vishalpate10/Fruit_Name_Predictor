import streamlit as st
import pandas as pd
import pickle

# Set custom background
page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.wallpaperscraft.com/image/single/fruit_exotic_pineapple_43771_3840x2400.jpg");
background-size: cover;
background-position: center;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load model
with open("fruit_prediction.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🍎🍌 Fruit Name Prediction App")
st.markdown("### Enter Fruit Features to Predict the Fruit Name")

# Input features
color = st.selectbox("Color", ['red', 'yellow', 'green', 'orange', 'purple', 'brown'])
season = st.selectbox("Season", ['summer', 'winter', 'rainy', 'all'])
average_weight_g = st.number_input("Average Weight (grams)", min_value=10, max_value=3000, value=200)
shape = st.selectbox("Shape", ['round', 'oval', 'elongated', 'irregular'])
taste = st.selectbox("Taste", ['sweet', 'sour', 'bitter', 'bland'])
size_cm = st.slider("Size (cm)", 1.0, 30.0, 10.0)
is_seeded = st.radio("Is it seeded?", ['Yes', 'No'])
skin_type = st.selectbox("Skin Type", ['smooth', 'rough', 'spiky'])

# Encode is_seeded manually
is_seeded_encoded = 1 if is_seeded == 'Yes' else 0

# Create input DataFrame
input_data = pd.DataFrame({
    'color': [color],
    'season': [season],
    'average_weight_g': [average_weight_g],
    'shape': [shape],
    'taste': [taste],
    'size_cm': [size_cm],
    'is_seeded': [is_seeded_encoded],
    'skin_type': [skin_type]
})

# Predict button
if st.button("Predict Fruit"):
    prediction = model.predict(input_data)[0]
    st.success(f"🍉 The predicted fruit is: **{prediction.upper()}**")
