import openai

# Replace YOUR_API_KEY with your API key from OpenAI
api_key = "<YOUR_API_KEY>"

# Set the API key
openai.api_key = api_key


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


# ЗRequest text for translation from the user
english_text = input("Enter the text for translation to Russian: ")

# Translate the text to russian
russian_translation = translate_text(english_text, target_language="ru")
print("English text:", english_text)
print("Russian translation:", russian_translation)
