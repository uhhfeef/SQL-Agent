# SQL Agent Boilerplate

## Overview
This project aims to democratize SQL queries for non-technical users and demonstrate how companies can leverage Large Language Models (LLMs) to make data more accessible. 

## Project Structure
The project is set up as a Python-based application with the following key components:

- `sql_gen.py`: Main script for SQL generation logic
- `ollama.py`: Integration with the Ollama LLM
- `streamlit_db_chat.py`: User interface for interacting with the SQL agent
- SQL database integration (using SQLite)

## Features
- Natural language to SQL query conversion
- SQL query explanation for better understanding
- Database schema exploration through natural language
- Interactive chat interface for querying databases
- Integration with Ollama for local LLM processing

## Setup and Installation
1. Clone the repository
2. Create a virtual environment:   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`   ```
3. Install dependencies:   ```
   pip install -r requirements.txt   ```
4. Deploy the defog/llama-3-sqlcoder-8b model to a Hugging Face Inference Endpoint:
   a. Go to the Hugging Face website and sign in to your account
   b. Navigate to the defog/llama-3-sqlcoder-8b model page
   c. Click on "Deploy" and select "Inference Endpoints"
   d. Choose your preferred cloud provider and region (e.g., AWS us-east-1)
   e. Select the instance type based on your requirements
   f. Configure any additional settings as needed
   g. Click "Create Endpoint" to deploy the model
   h. Once deployed, you'll receive an endpoint URL similar to:
      https://mxxhppax9agaovsm.us-east-1.aws.endpoints.huggingface.cloud/v1/
5. Update the `sql_gen.py` file with your Hugging Face API token and the new endpoint URL

## Usage
1. Run the Streamlit app:   ```
   streamlit run streamlit_db_chat.py   ```
2. Use the chat interface to interact with your database using natural language

## Development
This project demonstrates:
- LLM integration for natural language processing
- SQL query generation from natural language
- Database connectivity and querying
- User-friendly interface for database interactions
