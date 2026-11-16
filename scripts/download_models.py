import os
import urllib.request

# Define models and their download URLs
MODELS = {
    "agri_model_v1.pt": "https://example.com/path/to/your/agri_model_v1.pt",  # REPLACE WITH ACTUAL URL
    "agri_model.pt": "https://example.com/path/to/your/agri_model.pt"         # REPLACE WITH ACTUAL URL
}

DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend", "model_weights")

def download_models():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    for model_name, url in MODELS.items():
        model_path = os.path.join(DOWNLOAD_DIR, model_name)
        
        if os.path.exists(model_path):
            print(f"[INFO] {model_name} already exists. Skipping download.")
            continue
            
        if url.startswith("https://example.com"):
            print(f"[WARNING] Please update the URL for {model_name} in scripts/download_models.py")
            continue

        print(f"[INFO] Downloading {model_name}...")
        try:
            urllib.request.urlretrieve(url, model_path)
            print(f"[SUCCESS] Downloaded {model_name} to {model_path}")
        except Exception as e:
            print(f"[ERROR] Failed to download {model_name}: {e}")

if __name__ == "__main__":
    download_models()
