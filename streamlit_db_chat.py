import streamlit as st
import sqlite3
# from sql_gen import llm_request
from sql_gen_test import llm_request
from utils import DatabaseUtil


# Function to execute SQL query using DatabaseUtil
def execute_query(db_type, database_uri, sql_query):
    try:
        db_util = DatabaseUtil(database_uri, db_type)
        db_util.cursor.execute(sql_query)
        output = db_util.cursor.fetchall()
        return output
    except Exception as e:
        st.error(f"An error occurred while executing the SQL query: {e}")
        return None


# Streamlit app layout
st.title("Multi-Database Connection")

# Dropdown for selecting database type
db_type = st.sidebar.selectbox("Select Database Type", options=["SQLite", "PostgreSQL", "MySQL", "Oracle", "MSSQL"])

# Sidebar for taking database URI input
database_uri = st.sidebar.text_input("Database URI")

if not database_uri:
    st.info("Enter a database URI to continue")
    st.stop()    
    
    
# Input for database schema
with st.sidebar.form("my_form"):
    schema = st.text_area("Enter your database schema here:")
    submitted = st.form_submit_button("Submit")
        
if not schema:
    st.info("Enter a database schema to continue")
    st.stop()    
    
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Accept user input
if query := st.chat_input("Chat with your database"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)
        
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Create a placeholder for the assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response from the LLM
        for response_chunk in llm_request(query, schema, database_uri):
            full_response += response_chunk
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # Extract the SQL query from the full response
    sql_query = full_response

    # Execute the SQL query
    output = execute_query(db_type, database_uri, sql_query)
    print('outputw',output)

    # Print the output as an assistant response
    with st.chat_message("assistant"):
        st.markdown(f"Query Result:\n```\n{output[0][0]}\n```")
    


