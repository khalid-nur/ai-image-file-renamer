import os
from dotenv import load_dotenv
import base64
import requests

# Load .env file variables
load_dotenv()


# Encode the image file to a base64-encoded string
def encodeImage(imagePath):
    with open(imagePath, "rb") as imageFile:
        return base64.b64encode(imageFile.read()).decode('utf-8')

# Send a base64-encoded image to OpenAI API to generate
def analyzeImage(secretKey, base64Image, fileExtension):
    headers = {
        "Authorization": f"Bearer {secretKey}"
    }
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [{
            "role": "user",
            "content": [{
                "type": "text",
                "text": "Given an image with a specific file type, generate a descriptive filename that captures the essence of the image. The filename should exclude any stock photo identifiers or numerical codes. The generated filename should not include the file extension."
            }, {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64Image}"
                }
            }]
        }],
        "max_tokens": 20
    }
    # OpenAI sends back a description of the image and then keep original filetype by adding its file extension
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    responseData = response.json()
    content = responseData['choices'][0]['message']['content']
    return f"{content}.{fileExtension}"

# Rename the file with the new description.
def changeFileName(folderPath, filePath, description):
    newFilePath = os.path.join(folderPath, description)
    os.rename(filePath, newFilePath)

def main(secretKey, folderPath):
    # Iterate over all files in the specified folder path
    for filename in os.listdir(folderPath):
        # Get file extension
        fileExtension = filename.split('.')[-1].lower()
        # Checks the file extension to see if it ends with theses image formats
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            filePath = os.path.join(folderPath, filename)
            print(f"Processing: {filePath}")
            # Convert the image to a base64 string
            base64Image = encodeImage(filePath)
            # Get a descriptive of the image
            description = analyzeImage(secretKey, base64Image, fileExtension)
            # Rename the file with its new descriptive
            changeFileName(folderPath, filePath, description)
            print(f"File '{filename}' has been renamed to '{description}'")


if __name__ == "__main__":
    # Retrieve the API key
    secretKey = os.getenv('SECRET_KEY')

    folderPathInput = input("Enter the file path:\n")
    # Check if the entered path is valid and exists
    if folderPathInput and os.path.isdir(folderPathInput):
        main(secretKey, folderPathInput)
    else:
        print("Error: The folder path does not exist or was not provided. Please check the path and try again")
