import requests
import utils

# TODO: This is a work in progress

# The following code is under development
# Future improvements:
# - Error handling for API requests
# - Adding details in git repo

ollama_url = "http://localhost:11434/api/chat" 


# Make a POST request to the Ollama model
def llm_request(content, schema, database_uri):
    db_util = utils.DatabaseUtil(database_uri)
    top_five_rows_data = db_util.top_five_rows()
    
    messages =[
        {
            "role": "system",
            "content": "Below is the schema to the database. Create and send only the accurate sql queries for the schema."
            '''{}'''
            '''These are the top 5 distinct rows:
            {}'''
            .format(schema, top_five_rows_data)
        },
        {
            "role": "user",
            "content": content
        }
    ],
                    
    response = requests.post(
        ollama_url,
        json={
            'model': 'llama-3-sqlcoder-8b', # Your model name here
            "message": messages
        }  
    )

    # Check if the request was successful
    if response.status_code == 200:
        output = response.json()
        print("Model Output:", output)
    else:
        print("Error:", response.status_code, response.text)
    
