from openai import OpenAI
import sqlite3
import requests


# client = OpenAI(
# 	base_url="https://mxxhppax9agaovsm.us-east-1.aws.endpoints.huggingface.cloud/v1/", 
# 	api_key="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" 
# )

ollama_url = "http://localhost:11434/api/chat" 

SCHEMA = '''CREATE TABLE IF NOT EXISTS "EducationData" (
    Date TEXT,
    Course_ID TEXT,
    Student_ID TEXT,
    Engagement_Score REAL,
    Performance_Score REAL,
    Activity_Type TEXT,
    Completion_Flag INTEGER,
    Dropout_Flag INTEGER,
    Feedback_Score INTEGER,
    Demographic_Info TEXT
);'''
MODEL = "llama-3-sqlcoder-8b"

# Make a POST request to the Ollama model
def llm_request(content, schema):
    top_five_rows_data = top_five_rows()
    
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
            'model': MODEL,
            "message": messages
        }  
    )

    # Check if the request was successful
    if response.status_code == 200:
        output = response.json()
        print("Model Output:", output)
    else:
        print("Error:", response.status_code, response.text)
        
        

def top_five_rows():
    connection = sqlite3.connect("edtech.db")
    cursor = connection.cursor()
    
    cursor.execute("select distinct * from EducationData limit 5;")
    print(cursor.fetchall)
    return cursor.fetchall()

llm_request("count total rows in the table", SCHEMA)


def llm_request(content, schema):
    # Getting the top 5 rows and sending as metadata
    top_five_rows_data = top_five_rows()
    
    chat_completion = client.chat.completions.create(
        model="tgi",
        messages=[
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
        top_p=None,
        temperature=None,
        # max_tokens=150,
        stream=True,
        seed=None,
        frequency_penalty=None,
        presence_penalty=None
    )

    # print(chat_completion)
    # print('-'*40)
    # print(message.choices[0].delta for message in chat_completion)
    
    sql = ""
    
    for message in chat_completion:
        # print(message.choices[0].delta.content, end="")
        sql += message.choices[0].delta.content
        
    return sql
        