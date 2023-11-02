from detect import DetectLayout
import cv2
img=cv2.imread(r'app\resources\Temp\WhatsApp Image 2023-11-02 at 19.49.01.jpeg')
x=DetectLayout(img)
print(x.getIndex())
print(x.getMarks())