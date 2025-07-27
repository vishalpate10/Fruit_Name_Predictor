import streamlit as st
import pandas as pd
import pickle

# ✅ Set background image using HTML + CSS
st.markdown('''
<style>
.stApp {
    background-image: url("https://images.wallpaperscraft.com/image/single/fruit_exotic_pineapple_43771_3840x2400.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
''', unsafe_allow_html=True)

# ✅ Load the trained model
with open("fruit_prediction.pkl", "rb") as f:
    model = pickle.load(f)

# ✅ Page title
st.title("🍓 Fruit Name Prediction App")
st.markdown("Enter fruit features below to predict the fruit name.")

# ✅ Encoding dictionaries (must match training time)
color_map = {'red': 0, 'yellow': 1, 'green': 2, 'orange': 3, 'purple': 4, 'brown': 5}
season_map = {'summer': 0, 'winter': 1, 'rainy': 2, 'all': 3}
shape_map = {'round': 0, 'oval': 1, 'elongated': 2, 'irregular': 3}
taste_map = {'sweet': 0, 'sour': 1, 'bitter': 2, 'bland': 3}
skin_map = {'smooth': 0, 'rough': 1, 'spiky': 2}

# ✅ Reverse label encoding (int → fruit name)
fruit_label_map = {
    0: 'Apple',
    1: 'Banana',
    2: 'Mango',
    3: 'Watermelon',
    4: 'Grapes',
    5: 'Orange',
    6: 'Pineapple'
}

# ✅ User input form
color = st.selectbox("Color", list(color_map.keys()))
season = st.selectbox("Season", list(season_map.keys()))
average_weight_g = st.number_input("Average Weight (grams)", 10, 3000, 200)
shape = st.selectbox("Shape", list(shape_map.keys()))
taste = st.selectbox("Taste", list(taste_map.keys()))
size_cm = st.slider("Size (cm)", 1.0, 30.0, 10.0)
is_seeded = st.radio("Is it Seeded?", ['Yes', 'No'])
skin_type = st.selectbox("Skin Type", list(skin_map.keys()))

# ✅ Encode inputs
is_seeded_val = 1 if is_seeded == 'Yes' else 0

input_data = pd.DataFrame([[
    color_map[color],
    season_map[season],
    average_weight_g,
    shape_map[shape],
    taste_map[taste],
    size_cm,
    is_seeded_val,
    skin_map[skin_type]
]], columns=['color', 'season', 'average_weight_g', 'shape', 'taste', 'size_cm', 'is_seeded', 'skin_type'])

# ✅ Prediction
if st.button("Predict Fruit"):
    prediction = model.predict(input_data)[0]
    fruit_name = fruit_label_map.get(prediction, "Unknown")
    st.success(f"🍉 Predicted Fruit: **{fruit_name.upper()}**")
