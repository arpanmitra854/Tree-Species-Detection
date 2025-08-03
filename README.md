# 🌳 Tree Species Classifier

A web application for classifying tree species from leaf images using deep learning models. Built with **Streamlit** and **TensorFlow/Keras**.

---

## 🚀 Features
- Upload a leaf image and predict its tree species instantly.
- Choose from multiple pre-trained models (`.h5` and `.keras` formats).
- Supports 29+ tree species.
- Easy-to-use web interface.

---

## 🗂️ Project Structure
```
Tree/
│
├── app.py                      # Main Streamlit app
├── requirement.txt             # Python dependencies
├── utils/
│   └── model_loader.py         # Utility for loading models
├── Model_H5/                   # Directory for .h5 models
├── Models/                     # Directory for .keras models
├── Tree_Species_Dataset/       # Dataset of leaf images

---

## 📦 Dataset
- **Location:** `Tree_Species_Dataset/`
- **Classes:**
  - amla, asopalav, babul, bamboo, banyan, bili, cactus, champa, coconut, garmalo, gulmohor, gunda, jamun, kanchan, kesudo, khajur, mango, motichanoti, neem, nilgiri, other, pilikaren, pipal, saptaparni, shirish, simlo, sitafal, sonmahor, sugarcane, vad
- **Format:** Each folder contains images (`.jpg`, `.jpeg`, `.png`) for a specific species.

---

## 🧠 Models
- **Supported formats:** `.h5`, `.keras`
- **Model directories:**
  - `Model_H5/` (e.g., `basic_cnn_tree_species.h5`, `my_model.h5`)
  - `Models/` (e.g., `Model1.keras`)
- **Note:** There is an improved version of the model named `improved_cnn_model.h5` which is over 200MB and is not included in the repository. Download it from the link below if required:

  👉[Download improved_cnn_model.h5 from Google Drive](https://drive.google.com/drive/folders/124RDkpUKBdHFWq8MDTs3SO7pwoTTFTyr?usp=sharing)

---

## 🖥️ Usage
1. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```
2. **Run the app:**
   ```bash
   streamlit run app.py
   ```
3. **Open in browser:**
   - Go to the local URL provided by Streamlit (usually `http://localhost:8501`)
4. **Upload a leaf image and select a model to predict the species.**

---

## 🛠️ Scripts
- `app.py`: Main web application.
- `check_model_compatibility.py`: Checks if all models in the model directories are compatible with TensorFlow/Keras.
- `utils/model_loader.py`: Utility to load models.

---

## 📋 Requirements
See [`requirement.txt`](requirement.txt) for all dependencies. Key packages:
- streamlit
- tensorflow
- keras
- numpy
- pillow

---

## 📄 License
This project is for educational and research purposes.
