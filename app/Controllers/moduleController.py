from flask import Blueprint, request, jsonify
from app import db
from ..Models import User,Module,ModuleYear
from ..DTO import ModulesDTO,ModuleYearDTO, StatusDTO
module_bp = Blueprint('module',__name__)

#/module/getmodules
@module_bp.route('/getmodules', methods=['POST'])
def getmodules():
    try:
        data = request.get_json()
        user_name=data['user_name']
        user_instance = User.query.filter_by(user_name=user_name).first()
        modules=ModulesDTO(200,"Success")
        if user_instance:
            user_modules = user_instance.modules
            for module in user_modules:
                moduleYears=[]
                module_instance = module.module_years
                for year in module_instance:
                    moduleYear = ModuleYearDTO(year.module_year_id,year.year,year.caweights,
                                               year.finalweights,year.camax,year.finalmax,year.moderated,year.module_id)
                    moduleYears.append(moduleYear.__dict__)
                modules.addmodule(module.module_id,module.module_code,module.module_name,module.user_id,
                                        moduleYears 
                                     )
            return jsonify(modules.__dict__)
            
        else:
            return jsonify(ModulesDTO(404,"User not found").__dict__)
    except Exception as e:
        return jsonify(ModulesDTO(404, str(e)).__dict__)
#/module/addmodule
@module_bp.route('/addmodule', methods=['PUT'])
def addmodule():
    try:
        data = request.get_json()
        user_name=data['user_name']
        module_code = data['module_code']
        module_name = data['module_name']
        user_instance = User.query.filter_by(user_name=user_name).first()
        if user_instance:
            user_id = user_instance.user_id
            module = Module(module_code=module_code,module_name=module_name,
                            user_id=user_id)
            db.session.add(module)
            db.session.commit()
            return jsonify(StatusDTO(200,"Module added Successfully").__dict__)
        else:
            return jsonify(StatusDTO(404,"User Name not found"))
    except Exception as e:
        db.session.rollback()
        return jsonify(StatusDTO(404,str(e)).__dict__)
    finally:
        db.session.close()
    