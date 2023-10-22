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
            x2,y2 = q.getC2Cordinates()
            x3,y3 = q.getC3Cordinates()
            thresh = super().__xThreshold
            xt2 = x2+thresh
            xt3 = x3-thresh
            for m in marsk:
                x1 = m.getC1Cordinates()
                x4 = m.getC4Cordinates()
                if (x1<xt2 and x1>xt3) and (x4<xt2 and x4>xt3):
                    marks[int(q.getText())] = float(q.getText())
                else:
                    marks[int(q.getText())] = None
        return marks