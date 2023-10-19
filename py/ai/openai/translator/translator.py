#!/usr/bin/python3

import openai

# Replace YOUR_API_KEY with your API key from OpenAI
api_key = "YOUR_API_KEY"

# Set the API key
openai.api_key = api_key


def translate_text(text, target_language="en", source_language="en"):
    # Determine the source and target languages
    if source_language == "en" and target_language == "ru":
        prompt = f"Translate the following English text to Russian: '{text}'"
    elif source_language == "ru" and target_language == "en":
        prompt = f"Translate the following Russian text to English: '{text}'"
    else:
        return "Invalid language parameters"

    # Form a request to GPT-3.5 for text translation
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000  # Maximum number of tokens in the response
    )

    # Get the translation from the GPT-3.5 response
    translation = response.choices[0].text.strip()
    return translation


while True:
    # Request the source language from the user
    source_language = input("Choose the source language (en/ru): ").lower()
    if source_language not in ["en", "ru"]:
        print("Invalid language. Please choose 'en' or 'ru'.")
        continue

    user_input = input(f"Enter the text for translation to {source_language} (type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Determine the target language
    target_language = "ru" if source_language == "en" else "en"

    # Translate the text to the target language
    translation = translate_text(user_input, target_language, source_language)
    print(f"{source_language.capitalize()} text:", user_input)
    print(f"{target_language.capitalize()} translation:", translation)
