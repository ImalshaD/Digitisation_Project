from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Module,ModuleYear
from ..DTO import ModulesDTO,ModuleYearDTO, StatusDTO,ModuleYearsDTO
moduleYear_bp = Blueprint('moduleYear',__name__)
#/moduleYear/addmoduleYear
@moduleYear_bp.route('/addmoduleYear', methods=['PUT'])
def addmoduleYear():
    msg=''
    c0de=404
    try:
        data = request.get_json()
        year = data['year']
        caweights = data['caweights']
        finalweights = data['finalweights']
        camax = data['camax']
        finalmax = data['finalmax']
        module_id = data['module_id']
        max_qs = data['max_qs']
        moduleYear = ModuleYear(year=year,caweights=caweights,finalweights=finalweights
                                ,camax=camax,finalmax=finalmax,module_id=module_id,max_qs=max_qs)
        db.session.add(moduleYear)
        db.session.commit()
        code=200
        msg="Module Year added"
    except Exception as e:
        code=404
        db.session.rollback()
        msg=str(e)
    finally:
        db.session.close()
        return jsonify(StatusDTO(code,msg).__dict__)
#/moduleYear/getmoduleYears
@moduleYear_bp.route('/getmoduleYears', methods=['POST'])
def getModuleYears():
    try:
        data = request.get_json()
        module_id = data['module_id']
        print(module_id)
        module = Module.query.filter_by(module_id=module_id).first()
        moduleYears=[]
        module_instance = module.module_years
        for year in module_instance:
            moduleYear = ModuleYearDTO(year.module_year_id,year.year,year.caweights,
                                        year.finalweights,year.camax,year.finalmax,year.moderated,year.module_id,year.max_qs)
            moduleYears.append(moduleYear.__dict__)
        return jsonify(ModuleYearsDTO(200,moduleYears).__dict__)
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify(ModuleYearsDTO(404).__dict__)