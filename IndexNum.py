class IndexNumber:
    def __init__(self,text:str) -> None:
        self.__text=text

    def getIndexNumber(self) -> int:
        num=''
        for i in range(len(self.__text)):
            if self.__text[i].isdigit():
                num+=self.__text[i]
        if(self.__text[-1].isalpha()):
            num+=self.__text[-1]
        return num