# Sample script to call the OpenAI API using a placeholder API key
# Replace YOUR_OPENAI_API_KEY with your actual key before running
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)