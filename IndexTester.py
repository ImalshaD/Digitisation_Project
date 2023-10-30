from IndexNum import IndexNumber
from GoogelVisionOCR import GoogleVisionOCR
import cv2
ocr = GoogleVisionOCR()
img = cv2.imread(r'Test_Images\Index_Number\20231019_092406.jpg')
x=ocr.detectText(img)
print(x[0].description)
i=IndexNumber(x[0].description)
print(i.getIndexNumber())