from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Module,ModuleYear,Marks
from ..DTO import ModulesDTO,ModuleYearDTO, StatusDTO,ModuleYearsDTO,MarksDTO
import os

marksheet_bp = Blueprint('markSheet',__name__)

#/marksheet/upload
@marksheet_bp.route('/upload', methods=['PUT'])
def uploadImage():
    if 'image' in request.files:
        image = request.files['image']
        # Process the image as needed (e.g., save to server, perform analysis, etc.)
        image.save(r"app\resources\Temp\\"+image.filename)
        marks = MarksDTO(200,'200487B',1,10,11,12,13,14,15,16,17,18,19,12,11,11,23,100,78)
        return jsonify(marks.__dict__)
    else:
        marks = MarksDTO(404,'200487B',1,10,11,12,13,14,15,16,17,18,19,12,11,11,23,100,78)
        return jsonify(marks.__dict__)
@marksheet_bp.route('/upload', methods=['PUT'])
def confirm():
    try:
        data = request.get_json()
        module_year_id = data['module_year_id']
        index_number = data['index_number']
        record = Marks.query.filter_by(index_number=index_number, module_year_id=module_year_id).first()
        q1 = data['q1']
        q2 = data['q2']
        q3 = data['q3']
        q4 = data['q4']
        q5 = data['q5']
        q6 = data['q6']
        q7 = data['q7']
        q8 = data['q8']
        q9 = data['q9']
        q10 = data['q10']
        q11 = data['q11']
        q12 = data['q12']
        total = data['total']
        camarks = data['camarks']
        final = data['final']
        moderated_final = data["moderated_final"]
        if record:
        # Update existing record
            record.q1 = q1
            record.q2 = q2
            record.q3 = q3
            record.q4 = q4
            record.q5 = q5
            record.q6 = q6
            record.q7 = q7
            record.q8 = q8
            record.q9 = q9
            record.q10 = q10
            record.q11 = q11
            record.q12 = q12
            record.total = total
            record.camarks = camarks
            record.final = final
            record.moderated_final = moderated_final
        else:
        # Create new record
            record = Marks(
                index_number=index_number,
                module_year_id=module_year_id,
                q1=q1,
                q2=q2,
                q3=q3,
                q4=q4,
                q5=q5,
                q6=q6,
                q7=q7,
                q8=q8,
                q9=q9,
                q10=q10,
                q11=q11,
                q12=q12,
                total=total,
                camarks=camarks,
                final=final,
                moderated_final=moderated_final
            )
            db.session.add(record)
            db.session.commit()
        statusCode=200
        msg ="Database Update SuccessFull"
    except Exception as e:
        # Rollback in case of an error and return an error response
        db.session.rollback()
        code=404
        msg=str(e)
    finally:
        # Close the database session
        db.session.close()
        return jsonify(StatusDTO(code,msg).__dict__)
