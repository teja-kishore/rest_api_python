from flask import Flask,jsonify, request
app = Flask(__name__)
Student_Details = [{'name': "Teja kishore",'id':"N151127"}]
@app.route('/')
def index():
    return "Welcome"
@app.route('/Student_Details',methods=['GET'])
def get():
    return jsonify({'Student_Details':Student_Details})

@app.route("/Student_Details",methods=['POST'])
def create():
    Student_Details = {'name':"V.Y.T.Kishore",'id':"n151127"}
    Student_Details.append(Student_Details)
    return jsonify({'Created':Student_Details})
@app.route("/Student_Details/<str:id>",methods=['PUT'])
def details_update(id):
    Student_Details['id']['name']="Vemavarapu Yamuna Teja Kishore"
    return jsonify({'Student_Details'})
if __name__ == "__main__":
    app.run(debug=True)

