from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Module,ModuleYear,Marks
from ..DTO import ModulesDTO,ModuleYearDTO, StatusDTO,ModuleYearsDTO,MarksDTO
import os
from PIL import Image
from io import BytesIO
import base64
import cv2
from ..layoutDetection import DetectLayout
from ultralytics import YOLO
model = YOLO(r'app\layoutDetection\best.pt','v8')
marksheet_bp = Blueprint('markSheet',__name__)

#/marksheet/upload
@marksheet_bp.route('/upload/<int:module_year_id>', methods=['POST'])
def uploadImage(module_year_id):
    if 'image' in request.files:
        image = request.files['image']
        # Process the image as needed (e.g., save to server, perform analysis, etc.)
        image.save(r"app\resources\Temp\\"+"image2.jpeg")
        img=cv2.imread(r"app\resources\Temp\\"+"image2.jpeg")
        x = DetectLayout(img,model)
        index = x.getIndex()
        marksdict = x.getMarks()
        print(index,marksdict)
        markslist = map(marksdict)  
        marks = MarksDTO(200,index,module_year_id,
                         markslist[0],
                         markslist[1],
                         markslist[2],
                         markslist[3],
                         markslist[4],
                         markslist[5],
                         markslist[6],
                         markslist[7],
                         markslist[8],
                         markslist[9],
                         markslist[10],
                         markslist[11],
                         markslist[12],
                         "",
                         "",
                         "")
        return jsonify(marks.__dict__)
    else:
        marks = MarksDTO(404,'200487B',1,10,11,12,13,14,15,16,17,18,19,12,11,11,23,100,78)
        return jsonify(marks.__dict__)
#/marksheet/uploadjson
@marksheet_bp.route('/uploadjson', methods=['PUT'])
def upload_image():
    data = request.get_json()
    try:
        if 'image' in data:
            print('xx')
            # Decode the base64-encoded image data
            image_data = base64.b64decode(data['image'])
            
            # Process the image as needed (e.g., save to server, perform analysis, etc.)
            image = Image.open(BytesIO(image_data))
            image.save(r"app\resources\Temp\\" + "uploaded_image.jpg")

            # Respond with a success message or any other relevant information
            marks = MarksDTO(200, '200487B', 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 12, 11, 11, 23, 100, 78)
            return jsonify(marks.__dict__)
        else:
            marks = MarksDTO(404, '200487B', 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 12, 11, 11, 23, 100, 78)
            return jsonify(marks.__dict__)

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
@marksheet_bp.route('/confirm', methods=['PUT'])
def confirm():
    try:
        data2 = request.get_json()
        data1=data2['data']
        data=dict()
        for i,j in data1:
             data[i]=j
        print(data)
        module_year_id = data['module_year_id']
        index_number = data['index_number']
        record = Marks.query.filter_by(index_number=index_number, module_year_id=module_year_id).first()
        q1 = backwordmap(data['q1'])
        q2 = backwordmap(data['q2'])
        q3 = backwordmap(data['q3'])
        q4 = backwordmap(data['q4'])
        q5 = backwordmap(data['q5'])
        q6 = backwordmap(data['q6'])
        q7 = backwordmap(data['q7'])
        q8 = backwordmap(data['q8'])
        q9 = backwordmap(data['q9'])
        q10 = backwordmap(data['q10'])
        q11 = backwordmap(data['q11'])
        q12 = backwordmap(data['q12'])
        total = backwordmap(data['total'])
        camarks = backwordmap(data['camarks'])
        final = backwordmap(data['final'])
        moderated_final = backwordmap(data["moderated_final"])
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
            msg ="Database updated SuccessFull"
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
            msg ="Database new record added SuccessFull"
        db.session.add(record)
        db.session.commit()
        print(index_number,"Added or updated to database successfully!")
        code=200
    except Exception as e:
        # Rollback in case of an error and return an error response
        db.session.rollback()
        code=404
        msg=str(e)
        print(msg)
    finally:
        # Close the database session
        db.session.close()
        return jsonify(StatusDTO(code,msg).__dict__)
def map(marksdict):
    if '1' in marksdict:
            q1=marksdict['1']
    else:
        q1=None
    if '2' in marksdict:
        q2 =marksdict['2']
    else:
        q2=None
    if '3' in marksdict:
            q3=marksdict['3']
    else:
        q3=None
    if '4' in marksdict:
        q4 =marksdict['4']
    else:
        q4=None
    if '5' in marksdict:
            q5=marksdict['5']
    else:
        q5=None
    if '6' in marksdict:
        q6 =marksdict['6']
    else:
        q6=None
    if '7' in marksdict:
            q7=marksdict['7']
    else:
        q7=None
    if '8' in marksdict:
        q8 =marksdict['8']
    else:
        q8=None
    if '9' in marksdict:
            q9=marksdict['9']
    else:
        q9=None
    if '10' in marksdict:
        q10 =marksdict['10']
    else:
        q10=None
    if '11' in marksdict:
            q11=marksdict['11']
    else:
        q11=None
    if '12' in marksdict:
        q12 =marksdict['12']
    else:
        q12=None
    if "Total" in marksdict:
        total = marksdict["Total"]
    else:
        total = None
    return [forwardmap(q1),forwardmap(q2),forwardmap(q3),forwardmap(q4),forwardmap(q5),
            forwardmap(q6),forwardmap(q7),forwardmap(q8),forwardmap(q9),forwardmap(q10),forwardmap(q11),forwardmap(q12),
            forwardmap(total)]
def forwardmap(val):
    if val:
        return val
    else:
         return ""
def backwordmap(val):
    if val=="":
        return None
    else:
        return val
         