from GoogelVisionOCR import GoogleVisionOCR
import cv2
class IndexNumber:
    def __init__(self,img,ocr=GoogleVisionOCR()) -> None:
        x=ocr.detectText(img)
        self.__text=x[0].description
    def getIndexNumber(self) -> int:
        num=self.__text[-1]
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
        i=-2
        while i>=-6:
            i-=1
            if self.__text[i].isdigit():
                num+=self.__text[i]
            elif(self.__text[i] in d):
                num+=d[self.__text[i]][0]
            else:
                num+='_'
        return num