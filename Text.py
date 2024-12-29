from google.cloud import vision
from google.oauth2 import service_account

# Path to your service account JSON key file
key_path = "cred.json"

# Load credentials from the service account file
credentials = service_account.Credentials.from_service_account_file(key_path)

# Initialize the Vision API client with the credentials
client = vision.ImageAnnotatorClient(credentials=credentials)

# Example function to perform text detection
def detect_text(image_path):
    # Open the image file
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create an Image object
    image = vision.Image(content=content)

    # Perform text detection on the image
    response = client.text_detection(image=image)
    
    # Extract detected text
    texts = response.text_annotations
    if texts:
        detected_text = texts[0].description  # Full detected text
        with open("detected_text.txt", "w", encoding="utf-8") as file:  # Specify UTF-8 encoding
            file.write(detected_text + "\n")  # Save each result on a new line
        return detected_text
    else:
        return "No text detected"

if __name__ == "__main__":
    # Example: Path to the image you want to analyze
    image_path = "image.png"
    
    # Detect and print the text
    text = detect_text(image_path)
    print(f"Detected text: {text}")
