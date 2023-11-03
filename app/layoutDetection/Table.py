from .Cell import Cell
from .CustomSorter import CustomSorter
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
        self.__yThreshold = (self.__sumHeight/self.__cellCount)/2

    def getMeanWidthandHeight(self)->list:
        return [self.__sumHeight/self.__cellCount,self.__sumWidth/self.__cellCount]
    
    def getThreshold(self)->list:
        return [self.__xThreshold,self.__yThreshold]
    
    def sort(self):
        self.__cells = CustomSorter.sortByYandX(self.__cells)

    def sortCol(self,col)->list:
        sortCol = CustomSorter.sortByXandY(col)
        return sortCol
    
    def sortByY(self):
        self.__cells = CustomSorter.sortByY(self.__cells)

    def getColumns(self)-> list:
        columns = [[],[]]
        self.sortByY()
        x1,y1=self.__cells[8].getC1Cordinates()
        x2,y2=self.__cells[8].getC2Cordinates()
        x3,y3=self.__cells[8].getC3Cordinates()
        x4,y4=self.__cells[8].getC4Cordinates()
        ref=(x1+x2+x3+x4)/4
        # print(self.__cells[8].getC1Cordinates(),self.__cells[8].getC2Cordinates(),self.__cells[8].getC3Cordinates(),self.__cells[8].getC4Cordinates())
        for i in (self.__cells[8:]):
            w,h=i.getWidthAndHeight()
            x1,y1=i.getC1Cordinates()
            x2,y2=i.getC2Cordinates()
            x3,y3=i.getC3Cordinates()
            x4,y4=i.getC4Cordinates()
            meanX=(x1+x2+x3+x4)/4
            # print(meanX,ref,w,i.getText())
            print(meanX,ref+w/4,i.getText())
            if(meanX>100):
                columns[1].append(i)
            else:
                columns[0].append(i)
        # print(columns)
        return columns   
    
    def getYThreshold(self)->float:
        return self.__yThreshold

    
