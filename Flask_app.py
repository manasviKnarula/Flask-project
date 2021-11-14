from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Manasvi',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Sukirti',
        'Contact': u'9876543222', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please enter the info"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', " "),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "The contact was added"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)