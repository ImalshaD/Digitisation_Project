from GoogelVisionOCR import GoogleVisionOCR
import cv2
ocr = GoogleVisionOCR()
img = cv2.imread(r'app\resources\Temp\WhatsApp Image 2023-11-01 at 10.49.27.jpeg')
x=ocr.detectText(img)
