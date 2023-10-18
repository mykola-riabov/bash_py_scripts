#!/usr/bin/python3
import openai

# Replace YOUR_API_KEY with your OpenAI API key
api_key = "YOUR_API_KEY"

# Install the API key
openai.api_key = api_key


def chat_with_gpt(question, context, max_tokens=1000, temperature=1):
    # Concatenate the question and context to create a chat-like interaction
    prompt = f"You: {question}\nAI: {context}\nYou:"

    # We are forming a query to GPT-3.5 for generating a chat-like continuation
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_tokens,  # Maximum number of tokens in the response
        temperature=temperature,  # Temperature parameter for response diversity
        stop=None  # Stop condition for ending the response
    )

    # Extract the AI's reply from the GPT-3.5 response
    reply = response.choices[0].text.strip()
    return reply


if __name__ == "__main__":
    print("You are chatting with a GPT-3.5 model. Type 'exit' to end the conversation.")

    # Initialize context as an empty string
    context = ""

    while True:
        user_input = input("You: ")

        # Allow the user to exit the chat
        if user_input.lower() == 'exit':
            break

        # Incorporate user input into the conversation context
        context += f"You: {user_input}\n"

        # Get AI's reply
        gpt_reply = chat_with_gpt(user_input, context, max_tokens=1000, temperature=1)
        print("AI:", gpt_reply)

        # Update the context with AI's reply
        context += f"AI: {gpt_reply}\n"
