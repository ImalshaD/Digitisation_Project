from ultralytics import YOLO
from indexNum import IndexNumber
from MarksheetTable import MarksheetTable
import numpy
import cv2
class DetectLayout:
    def __init__(self,image,model=YOLO(r'app\layoutDetection\best.pt','v8')) -> None:
        self.image=image
        self.model = model
        self.saves=model.predict(source=image, show=False, save=False, conf=0.5, save_txt=False, save_crop=False)
        for detection in self.saves:
            for index, (box, label) in enumerate(zip(detection.boxes.xyxy, detection.boxes.cls)):
                if int(label)==1:
                    x1=float(box[0])
                    y1=float(box[1])
                    x2=float(box[2])
                    y2=float(box[3])
                    self.index_crop=self.crop_image(self.image,x1,y1,x2,y2)
                    index=IndexNumber(self.index_crop)
                    self.indexNumber = index.getIndexNumber()
                elif int(label)==2:
                    x1=float(box[0])
                    y1=float(box[1])
                    x2=float(box[2])
                    y2=float(box[3])
                    self.table=self.crop_image(self.image,x1,y1,x2,y2)
                    marks = MarksheetTable(2,2,self.table,"Marks")
                    self.marks = marks.getMarks()
    def crop_image(self,image, x1, y1, x2, y2):
        """
        Crop an image based on the provided coordinates.

        Parameters:
        - image: The input image.
        - x1, y1, x2, y2: Coordinates of the region to be cropped.

        Returns:
        - The cropped region of the image.
        """
        # Convert coordinates to integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Crop the image
        cropped_image = image[y1:y2, x1:x2]

        return cropped_image
    def getIndex(self):
        return self.indexNumber
    def getMarks(self):
        return self.marks


