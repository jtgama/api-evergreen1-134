from flask import Flask, jsonify, request
from flask_cors import CORS
from api.controllers.participantesp import participantesp

app = Flask(__name__)
CORS(app)

@app.route('/participant', methods = ['GET'])
def getAll():
    return (participantesp.list())

@app.route('/participant', methods = ['POST'])
def postOne():
    body = request.json
    return (participantesp.create(body))

app.run(port=3000,debug=True)