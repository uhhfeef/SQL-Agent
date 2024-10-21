import requests

# Replace with your Hugging Face API token
API_TOKEN = ''
headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}

# Define the model and input data
model = "defog/llama-3-sqlcoder-8b"  # or any other model available on Hugging Face
data = {
    "inputs": "Generate a SQL query to answer this question: What are the sales for Q1?"
}

# Make a POST request to the inference API
response = requests.post(f'https://api-inference.huggingface.co/models/{model}', headers=headers, json=data)

# Print the response from the model
print(response.json())