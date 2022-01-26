import os
import psycopg2
from flask import Flask, jsonify, request
#import urlparse
from os.path import exists
from os import makedirs

'''
url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
schema = "schema.sql"
conn = psycopg2.connect(db)
'''

'''
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
'''
# docker run --name teste-postgres --network=postgres-network -e "POSTGRES_PASSWORD=Postgres2018!" -p 5432:5432 -v /home/renatogroffe/Desenvolvimento/PostgreSQL:/var/lib/postgresql/data -d postgres
# docker run --name postgres -e "POSTGRES_PASSWORD=Postgres2018!" -p 5432:5432 -d postgres
#172.17.0.2

DATABASE_NAME = os.getenv("DATABASE_NAME", "teste")
DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
DATABASE_PWD = os.getenv("DATABASE_PWD", "Postgres2018!")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost") 

conn = psycopg2.connect(
    dbname = DATABASE_NAME, 
    user = DATABASE_USER, 
    password = DATABASE_PWD, 
    host = DATABASE_HOST, 
    port = DATABASE_PORT
)
#conn = psycopg2.connect(dbname="postgres", user="postgres", password="Postgres2018!", host="172.17.0.2", port="5432")
cursor = conn.cursor()


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá = ' + DATABASE_HOST

@app.route('/lista',methods = ['GET'])
def lista():
    try:
        cursor.execute("""SELECT id, nome from teste""")
        rows = cursor.fetchall()
        #cursor.close()
        #conn.close()
        return jsonify({
            "resultado": rows,
        })
    except Exception as e:
        return jsonify({
            "erro": e,
        })


@app.route('/grava',methods = ['POST'])
def grava():
    try:
        nome = request.form['nome']
        cursor.execute("INSERT INTO teste (nome) VALUES(%s)", (f'${nome}', ))
        conn.commit()
        #cursor.close()
        #conn.close()
        return jsonify({
            "resultado": "gravado com sucesso",
        })
    except Exception as e:
        return jsonify({
            "erro": e,
        })

if __name__ == '__main__':
    app.run(debug=True)