import gradio as gr
from waste_model import WasteClassifier
from PIL import Image
import torch

model = WasteClassifier()

def classify(image):
    result = model.classify(image)
    return result

iface = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Label(num_top_classes=3),
    title="Augmented Waste Classifier",
    description="Upload an image to classify waste type."
)

if __name__ == "__main__":
    iface.launch()
