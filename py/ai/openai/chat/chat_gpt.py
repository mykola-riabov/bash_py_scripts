import openai

# Replace YOUR_API_KEY with your OpenAI API key
api_key = "YOUR_API_KEY"

# Install the API key
openai.api_key = api_key

def generate_answer(question, context, max_tokens=1000, temperature=1):
    # We are forming a query to GPT-3.5 for generating an answer to the question
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Question: {question}\nContext: {context}\nAnswer:",
        max_tokens=max_tokens,  # Maximum number of tokens in the response
        temperature=temperature,  # temperature parameter for response diversity
        stop=None  # Stop condition for ending the response
    )

    # We get the answer from the GPT-3.5 response
    answer = response.choices[0].text.strip()
    return answer

# Prompting the user for a question
question = input("Enter your question: ")

# Prompting the user for context
context = input("Enter the context: ")

# Generating the answer to the question with a high value of max_tokens
gpt_answer = generate_answer(question, context, max_tokens=1000, temperature=1)
print("Question:", question)
print("Answer:", gpt_answer)
