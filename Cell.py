from Box import Box
class Cell:
    # cell loactions of GoogleOCR
    #    1--------------2
    #    |              |
    #    |              |
    #    4--------------3     
    def __init__(self,text:str,box : Box) -> None:
        self.__text = text
        self.__box = box
    
    def getText(self) -> str:
        return self.__text
    def getWidthAndHeight(self)->list:
        return [self.__box.getHeight(),self.__box.getWidth()]
    def getC1Cordinates(self)->list:
        return [self.__box.getx1(),self.__box.gety1()]
    def getC2Cordinates(self)->list:
        return [self.__box.getx2(),self.__box.gety2()]
    def getC3Cordinates(self)->list:
        return [self.__box.getx3(),self.__box.gety3()]
    def getC4Cordinates(self)->list:
        return [self.__box.getx4(),self.__box.gety4()]