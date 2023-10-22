from Cell import Cell
from Table import Table

class MarksheetTable(Table):
    def __init__(self, cols, rows, *cells: Cell, name: str) -> None:
        super().__init__(cols, rows, *cells, name=name)
        self.__question=[]
        self.__marks=[]
    def getMarks(self)->dict:
        marks=dict()
        qs,marsk = super().getColumns()
        for q in qs:
            marks[q.getText()]=None
            x2,y2 = q.getC2Cordinates()
            x3,y3 = q.getC3Cordinates()
            thresh = super().getYThreshold()
            yt2 = y2-thresh
            yt3 = y3+thresh
            for m in marsk:
                x1 ,y1= m.getC1Cordinates()
                print(q.getText(),m.getText(),y1,yt2,yt3)
                if (y1>=yt2 and y1<=yt3):
                    marks[q.getText()] = float(m.getText())
        return marks