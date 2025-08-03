import streamlit as st
import os
import numpy as np
from tensorflow.keras.preprocessing import image
from utils.model_loader import load_model

st.set_page_config(page_title="🌿 Tree Species Classifier")

# Directories with models
MODEL_PATHS = {
    "Model_H5": "Model_H5",
    "Model_H5_1.o": "Model_H5_1.o",
    "Models": "Models"
}

# Scan and collect all models
model_files = {}
for label, folder in MODEL_PATHS.items():
    full_path = os.path.join(folder)
    if os.path.isdir(full_path):
        for file in os.listdir(full_path):
            if file.endswith((".h5", ".keras")):
                model_files[f"{label}/{file}"] = os.path.join(full_path, file)

st.title("🌳 Tree Species Classification from Leaf Image")
st.markdown("Upload a leaf image and select a trained model to predict the species.")

# Upload image
uploaded_file = st.file_uploader("📁 Upload Leaf Image", type=["jpg", "jpeg", "png"])

# Choose model
model_choice = st.selectbox("🧠 Choose a Model", list(model_files.keys()))

if uploaded_file and model_choice:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Load and prepare model
    model_path = model_files[model_choice]
    model = load_model(model_path)

    # Preprocess image
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_batch)
    predicted_class = np.argmax(prediction[0])
    confidence = np.max(prediction[0])

    # Class labels mapping — update based on your dataset
    labels = ["amla", "asopalav", "babul", "bamboo", "banyan", "bili", "cactus",
    "champa", "coconut", "garmalo", "gulmohar", "gunda", "jamun",
    "kanchan", "kesudo", "khajur", "mango", "motichanoti", "neem",
    "nilgiri", "other", "pilikaren", "pipal", "saptaparni", "shirish",
    "simlo", "sitafal", "sonmahor", "sugarcane", "vad"]  # Change if different
    species_name = labels[predicted_class]

    st.success(f"✅ Predicted Species: **{species_name}** (Class {predicted_class}) with {confidence*100:.2f}% confidence")
