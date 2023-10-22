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
        self.__xThreshold = (self.__sumWidth/self.__cellCount)
        self.__yThreshold = (self.__sumHeight/self.__cellCount)

    def getMeanWidthandHeight(self)->list:
        return [self.__sumHeight/self.__cellCount,self.__sumWidth/self.__cellCount]
    
    def getThreshold(self)->list:
        return [self.__xThreshold,self.__yThreshold]
    
    def getColumns(self)-> list:
        columns = [[],[]]
        col1=False
        col2=False
        for i in (self.__cells):
            if(i.getText()=="Question"):
                col1=True
            elif(i.getText()=="Marks" and col1==True):
                col2=True
            elif(col1==True and col2==False):
                columns[0].append(i)
            elif(col1==True and col2==True):
                columns[1].append(i)
        return columns   
    def getYThreshold(self)->float:
        return self.__yThreshold

    
