import requests
import utils

ollama_url = "http://localhost:11434/api/chat" 


# Make a POST request to the Ollama model
def llm_request(content, schema, database_uri):
    db_util = utils.DatabaseUtil(database_uri)
    top_five_rows_data = db_util.top_five_rows()
    
    messages =[
        {
            "role": "system",
            "content": "this is the schema to the database. create and send only the accurate sql queries for the below schema."
            '''{}'''
            '''This is the top 5 distinct rows:
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
    
