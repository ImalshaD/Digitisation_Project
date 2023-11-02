from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Module,ModuleYear
from ..DTO import ModulesDTO,ModuleYearDTO, StatusDTO,ModuleYearsDTO
import os

marksheet_bp = Blueprint('markSheet',__name__)

#/marksheet/upload
@marksheet_bp.route('/upload', methods=['PUT'])
def uploadImage():
    if 'image' in request.files:
        image = request.files['image']
        # Process the image as needed (e.g., save to server, perform analysis, etc.)
        image.save(r"app\resources\Temp\\"+image.filename)
        return jsonify(StatusDTO(200,"Image Uploaded Successfully").__dict__)
    else:
        return jsonify(StatusDTO(404,"Image Uploaded Failed").__dict__)
