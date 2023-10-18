
---

## GPT-3.5 Text Translation App

This Python application utilizes the GPT-3.5 language model by OpenAI to translate text from English to Russian or vice versa. It provides a simple interface for users to input the text they wish to translate and displays the translation.

### Usage

1. Obtain an API key from OpenAI and replace `<YOUR_API_KEY>` in the code with your actual API key.
2. Run the script.
3. Enter the text you want to translate when prompted.
4. The application will translate the text and display both the original and translated texts.

### Example

```python
import openai

# Replace YOUR_API_KEY with your API key from OpenAI
api_key = "<YOUR_API_KEY>"

# Set the API key
openai.api_key = api_key

# Function to translate text using GPT-3.5
def translate_text(text, target_language="en"):
    # Form a request to GPT-3.5 for text translation
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following English text to {target_language}: '{text}'",
        max_tokens=1000  # Maximum number of tokens in the response
    )

    # Get the translation from the GPT-3.5 response
    translation = response.choices[0].text.strip()
    return translation

# Request text for translation from the user
english_text = input("Enter the text for translation to Russian: ")

# Translate the text to Russian
russian_translation = translate_text(english_text, target_language="ru")
print("English text:", english_text)
print("Russian translation:", russian_translation)
```

### Note

This application uses the GPT-3.5 engine by OpenAI to perform translations. Ensure you have the necessary API access and permissions before using this app.

---