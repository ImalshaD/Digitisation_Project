from flask import Blueprint, request, jsonify
from app import db
from ..Models import User
from ..DTO import StatusDTO
import os
ca_bp = Blueprint('ca',__name__)

@ca_bp.route('/' , methods = ["POST"])
def uploadcsv():
    try:
        if 'file' not in request.files:
            return jsonify(StatusDTO(404,"File Not Found").__dict__)

        file = request.files['file']

        if file.filename == '':
            return jsonify(StatusDTO(404,"No file selected"))

        if file:
            # Ensure the 'uploads' folder exists
            # Save the file to the 'uploads' folder
            file_path = os.path.join(r'app\resources\CSV',"temp.csv")
            file.save(file_path)
            return jsonify(StatusDTO(404,"File Uploaded Successful"))
        else:
            return jsonify(StatusDTO(404,"No file selected"))
    except Exception as e:
        jsonify(StatusDTO(404,str(e)))


