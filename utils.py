import sqlite3

def top_five_rows():
    connection = sqlite3.connect("edtech.db")
    cursor = connection.cursor()
    
    cursor.execute("select distinct * from EducationData limit 5;")
    print(cursor.fetchall)
    return cursor.fetchall()