from openai import OpenAI
import utils
import dotenv
import os
from streamlit_db_chat import hf_api_call

dotenv.load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

hf_url, hf_token = hf_api_call()

client = OpenAI(
	base_url=hf_url, 
	api_key=hf_token 
)

def llm_request(content, schema, database_uri):
    # Fetch sample data from the database for context
    db_util = utils.DatabaseUtil(database_uri)
    top_five_rows_data = db_util.top_five_rows()

    ### Connecting to HF endpoint ###
    chat_completion = client.chat.completions.create(
        model="tgi",
        messages=[
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
        # Change the below as per requirements:
        # top_p=None,
        # temperature=None,
        # max_tokens=150,
        # stream=True,
        # seed=None,
        # frequency_penalty=None,
        # presence_penalty=None
    )

    sql = ""

    for message in chat_completion:
        sql += message.choices[0].delta.content

    return sql
