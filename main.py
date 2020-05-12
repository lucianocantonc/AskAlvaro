from google.cloud import firestore
from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
import os

db = firestore.Client()
app = Flask(__name__)
CORS(app, resources={r"": {"origins": ""}})

@app.route('/register', methods=['POST'])
def input():
    data = request.get_json()

    db.collection('questions').add(data)
   

    
    response = {
        'message' : 'valeu!!',
    }

    return jsonify(response), 200

@app.route('/index', methods=['GET'])
def showusers():  
    docs = db.collection('questions').get()
    
    question = []
    for doc in docs:
        
        question.append(doc.to_dict())
        
    return jsonify(question), 200         
  
        
          

if __name__ == '__main__':
    if os.environ.get('GAE_ENV') != 'standard':
        app.run(host='127.0.0.1', port=8080, debug=True)