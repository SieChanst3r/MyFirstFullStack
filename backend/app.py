import mariadb
from flask import Flask
from flask_cors import CORS
import json
import dbcreds

app = Flask(__name__)
CORS(app)

@app.route('/posts', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def posts():
    if request.method == 'GET':
        conn = None
        cursor = None
        posts = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts")
            cars = cursor.fetchall()
        except Exception as error:
            print("Something went wrong: ")        
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                 conn.rollback()
                 conn.close()
            if(cars != None):
                 return Response(json.dumps(posts, default=str), mimetype="application/json", status=200)
            else:
                 return Response("Something went wrong!", mimetype="text/html", status=500)
              