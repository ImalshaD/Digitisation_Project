from flask import Blueprint, request, jsonify
from app import db
from ..Models import User
from ..DTO import StatusDTO
import os
ca_bp = Blueprint('ca',__name__)
#ca/uploadcsv
@ca_bp.route('/uploadcsv' , methods = ["PUT"])
def uploadcsv():
    try:
        if 'file' not in request.files:
            return jsonify(StatusDTO(404,"File Not Found").__dict__)
        data = request.get_json()
        module_year_id = data['module_year_id']
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
        jsonify(StatusDTO(404,str(e)).__dict__)


