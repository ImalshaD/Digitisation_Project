from detect import DetectLayout
import cv2
img=cv2.imread(r'app\resources\Temp\WhatsApp Image 2023-11-01 at 10.49.27.jpeg')
x=DetectLayout(img)
print(x.getIndex())
print(x.getMarks())