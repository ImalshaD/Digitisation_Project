from .ds import DS

class MokDS(DS):
    def getQCount(self):
        x = {'q{}'.format(i): 0 for i in range(1, 13)}
        return x
    def getGradecounts(self):
        grades = {'A+': [10, 15], 
                  'A': [20, 25],
                  'A-':[20,25] ,
                  'B+' : [12,13],
                  'B': [30, 35], 
                  'B-': [40, 45],
                  'C+':[10,20],
                  'C': [40, 45],
                  "C-" :[12,34],
                  'D': [50, 55],
                  "W": [12,9]}
        return grades
    def getlines(self):
        my_dict = {'q{}'.format(i): [2 * i - i for i in range(100)] for i in range(1, 13)}
        return my_dict
    def getDistributuions(self):
        my_dict = {i: [i + 1, i] for i in range(101)}
        return my_dict
    def getBoxPlot(self):
        my_dict ={
            "q1": [10,20,30,40],
            "q2": [10,20,30,40],
            "q3": [10,20,30,40],
            "q4": [10,20,30,40]
        }
        return my_dict