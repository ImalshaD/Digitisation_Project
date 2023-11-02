from Cell import Cell
from Table import Table
from Box import Box
from GoogelVisionOCR import GoogleVisionOCR
#asdddddf
##Comitt
class MarksheetTable(Table):
    def __init__(self, cols, rows, img, name: str,ocr = GoogleVisionOCR()) -> None:
        l=[]
        x=ocr.detectText(img)
        print(x)
        for i in x[1:]:
            b=Box(i.bounding_poly.vertices[0].x,i.bounding_poly.vertices[1].x,i.bounding_poly.vertices[2].x,i.bounding_poly.vertices[3].x,i.bounding_poly.vertices[0].y,i.bounding_poly.vertices[1].y,i.bounding_poly.vertices[2].y,i.bounding_poly.vertices[3].y)
            c=Cell(i.description,b)
            l.append(c)
        super().__init__(cols, rows, *l, name=name)
        self.__question=[]
        self.__marks=[]

    def mapping(self,x)->str:
        d={'a': ['4'],
            'b': ['8'],
            'c': ['6'],
            'd': ['9'],
            'e': ['3'],
            'f': ['7'],
            'g': ['9'],
            'h': ['4'],
            'i': ['1'],
            'j': ['1'],
            'k': ['8'],
            'l': ['1'],
            'm': ['3'],
            'o': ['0'],
            'p': ['9'],
            'q': ['9'],
            'r': ['1'],
            's': ['5'],
            't': ['7'],
            'u': ['0'],
            'v': ['7'],
            'w': ['7'],
            'x': ['2'],
            'y': ['5'],
            'z': ['2'],
            'A': ['4'],
            'B': ['8'],
            'C': ['6'],
            'D': ['0'],
            'E': ['3'],
            'F': ['7'],
            'G': ['9'],
            'H': ['4'],
            'I': ['7'],
            'J': ['1'],
            'K': ['8'],
            'L': ['1'],
            'M': ['3'],
            'N': ['5'],
            'O': ['0'],
            'P': ['9'],
            'Q': ['9'],
            'R': ['8'],
            'S': ['5'],
            'T': ['7'],
            'U': ['0'],
            'V': ['0'],
            'W': ['7'],
            'X': ['2'],
            'Y': ['5'],
            'Z': ['2']}
        y=''
        for i in x:
            if i.isdigit():
                y+=i
            elif(i in d):
                y+=d[i][0]
            else:
                y+='_'
        return y

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
                    marks[self.mapping(q.getText()) if len(q.getText())<=3 else q.getText()] = float(self.mapping(m.getText()))
        return marks