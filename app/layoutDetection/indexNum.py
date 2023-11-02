from OCR import GoogleVisionOCR
import cv2
class IndexNumber:
    def __init__(self,img,ocr=GoogleVisionOCR()) -> None:
        x=ocr.detectText(img)
        self.__text=x[0]['description']
    def getIndexNumber(self) -> int:
        num=''
        for i in range(len(self.__text)):
            if self.__text[i].isdigit():
                num+=self.__text[i]
        num+=self.__text[-1]
        return num