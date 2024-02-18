from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as con

mydb = con.connect(host="localhost", user="root", password="mom@dad", database="khush")
cur = mydb.cursor()

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def hello():
    return "Welcome to the page!"

@app.route('/select_frist', methods=["POST"])
def select():
    request_data = request.get_json()
    bname = request_data['namek']

    cur.execute("SELECT * FROM online where na=%s", (bname,))
    data = cur.fetchall()  

    result = []
    for row in data:
        # Assuming the first column is 'id' and the second column is 'name'
        result.append({"id": row[0], "name": row[1]})  # Adjust column indexes accordingly

    return jsonify({"data": result})

    return jsonify(data)

@app.route('/insert-data', methods=['POST'])
def insert_data():
    request_data = request.get_json()
    bname = request_data['namek']
    bsurname = request_data['surnamek']
    cur.execute("INSERT INTO online (num,na) VALUES (%s, %s)", (bname, bsurname))
    mydb.commit()

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
