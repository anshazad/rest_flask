import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    response=""
    a=int(jsonObj['A'])
    if len(str(a))!=3:
        response+="<b> Enter 3 digit number only </b><br>"  
    arm=0
    b=a
    while b>0:
        arm=arm + (b%10)**3
        b=b//10
    if arm==a:
        response+="<b> Yes it is an armstrong number </b><br>"
    else:
        response+= "<b> No it is not an armstrong number </b>"
        
    return response


if __name__ == "__main__":
    app.run(debug=True)   


