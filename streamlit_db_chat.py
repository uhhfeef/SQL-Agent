import streamlit as st
from sqlalchemy import create_engine
import sqlite3
from sql_gen import llm_request


# Streamlit app layout
st.title("Multi-Database Connection")

# # Dropdown for selecting database type
db_type = st.sidebar.selectbox("Select Database Type", options=["MySQL", "PostgreSQL", "SQLite", "Oracle", "Microsoft SQL Server"])

# Sidebar for taking openai input
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
    
    
# Accept user input
if query := st.chat_input("Chat with your database"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)
        
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Sending as a query to the LLM
    response = llm_request(query, schema, database_uri)

    # Writing the response from the LLM
    st.write(response)

    connection = sqlite3.connect(database_uri)
    cursor = connection.cursor()

    # Executing the generated SQL
    cursor.execute(response)
    
    output = cursor.fetchall()
    st.write('-'*50)
    st.write(str(output[0][0]))
    
    connection.close()