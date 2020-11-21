import mariadb
from flask import Flask, request, Response
from flask_cors import CORS
import json
import dbcreds

app = Flask(__name__)
CORS(app)

@app.route('/api/posts', methods=['GET', 'POST', 'PATCH', 'DELETE'])
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
            if(posts != None):
                 return Response(json.dumps(posts, default=str), mimetype="application/json", status=200)
            else:
                 return Response("Something went wrong!", mimetype="text/html", status=500)
    elif request.method == 'POST':
        conn = None
        cursor = None 
        posts_content = request.json.get('content')
        posts_name = request.json.get('name')
        posts_created = request.json.get('created')
        row = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts(content, name, created) VALUES(?, ?, ?)", [posts_content, posts_name, posts_created])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong (THIS IS LAZY): ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                 conn.rollback()
                 conn.close()
            if(rows == 1):
                return Response("Post created! ", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)
    elif request.method == 'PATCH':
        conn = None
        cursor = None 
        posts_content = request.json.get('content')
        posts_name = request.json.get('name')
        posts_created = request.json.get('created')
        posts_id = request.json.get('id')
        row = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if posts_content != "" and posts_content != None:
                cursor.execute("UPDATE posts SET name=? WHERE id=?", [posts_content, posts_id])
            if posts_name != "" and posts_name != None:
                cursor.execute("UPDATE posts SET description=? WHERE id=?", [posts_name, posts_id])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong (THIS IS LAZY!)")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Updated successfully", mimetype="text/html", status=204)
            else: 
                return Response("Update failed", mimetype="text/html", status=500)
    elif request.method == 'DELETE':
        conn = None
        cursor = None  
        posts_id = request.json.get('id')
        rows = None                  
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM posts WHERE id=?", [posts_id,])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong (THIS IS LAZY!)")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Deleted successfully", mimetype="text/html", status=204)
            else: 
                return Response("Delete failed", mimetype="text/html", status=500)