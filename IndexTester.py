# from IndexNum import IndexNumber
from GoogelVisionOCR import GoogleVisionOCR
import cv2
di={'a': ['4'],
            'b': ['8'],
            'c': ['6'],
            'd': ['9'],
            'e': ['3'],
            'f': ['7'],
            'g': ['9'],
            'h': ['4'],
            'i': ['1'],
            'j': ['7'],
            'k': ['8'],
            'l': ['1'],
            'n': ['0'],
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
            'F': ['8'],
            'G': ['9'],
            'H': ['4'],
            'I': ['7'],
            'J': ['7'],
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
            'Z': ['2'],
            '}': ['1'],
            '{': ['1']}
dc={'0': ['O'],
    '1': ['I'],
    '2': ['Z'],
    '3': ['B'],
    '4': ['A'],
    '5': ['S'],
    '6': ['G'],
    '7': ['J'],
    '8': ['B'],
    '9': ['Q']}
ocr = GoogleVisionOCR()
img = cv2.imread(r'Test_Images\Index_Number\IMG-20231006-WA0008.jpg')
n=ocr.detectText(img)[0].description
print(n)
i=-2
m=6
if(n[-1].isupper()):
    num=n[-1]
elif(n[-1].islower()):
    num=n[-1].upper()
elif(n[-1] in dc):
    num=dc[n[-1]][0]
else:
    num='_'
while m>0:
    if n[i].isdigit():
        num=n[i]+num
        m-=1
    elif(n[i] in di):
        num=di[n[i]][0]+num
        m-=1
    i-=1
print(num)

# not working
#Test_Images\Index_Number\20231019_092500.jpg
#Test_Images\Index_Number\20231019_092712.jpg

# i=IndexNumber(x[0].description)

# print(x[0].description)