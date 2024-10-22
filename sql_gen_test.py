from openai import OpenAI
import utils
import dotenv
import os

dotenv.load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def llm_request(content, schema, database_uri):
    # Getting the top 5 rows and sending as metadata
    db_util = utils.DatabaseUtil(database_uri)
    top_five_rows_data = db_util.top_five_rows()

    ### Connecting to HF endpoint ###
    # chat_completion = client.chat.completions.create(
    #     model="tgi",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "Below is the schema to the database. Create and send only the accurate sql queries for the schema."
    #             '''{}'''
    #             '''These are the top 5 distinct rows:
    #             {}'''
    #             .format(schema, top_five_rows_data)
    #         },
    #         {
    #             "role": "user",
    #             "content": content
    #         }
    # ],
    #     # Change the below as per requirements:
    #     # top_p=None,
    #     # temperature=None,
    #     # max_tokens=150,
    #     # stream=True,
    #     # seed=None,
    #     # frequency_penalty=None,
    #     # presence_penalty=None
    # )

    """Connecting to OpenAI endpoint for testing"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use the latest available model
        messages=[
            {"role": "system", "content": "Below is the schema to the database. Create and send only the accurate sql queries for the schema. Don't use markdown."
                '''{}'''
                '''These are the top 5 distinct rows:
                    {}'''
                .format(schema, top_five_rows_data)},
            {"role": "user", "content": content}
        ],
        stream=True  # Enable streaming
    )

    # Stream the response
    sql = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            sql += content
            yield content

    return sql 