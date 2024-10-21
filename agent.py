import dotenv
from openai import OpenAI
import os 
import prompts

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

dotenv.load_dotenv()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a quick haiku about recursion in programming."}
]

# Make the API call to get a response from the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)SELECT * FROM EducationData LIMIT 1;

# Print the generated response
print(response.choices[0].message.content)