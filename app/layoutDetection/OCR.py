import os
import base64
from google.protobuf.json_format import MessageToJson
from google.cloud import vision
import numpy as np
import cv2
import requests  # Add the requests module for making HTTP requests

class GoogleVisionOCR:
    def __init__(self, api_key: str ="AIzaSyDkXzKDQp5BB6FBYOFJlcb_4sX_by2S5Ls") -> None:
        self.api_key = api_key

    def detectText(self, img: np.array):
        # Convert the image to a byte array
        _, img_encoded = cv2.imencode('.jpg', img)
        img_bytes = img_encoded.tobytes()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')

        # Pass the byte array to the vision.Image constructor
        image = vision.Image(content=img_base64)

        # Construct the Vision API request URL with the API key
        vision_api_url = f"https://vision.googleapis.com/v1/images:annotate?key={self.api_key}"

        # Make the Vision API request
        response = requests.post(
            vision_api_url,
            json={
                "requests": [
                    {
                        "image": {
                            "content": img_base64
                        },
                        "features": [
                            {"type": "TEXT_DETECTION"}
                        ]
                    }
                ]
            }
        )

        # Check the response status and process the result
        if response.status_code == 200:
            result = response.json()
            # Extract the text annotations from the result
            text_annotations = result.get("responses", [])[0].get("textAnnotations", [])
            return text_annotations
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None