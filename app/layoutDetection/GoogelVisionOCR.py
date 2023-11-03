import os
import base64
from google.protobuf.json_format import MessageToJson
from google.cloud import vision
from google.oauth2 import service_account
import numpy as np
import cv2
class GoogleVisionOCR:
    def __init__(self,accessTokenPath:str = "digitization-pro-db817cdea63f.json") -> None:
        self.accessToken = accessTokenPath
        self.credentials = service_account.Credentials.from_service_account_file(self.accessToken)
        self.client = vision.ImageAnnotatorClient(credentials=self.credentials)
    def detectText(self,img : np.array):
        # Convert the image to a byte array
        _, img_encoded = cv2.imencode('.jpg', img)
        img_bytes = img_encoded.tobytes()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')

        # Pass the byte array to the vision.Image constructor
        image = vision.Image(content=img_base64)
        response = self.client.text_detection(image=image)
        return response.text_annotations
