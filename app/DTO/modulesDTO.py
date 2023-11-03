class ModulesDTO:
    def __init__(self,statusCode,msg) -> None:
        self.statusCode = statusCode
        self.msg=msg
        self.modules=[]
    def addmodule(self,module_id,module_code,module_name,user_id,module_years):
        module=dict()
        module["module_id"]=module_id
        module["module_code"]=module_code
        module["module_name"]=module_name
        module["module_years"]=module_years
        module["user_id"]=user_id
        self.modules.append(module)
