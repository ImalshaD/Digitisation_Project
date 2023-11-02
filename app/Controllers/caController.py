from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Marks
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
            list1=[]
            with open(file_path) as f:
                for lines in f:
                    list1.append(lines.strip().split(','))
            for index_num,marks in list1[1:]:
                marks=float(marks)
                code,msg=update_or_create_marks(index_num,module_year_id,marks)
                if code:
                    return jsonify(StatusDTO(404,msg).__dict__)
            return jsonify(StatusDTO(200,"File Uploaded Successful").__dict__)
        else:
            return jsonify(StatusDTO(404,"No file selected").__dict__)
    except Exception as e:
        return jsonify(StatusDTO(404,str(e)).__dict__)
def update_or_create_marks(index_number, module_year_id,camarks):

    try:
        # Check if a record with the given index_number and module_year_id exists
        existing_marks = Marks.query.filter_by(index_number=index_number, module_year_id=module_year_id).first()

        if existing_marks:
            existing_marks.camarks = camarks
        else:
            # Create a new record
            new_marks = Marks(
                index_number=index_number,
                module_year_id=module_year_id,
                camarks=camarks,
            )
            db.session.add(new_marks)

        db.session.commit()
        code=0
        msg="Success!"
    except Exception as e:
        db.session.rollback()
        code=1
        msg=str(e)
    finally:
        db.session.close()
        return code,msg


