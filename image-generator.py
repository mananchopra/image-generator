import os
from flask import Flask, request, send_file, jsonify
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

PROJECT_ID = "your project id"
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)

app = Flask(__name__)

# Directory to save generated images
IMAGE_DIR = "generated_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

def generate_image(prompt):
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = model.generate_images(
        prompt=prompt,
        number_of_images=1,  # You can change this to generate more images
        aspect_ratio="1:1",  # Specify the aspect ratio
        safety_filter_level="block_some"  # Set the safety filter level
    )
    return images[0]  # Return the generated image

@app.route('/generate_image', methods=['POST'])
def generate_image_api():
    data = request.json
    news_description = data.get('newsDescription')
    news_event_id = data.get('newsEventId')

    if not news_description or not news_event_id:
        return jsonify({"error": "newsDescription and newsEventId are required"}), 400

    # Define the image file path
    image_path = os.path.join(IMAGE_DIR, f"{news_event_id}.png")

    # Check if the image already exists
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/png')

    # Generate a new image
    generated_image = generate_image(news_description)
    generated_image.save(image_path, include_generation_parameters=False)  # Save the generated image

    return send_file(image_path, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5012)