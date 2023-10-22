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
    
    