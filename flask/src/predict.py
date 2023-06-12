import io, re, base64
import numpy as np

from PIL import Image

from keras.models import load_model
from model.labels import LABELS

class PlantClassifier:
    def __init__ (self, model_path):
        self.model = load_model(model_path)
        self.classes = LABELS
    
    def predict_base64 (self, image_str):
        image = self.decode_base64(image_str)
        return self.predict(image)
    
    def predict_binary(self, image_str):
        image = self.decode_binary(image_str)
        return self.predict(image)   
    
    def predict (self, image):
        image = self.preprocess(image)
        pred = self.model.predict(image)
        label = self.classes[pred.argmax()]
        return label
    
    @staticmethod
    def decode_base64(image_str):
        image_str = re.sub('^data:image/.+;base64,', '', image_str)
        decode_image = base64.b64decode(image_str)
        image_buffer = io.BytesIO(decode_image)
        return Image.open(image_buffer)
    
    @staticmethod
    def decode_binary(image_binary):
        return Image.open(image_binary)

    @staticmethod
    def preprocess(pil_image):
         pil_image = pil_image.resize((150, 150)).convert('RGB')
         image = np.array(pil_image) / 255.0
         return image[None, ...]
    
    