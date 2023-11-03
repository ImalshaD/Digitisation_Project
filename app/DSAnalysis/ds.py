from abc import ABC,abstractmethod

class DS(ABC):
    @abstractmethod
    def getQCount():
        pass
    @abstractmethod
    def getGradecounts():
        pass
    @abstractmethod
    def getlines():
        pass
    
    @abstractmethod
    def getDistributuions():
        pass