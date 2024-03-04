
# ImageRenamerAI

ImageRenamerAI is a tool that renames images using AI, making it easier to manage and find your photos by describing what's in them. It was built to help organize photo collections

## Demo

https://github.com/khalid-nur/ai-image-file-renamer/assets/85604999/fbd8df07-bb1a-438a-93b9-67dd90a3d082

## Getting Started

Before you begin, ensure you have Python installed on your system and an active OpenAI API key. Here is a link to get your OpenAI Key 👉🏽 https://openai.com/product#made-for-developers

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/khalid-nur/ai-image-file-renamer.git
   ```

2. **Navigate to the Project Directory**

   ```bash
    cd ai-image-file-renamer
   ```

3. **Install Dependencies**
   ```bash
    pip install requests python-dotenv
   ```
4. **Create a .env file in the root directory and add your OpenAI API key**

   ```bash
   SECRET_KEY=your_openai_api_key_here
   ```

## How to Use ImageRenamerAI

1.  **Run the Script**

    ```bash
    python main.py
    ```

2.  **Provide the Image Directory**

- When prompted, enter the full path to the directory containing the images you wish to rename

  ```bash
  /Users/khalidnur/Pictures/
  ```

## How It Works

- Finds all images within the directory, which supports a wide range of filetypes (PNG, JPG, JPEG, and WEBP)
- Analyzes the content of each image using OpenAI's gpt-4-vision-preview model, to accurately understand and describe the imagery
- Renames the files based on AI analysis of the image content, preserving the original file formats
- Restores the renamed files back to their original location

## Show Your Support

Give a ⭐️ if you like this project!
