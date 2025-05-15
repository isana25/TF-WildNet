import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import json

# Load model and class names JSON
model = tf.keras.models.load_model("animal_classifier.keras")

with open("class_names.json", "r") as f:
    class_names = json.load(f)

def predict_image(image):
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    confidence = np.max(preds)
    predicted_index = np.argmax(preds)

    threshold = 0.5  # minimum confidence to accept prediction

    if confidence < threshold:
        return "Image not recognized as any animal in the dataset"
    else:
        return class_names[predicted_index]

demo = gr.Interface(fn=predict_image, inputs=gr.Image(type="pil"), outputs="text",
                    title="MobileNetV2 Animal Classifier")

demo.launch()
