class Box:
    def __init__(self,x1,x2,x3,x4,y1,y2,y3,y4) -> None:
        self.__x1=x1
        self.__x2=x2
        self.__x3=x3
        self.__x4=x4
        self.__y1=y1
        self.__y2=y2
        self.__y3=y3
        self.__y4=y4
        self.__width=((self.__x2-self.__x1)+(self.__x3-self.__x4))/2
        self.__height=((self.__y2-self.__y3)+(self.__y1-self.__y4))/2

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getx1(self):
        return self.__x1
    def getx2(self):
        return self.__x2
    def getx3(self):
        return self.__x3
    def getx4(self):
        return self.__x4
    def gety1(self):
        return self.__y1
    def gety2(self):
        return self.__y2
    def gety3(self):
        return self.__y3
    def gety4(self):
        return self.__y4