import os
import psycopg2

DATABASE_NAME = os.getenv("DATABASE_NAME", "teste")
DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
DATABASE_PWD = os.getenv("DATABASE_PWD", "Postgres2018!")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost") 

def on_starting(server):  
    conn = psycopg2.connect(
        dbname = DATABASE_NAME, 
        user = DATABASE_USER, 
        password = DATABASE_PWD, 
        host = DATABASE_HOST, 
        port = DATABASE_PORT
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS teste ( id serial PRIMARY KEY,	nome VARCHAR ( 100 ) NOT NULL)")
    conn.commit()