from Cell import Cell
from Table import Table
from Box import Box
from OCR import GoogleVisionOCR
#asdddddf
class MarksheetTable(Table):
    def __init__(self, cols, rows, img, name: str,ocr = GoogleVisionOCR()) -> None:
        l=[]
        x=ocr.detectText(img)
        print(x)
        for i in x[1:]:
            b=Box(i['boundingPoly']['vertices'][0]['x'],i['boundingPoly']['vertices'][0]['x'],i['boundingPoly']['vertices'][2]['x'],i['boundingPoly']['vertices'][3]['x'],i['boundingPoly']['vertices'][0]['y'],i['boundingPoly']['vertices'][1]['y'],i['boundingPoly']['vertices'][2]['y'],i['boundingPoly']['vertices'][3]['y'])
            c=Cell(i['description'],b)
            l.append(c)
        super().__init__(cols, rows, *l, name=name)
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
                if (y1>=yt2 and y1<=yt3):
                    marks[q.getText()] = float(m.getText())
        return marks