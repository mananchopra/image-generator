
Image Generation API with Vertex AI and Flask
This repository provides a simple Flask-based API for generating images using Google Vertex AI's Image Generation Model. The service accepts POST requests with a news description and event ID, generates an image from the prompt using Vertex AI, and serves the generated images.

Features
REST API endpoint for on-demand image generation.

Integrates with Google Vertex AI's Imagen-3.0 Model for high-quality image synthesis.

Auto-saves images to a local directory; identical prompts with the same event ID are served from cache.

Supports safety filters and configurable image properties.

Getting Started
Prerequisites
Python 3.8 or newer

Google Cloud account with Vertex AI permissions

Vertex AI Python SDK (vertex-ai), Flask

Install dependencies
bash
pip install flask vertex-ai
Configuration
Update your GCP Project ID in the script:

python
PROJECT_ID = "your project id"
If needed, adjust the LOCATION variable (default: "us-central1").

Usage
Run the server
bash
python app.py
The server will start on http://0.0.0.0:5012.

API Endpoint
POST /generate_image

Request body (JSON):
newsDescription: Description or prompt for the image (string).

newsEventId: Unique event ID to identify and cache the generated image (string).

Example:

json
{
  "newsDescription": "A futuristic city skyline at sunset",
  "newsEventId": "event12345"
}
Response
Returns the generated image as a PNG file.

Directory Structure
generated_images/: Stores all generated images, using the event ID as filename.

Customization
Change number_of_images or aspect_ratio in generate_image() for different image generation needs.

Adjust safety levels via safety_filter_level.

Notes
Vertex AI Credentials: Ensure your environment is authenticated with GCP and you have appropriate permissions to use Vertex AI.

Caching: If an image for a given event ID already exists, the API serves it directly instead of regenerating.

License
MIT License. See LICENSE for details.

Acknowledgements
Google Vertex AI

Flask

Feel free to fork and adapt this project for your custom image generation workflows!
