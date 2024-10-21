import sqlite3
import psycopg2
import mysql.connector
import cx_Oracle
import pyodbc

class DatabaseUtil:
    def __init__(self, database_uri, db_type='SQLite'):
        self.db_type = db_type
        if db_type == 'SQLite':
            self.connection = sqlite3.connect(database_uri)
        elif db_type == 'PostgreSQL':
            self.connection = psycopg2.connect(database_uri)
        elif db_type == 'MySQL':
            self.connection = mysql.connector.connect(**database_uri)
        elif db_type == 'Oracle':
            self.connection = cx_Oracle.connect(database_uri)
        elif db_type == 'MSSQL':
            self.connection = pyodbc.connect(database_uri)
        else:
            raise ValueError("Unsupported database type")
        self.cursor = self.connection.cursor()

    def top_five_rows(self):
        if self.db_type == 'SQLite':
            return self._top_five_rows_sqlite()
        elif self.db_type == 'PostgreSQL':
            return self._top_five_rows_postgres()
        elif self.db_type == 'MySQL':
            return self._top_five_rows_mysql()
        elif self.db_type == 'Oracle':
            return self._top_five_rows_oracle()
        elif self.db_type == 'MSSQL':
            return self._top_five_rows_mssql()

    def _top_five_rows_sqlite(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = self.cursor.fetchall()
        
        table_list = []
        
        for table in table_names:
            sql_query = f"SELECT DISTINCT * FROM {table[0]} LIMIT 3;"
            
            self.cursor.execute(sql_query)
            table_list.append(self.cursor.fetchall())
        
        return table_list

    def _top_five_rows_postgres(self):
        self.cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        table_names = self.cursor.fetchall()
        
        table_list = []
        
        for table in table_names:
            sql_query = f"SELECT DISTINCT * FROM {table[0]} LIMIT 3;"
            
            self.cursor.execute(sql_query)
            table_list.append(self.cursor.fetchall())
        
        return table_list

    def _top_five_rows_mysql(self):
        self.cursor.execute("SHOW TABLES")
        table_names = self.cursor.fetchall()
        
        table_list = []
        
        for table in table_names:
            sql_query = f"SELECT DISTINCT * FROM {table[0]} LIMIT 3;"
            
            self.cursor.execute(sql_query)
            table_list.append(self.cursor.fetchall())
        
        return table_list

    def _top_five_rows_oracle(self):
        self.cursor.execute("SELECT table_name FROM user_tables")
        table_names = self.cursor.fetchall()
        
        table_list = []
        
        for table in table_names:
            sql_query = f"SELECT DISTINCT * FROM {table[0]} WHERE ROWNUM <= 3"
            
            self.cursor.execute(sql_query)
            table_list.append(self.cursor.fetchall())
        
        return table_list

    def _top_five_rows_mssql(self):
        self.cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        table_names = self.cursor.fetchall()
        
        table_list = []
        
        for table in table_names:
            sql_query = f"SELECT DISTINCT TOP 3 * FROM {table[0]}"
            
            self.cursor.execute(sql_query)
            table_list.append(self.cursor.fetchall())
        
        return table_list


    def __del__(self):
        if self.connection:
            self.connection.close()
