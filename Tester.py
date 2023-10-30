from MarksheetTable import MarksheetTable
from Table import Table
from Cell import Cell
from Box import Box

from GoogelVisionOCR import GoogleVisionOCR
import cv2
ocr = GoogleVisionOCR()
img = cv2.imread(r'Test_Images\Tables\20231019_092445.jpg')
x=ocr.detectText(img)
l=[]
for i in x:
    b=Box(i.bounding_poly.vertices[0].x,i.bounding_poly.vertices[1].x,i.bounding_poly.vertices[2].x,i.bounding_poly.vertices[3].x,i.bounding_poly.vertices[0].y,i.bounding_poly.vertices[1].y,i.bounding_poly.vertices[2].y,i.bounding_poly.vertices[3].y)
    c=Cell(i.description,b)
    l.append(c)
mt=MarksheetTable(2,2,*l,name="Test")
print(mt.getMarks())