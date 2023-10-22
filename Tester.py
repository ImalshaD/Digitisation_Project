from GoogelVisionOCR import GoogleVisionOCR
import cv2
ocr = GoogleVisionOCR()
img = cv2.imread(r'Test_Images\Tables\IMG_20231019_092933.jpg')
x=ocr.detectText(img)
print(x[1])