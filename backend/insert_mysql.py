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

#user data store
@app.route('/insert-data', methods=['POST'])
def insert_data():
    request_data = request.get_json()
    frist= request_data['firstk']
    last = request_data['lastk']
    email=request_data['emailk']
    gender=request_data['genderk']
    dob=request_data['dobk']
    mobile=request_data['mobilek']
    cur.execute("INSERT INTO users_information(FristName,LastName,Email,Gender,Dateofbrith,Contact) VALUES (%s, %s,%s,%s,%s, %s)", (frist,last,email,gender,dob,mobile))
    mydb.commit()
    #todo make return statement universal for every api 
    #formamt=> {"status":200,"msg":"your msg","data":[]}
    #status=>success=200,error=>500
    return jsonify({"status": "success"})
# payment 
@app.route('/payment', methods=['POST'])
def pay():
    request_data = request.get_json()
    cardnum= request_data['cardNumberk']
    cardhold=request_data['cardHolderNamek']
    expire=request_data['expireDatek']
    ccv=request_data['ccvk']
    amount=request_data['amountk']

    cur.execute("INSERT INTO payment(Card_number,Card_holdername,Expiration_Date,CCV,amount) VALUES (%s, %s,%s,%s,%s)",(cardnum,cardhold,expire,ccv,amount))
    mydb.commit()

    return jsonify({"status": "success"})
# admin login
@app.route('/login', methods=['POST'])
def log():
    request_data = request.get_json()
    name= request_data['namek']
    passw=request_data['passk']
    print(name)
    cur.execute("select * from admin_table where UserName=%s and Password= %s",(name,passw))
    data = cur.fetchall()
    if(len(data)>0):
         return jsonify({"status":200,"msg": "success",f"data":[data]})
    else:
         return jsonify({"status":500,"msg": "fail",f"data":[data]})


    # result = []
    # for row in data:
    #     # Assuming the first column is 'id' and the second column is 'name'
    #     result.append({"id": row[0], "name": row[1]})  # Adjust column indexes accordingly
    
    # print(result)
    # return jsonify({"data": result})


if __name__ == "__main__":
    app.run(debug=True)
print("khush")