from flask import Flask, request, jsonify
from flask_cors import CORS
from waste_model import WasteClassifier
import os

app = Flask(__name__)
CORS(app)  # allow browser apps to call your API
model = WasteClassifier()

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/classify", methods=["POST"])
def classify():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = request.files["image"]
    image_path = "/tmp/uploaded.jpg"
    image.save(image_path)
    result = model.classify(image_path)
    return jsonify(result), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
