from flask import Blueprint, request, jsonify
from app import db
from ..Models import User
from ..DTO import StatusDTO
import os
ca_bp = Blueprint('ca',__name__)
#ca/uploadcsv
@ca_bp.route('/uploadcsv/<int:module_year_id>' , methods = ["PUT"])
def uploadcsv(module_year_id):
    try:
        if 'file' not in request.files:
            return jsonify(StatusDTO(404,"File Not Found").__dict__)
        file = request.files['file']

        if file.filename == '':
            return jsonify(StatusDTO(404,"No file selected").__dict__)

        if file:
            # Ensure the 'uploads' folder exists
            # Save the file to the 'uploads' folder
            file_path = os.path.join(r'app\resources\CSV',"temp.csv")
            file.save(file_path)
            return jsonify(StatusDTO(404,"File Uploaded Successful").__dict__)
        else:
            return jsonify(StatusDTO(404,"No file selected").__dict__)
    except Exception as e:
        return jsonify(StatusDTO(404,str(e)).__dict__)


