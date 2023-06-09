from flask import Flask, request, jsonify
from PIL import Image
from keras.models import load_model
from werkzeug.utils import secure_filename
import os
import numpy as np
import base64
import werkzeug

app = Flask(__name__)

#ini sementara modelnya pake Inception
model = load_model('model.h5')
classes = np.loadtxt('labels.txt', delimiter=',', dtype=str)

def model_predict (file_path, model):
    image = image.resize((150, 150))
    image_array = np.array(image.convert('RGB')) / 255.0
    expand_input = np.expand_dims(image_array,axis=0)
    prediction = model.predict(expand_input)
    index = np.argmax(prediction)
    return str(classes[index])

def decodeImage(image_string, file_name):
    image_data = base64.b64decode(image_string)
    with open(file_name, 'wb') as f:
        f.write(image_data)
        f.close()

@app.route('/classify', methods = ['GET', 'POST'])
def classify():
    if request.method == 'POST':
        # Get the json file from the request
        image_file = request.json['image']
        # Read the image file
        image = Image.open(image_file)
        # Constructing file path
        filename = werkzeug.utils.secure_filename(image_file.filename)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', filename)
        # Saving image temporarily in "upload" folder
        image_file.save(file_path)
        decodeImage(image_file['data'], file_path)
        #the image is ready to get predicted
        result = model_predict(file_path, model)
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)