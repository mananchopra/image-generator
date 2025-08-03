# 🎨 AI Image Generator API

> A powerful Flask-based REST API for generating high-quality images using Google Vertex AI's Imagen-3.0 model.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Imagen%203.0-orange.svg)](https://cloud.google.com/vertex-ai)

## ✨ Features

- 🚀 **RESTful API** - Simple HTTP endpoints for on-demand image generation
- 🎯 **High-Quality Images** - Powered by Google Vertex AI's Imagen-3.0 model
- 💾 **Smart Caching** - Automatic image caching to avoid regeneration
- 🔒 **Safety Filters** - Configurable content safety controls
- ⚙️ **Customizable** - Adjustable image properties and generation parameters
- 📁 **Local Storage** - Images saved to local directory for easy access

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client App    │───▶│  Flask API      │───▶│  Vertex AI      │
│                 │    │  (Port 5012)    │    │  Imagen-3.0     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │ generated_images│
                       │ Directory       │
                       └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Google Cloud Account** - [Sign up for GCP](https://cloud.google.com/)
- **Vertex AI Permissions** - Enable Vertex AI API in your GCP project

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd image-generator
   ```

2. **Install dependencies**
   ```bash
   pip install flask vertex-ai
   ```

3. **Configure your project**
   ```python
   # Edit image-generator.py
   PROJECT_ID = "your-gcp-project-id"
   LOCATION = "us-central1"  # Optional: change region if needed
   ```

4. **Set up authentication**
   ```bash
   # Option 1: Use service account key
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"
   
   # Option 2: Use gcloud CLI
   gcloud auth application-default login
   ```

5. **Run the server**
   ```bash
   python image-generator.py
   ```

   The API will be available at `http://localhost:5012`

## 📡 API Reference

### Generate Image

**Endpoint:** `POST /generate_image`

**Request Body:**
```json
{
  "newsDescription": "A futuristic city skyline at sunset with flying cars",
  "newsEventId": "event_2024_001"
}
```

**Response:**
- **Success:** Returns the generated image as a PNG file
- **Error:** JSON error message with appropriate HTTP status code

**Example Usage:**
```bash
curl -X POST http://localhost:5012/generate_image \
  -H "Content-Type: application/json" \
  -d '{
    "newsDescription": "A serene mountain landscape with snow-capped peaks",
    "newsEventId": "mountain_scene_001"
  }' \
  --output generated_image.png
```

## ⚙️ Configuration

### Image Generation Parameters

You can customize the image generation by modifying these parameters in `image-generator.py`:

```python
def generate_image(prompt):
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    images = model.generate_images(
        prompt=prompt,
        number_of_images=1,           # Generate multiple images
        aspect_ratio="1:1",          # Options: "1:1", "16:9", "9:16"
        safety_filter_level="block_some"  # Options: "block_some", "block_few"
    )
    return images[0]
```

### Available Options

| Parameter | Options | Description |
|-----------|---------|-------------|
| `aspect_ratio` | `"1:1"`, `"16:9"`, `"9:16"` | Image aspect ratio |
| `safety_filter_level` | `"block_some"`, `"block_few"` | Content safety level |
| `number_of_images` | `1-4` | Number of images to generate |

## 📁 Project Structure

```
image-generator/
├── image-generator.py      # Main Flask application
├── README.md              # This file
├── generated_images/       # Generated image storage
│   ├── event_001.png
│   ├── event_002.png
│   └── ...
└── requirements.txt       # Python dependencies (optional)
```

## 🔧 Development

### Local Development

1. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run in debug mode**
   ```bash
   export FLASK_ENV=development
   python image-generator.py
   ```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account key | None |
| `PROJECT_ID` | GCP Project ID | "your project id" |
| `LOCATION` | Vertex AI region | "us-central1" |

## 🛡️ Security Considerations

- **Authentication**: Ensure proper GCP authentication is configured
- **Input Validation**: The API validates required fields
- **Rate Limiting**: Consider implementing rate limiting for production
- **CORS**: Configure CORS headers if needed for web applications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- **Google Vertex AI** - For providing the powerful Imagen-3.0 model
- **Flask** - For the lightweight web framework
- **Python Community** - For excellent documentation and support

---

**Made with ❤️ using Flask and Google Vertex AI**

*Star this repository if you found it helpful!*
