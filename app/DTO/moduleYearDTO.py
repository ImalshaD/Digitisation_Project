class ModuleYearDTO:
    def __init__(self,module_year_id,year,caweights,finalweights,camax,finalmax,moderated,module_id) -> None:
        self.module_year_id = module_year_id
        self.year = year
        self.caweights = caweights
        self.finalweights = finalweights
        self.camax = camax
        self.finalmax = finalmax
        self.moderated = moderated
        self.module_id = module_id