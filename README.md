# MobileNetV2 Animal Classifier with Gradio Deployment

This project is an animal image classification application built using a **MobileNetV2** deep learning model. The model was **trained from scratch on a custom dataset** and then deployed as an interactive web app using **Gradio**, hosted on **Hugging Face Spaces**.

---

## 🚀 Project Overview

- **Model Training:** The MobileNetV2 model was trained on a custom dataset of animal images to accurately classify different animal classes.
- **Deployment:** After training, the saved model and dynamically generated class labels were used to build a user-friendly web application with Gradio for image classification.
- **Hosting:** The app is deployed on Hugging Face Spaces for easy access and sharing.

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow / Keras (MobileNetV2)
- **Web App Framework:** Gradio
- **Deployment Platform:** Hugging Face Spaces
- **Image Processing:** Pillow, NumPy

---

## 📁 Project Structure

- `animal_classifier.keras` — Trained Keras model file  
- `class_names.json` — Class labels extracted from training data  
- `app.py` — Gradio application script for inference and UI  
- `requirements.txt` — Python dependencies for deployment  

---

## 📦 Installation & Usage

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
