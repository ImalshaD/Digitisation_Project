from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Marks
from ..DTO import DsDTO
from ..DSAnalysis import MokDS
import os
ds_bp = Blueprint('ds',__name__)

mokds = MokDS()
#ds/getds
@ds_bp.route('/getds/<int:module_year_id>' , methods = ["GET"])
def getdsDistributions(module_year_id):
    ds = DsDTO(200,mokds.getQCount(),mokds.getGradecounts(),mokds.getlines(),mokds.getDistributuions(),mokds.getBoxPlot())
    return jsonify(ds.__dict__)
@ds_bp.route('/getpie/<int:module_year_id>' , methods = ["GET"])
def getdsPie(module_year_id):
    return jsonify({"statusCode": 200,'data': mokds.getQCount()})
@ds_bp.route('/getbar/<int:module_year_id>' , methods = ["GET"])
def getdsbar(module_year_id):
    return jsonify({"statusCode": 200,'data': mokds.getGradecounts()})
@ds_bp.route('/getline/<int:module_year_id>' , methods = ["GET"])
def getdsline(module_year_id):
    return jsonify({"statusCode": 200,'data': mokds.getlines()})
@ds_bp.route('/getdist/<int:module_year_id>' , methods = ["GET"])
def getdsdist(module_year_id):
    return jsonify({"statusCode": 200,'data': mokds.getDistributuions()})
@ds_bp.route('/getbox/<int:module_year_id>' , methods = ["GET"])
def getdsbox(module_year_id):
    return jsonify({"statusCode": 200,'data': mokds.getBoxPlot()})
@ds_bp.route('/getMarks/<int:module_year_id>' , methods = ["GET"])
def getMarks(module_year_id):
    try:
        # Query the Marks table for all records with the specified module_year_id
        marks = Marks.query.filter_by(module_year_id=module_year_id).all()

        # Convert the query results to a list of dictionaries for JSON response
        marks_list = [
            {
                'index_number': mark.index_number,
                'q1': mark.q1,
                'q2': mark.q2,
                'q3': mark.q3,
                'q4': mark.q4,
                'q5': mark.q5,
                'q6': mark.q6,
                'q7': mark.q7,
                'q8': mark.q8,
                'q9': mark.q9,
                'q10': mark.q10,
                'q11': mark.q11,
                'q12': mark.q12,
                'total': mark.total,
                'camarks': mark.camarks,
                'final': mark.final,
                'moderated_final': mark.moderated_final,

                # ... include other columns as needed
            }
            for mark in marks
        ]

        return jsonify({'statusCode': 200,'marks': marks_list})

    except Exception as e:
        return jsonify({'statusCode': 404 ,'marks': str(e)})