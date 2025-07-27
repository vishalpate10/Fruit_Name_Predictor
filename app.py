import streamlit as st
import pandas as pd
import pickle

# ✅ Set background image
st.markdown('''
<style>
.stApp {
    background-image: url("https://images.wallpaperscraft.com/image/single/fruit_exotic_pineapple_43771_3840x2400.jpg");
    background-size: cover;
    background-position: center;
}
</style>
''', unsafe_allow_html=True)

# ✅ Load model
with open("fruit_prediction.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🍓 Fruit Name Prediction App")
st.markdown("Enter fruit details to predict the fruit name.")

# ✅ Encoding dictionaries
color_map     = {'green': 0, 'yellow': 1, 'red': 2, 'orange': 3, 'purple': 4}
season_map    = {'winter': 0, 'all season': 1, 'summer': 2}
shape_map     = {'round': 0, 'long': 1, 'oval': 2}
taste_map     = {'sweet': 0, 'sour': 1}
skin_map      = {'smooth': 0, 'peelable': 1, 'rough': 2}
fruit_map_rev = {0: 'apple', 1: 'banana', 2: 'mango', 3: 'orange', 4: 'watermelon', 5: 'grapes'}

# ✅ User input form
color = st.selectbox("Color", list(color_map.keys()))
season = st.selectbox("Season", list(season_map.keys()))
average_weight_g = st.number_input("Average Weight (g)", 10, 5000, 200)
shape = st.selectbox("Shape", list(shape_map.keys()))
taste = st.selectbox("Taste", list(taste_map.keys()))
size_cm = st.slider("Size (cm)", 1.0, 30.0, 10.0)
is_seeded = st.radio("Is it Seeded?", ['Yes', 'No'])
skin_type = st.selectbox("Skin Type", list(skin_map.keys()))

# ✅ Encode inputs
input_data = pd.DataFrame([[
    color_map[color],
    season_map[season],
    average_weight_g,
    shape_map[shape],
    taste_map[taste],
    size_cm,
    1 if is_seeded == 'Yes' else 0,
    skin_map[skin_type]
]], columns=[
    'color', 'season', 'average_weight_g', 'shape', 'taste', 'size_cm', 'is_seeded', 'skin_type'
])

# ✅ Prediction
if st.button("Predict Fruit"):
    prediction = model.predict(input_data)[0]
    fruit_name = fruit_map_rev.get(prediction, "Unknown")
    st.success(f"🍉 Predicted Fruit: **{fruit_name.upper()}**")
