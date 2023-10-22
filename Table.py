from Cell import Cell

class Table:
    def __init__(self,cols,rows,*cells: Cell,name:str) -> None:
        self.__name = name
        self.__cells = cells
        self.__cellCount = len(cells)
        self.__rows=rows
        self.__cols = cols
        self.__sumWidth=0
        self.__sumHeight = 0
        for cell in self.__cells:
            sellheight,sellwidth = cell.getWidthAndHeight()
            self.__sumHeight+=sellheight
            self.__sumHeight+=sellwidth
    def getMeanWidthandHeight(self)->list:
        return [self.__sumHeight/self.__cellCount,self.__sumWidth/self.__cellCount]