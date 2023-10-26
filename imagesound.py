import pytesseract, pyttsx3

def image_to_speech(image_path):
    text = pytesseract.image_to_string(image_path)  # Perform OCR on the image
    engine = pyttsx3.init()  # Initialize the speech synthesis engine
    engine.say(text)  # Convert text to speech
    engine.runAndWait()  # Wait for the speech to finish

# Usage example
image_path = "path/to/your/image.png"
image_to_speech(image_path)
