import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your trained KNN model
with open("knn_fruit_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🍓 Fruit Classifier App")
st.write("Predict the fruit based on characteristics like color, size, shape, and taste.")

# Input features
color = st.selectbox("Color", ['Red', 'Green', 'Yellow', 'Orange', 'Purple'])
season = st.selectbox("Season", ['Summer', 'Winter', 'All Season'])
average_weight_g = st.slider("Average Weight (grams)", 50, 3000, 500)
shape = st.selectbox("Shape", ['Round', 'Oval', 'Long'])
taste = st.selectbox("Taste", ['Sweet', 'Sour'])
size_cm = st.slider("Size (cm)", 1.0, 30.0, 10.0)
is_seeded = st.radio("Is it Seeded?", [0, 1])
skin_type = st.selectbox("Skin Type", ['Smooth', 'Rough', 'Peelable'])

# Convert categorical inputs to numerical form manually (if required)
# Example (only if your model was trained on label-encoded data)
input_dict = {
    "color": color,
    "season": season,
    "average_weight_g": average_weight_g,
    "shape": shape,
    "taste": taste,
    "size_cm": size_cm,
    "is_seeded": is_seeded,
    "skin_type": skin_type
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Prediction
try:
    prediction = model.predict(input_df)[0]
    st.success(f"🔍 Predicted Fruit: **{prediction}**")
except Exception as e:
    st.error(f"❌ Error during prediction: {e}")
    st.write("Please make sure the model was trained on the same feature order and data types.")



page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/free-photo/assortment-sweet-juicy-fruits_23-2148144275.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background-color: rgba(255,255,255,0.1);
}
[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.5);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
