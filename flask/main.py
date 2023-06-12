from src.config import FLASK_ENV
from flask import Flask, request, jsonify
from src.predict import PlantClassifier

app = Flask(__name__)
clf = PlantClassifier("model3.h5")

@app.route('/')
def home():
    return {"message": "Hi, this is TemanTanam"}

@app.route('/classify_base64', methods = ['POST'])
def classify_base64():
    pred = clf.predict_base64(request.json['image'])
    return jsonify({'result': pred})

@app.route('/classify_binary', methods=['POST'])
def classify_binary():
    pred = clf.predict_binary(request.files['image'])
    return jsonify({'result': pred})

if __name__ == '__main__':
    # debug = FLASK_ENV["FLASK_ENV"] == "DEV"
    # app.run(host = FLASK_ENV["HOST"], port = FLASK_ENV["PORT"], debug=debug)
    app.run(host='0.0.0.0', port=8080, debug=True)