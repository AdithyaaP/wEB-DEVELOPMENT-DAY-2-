from flask import Flask,jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    data =[{
        "name": "John"
        "link": "https://media.giphy.com/media/MSCmj0qsPPTDq/giphy.gif"
    }]
return jsonify(data)

