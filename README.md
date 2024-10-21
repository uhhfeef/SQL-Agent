# SQL Agent

## Overview
This project aims to democratize SQL queries for non-technical users and demonstrate how companies can leverage Large Language Models (LLMs) to make data more accessible. By creating an intelligent agent capable of understanding natural language inputs and generating SQL queries, we're bridging the gap between data and those who need insights from it, regardless of their technical background.

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
4. Set up Ollama and the required model (instructions in ollama.py)

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
