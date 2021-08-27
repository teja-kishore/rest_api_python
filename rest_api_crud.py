from flask import Flask,jsonify,request
app = Flask(__name__)
studentdetails = [{'name':"Teja Kishore","email" : "ytkishore7@gmail.com","id" : 1}]
@app.route("/",methods = ["GET"])
def home():
    return ("Welcome")

@app.route("/details", methods = ["GET"])
def readAll():
    return jsonify ({"studentdetails" : studentdetails})
@app.route("/details/<string:name>", methods = ["GET"])
def readOne(name):
    det = [details for details in studentdetails if details['name'] == name]
    return jsonify ({"studentdetails" : det[0]})

@app.route("/details", methods = ["POST"])
def add():
    details = {"name" : request.json['name'], "id" : request.json[id], "email" : request.json['email']}
    studentdetails.append(details)
    return jsonify({"studentdetails" : studentdetails})

@app.route("/details/<string:name>", methods = ["PUT"])
def update(name):
    det = [details for details in studentdetails if studentdetails["name"] == name]
    det[0]["name"] = request.json['name']
    return jsonify ({"studentdetails" : det[0]})

@app.route ("details/<string:name>", methods = ["DELETE"])
def delete(name):
    det = [details for details in studentdetails if studentdetails["name"]==name]
    studentdetails.remove(det[0])
    return jsonify({"studentdetails" : studentdetails}) 

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port ="3000")
