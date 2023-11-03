from .ds import DS
class DSChild(DS):
  def __init__(self,data,caWeight=30):
    self.data=data
    print(self.data)
    self.caWeight=caWeight
    self.weWeight=100-self.caWeight
    for i in data:
      if(i['camarks']!=None and i['total']!=None):
        i['final']=(int(i['camarks'])*self.caWeight+int(i['total'])*self.weWeight)//100
      elif(i['camarks']!=None):
        i['final']=(int(i['camarks'])*self.caWeight)//100
      elif(i['total']!=None):
        i['final']=(int(i['total'])*self.weWeight)//100
    self.qd={'q' + str(i): {str(j): 0 for j in range(21)} for i in range(1, 13)}
    self.md={str(i):[0,0] for i in range(101)}
    self.df={grade: [0,0] for grade in ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'W', 'I-CA', 'I-WE', "AB"]}
    for student in self.data:
      if(student['final']!=None):
        self.md[str(student['final'])][0]+=1
        self.md[str(student['final'])][1]+=1
      for i in range(1,13):
        if(student['q'+str(i)]):
          self.qd['q'+str(i)][str(int(student['q'+str(i)]))]+=1
      if(student['total']!=None):
        self.md[str(int(student['total']))][0]+=1
        self.md[str(int(student['total']))][1]+=1
      if(student['total']==None and student['camarks']==None):
        self.df["AB"][0]+=1
        self.df["AB"][1]+=1
      elif((student['total']==None or student['total']<35) and (student['camarks']!=None and student['camarks']>=35)):
        self.df['I-WE'][0]+=1
        self.df['I-WE'][1]+=1
      elif((student['camarks']==None or student['camarks']<35) and (student['total']!=None and student['total']>=35)):
        self.df['I-CA'][0]+=1
        self.df['I-CA'][1]+=1

#done
  def getGradecounts(self):
    for i in range(100,-1,-1):
      if i >= 85:
        self.df['A+'][0]+=self.md[str(i)][0]
        self.df['A+'][1]+=self.md[str(i)][1]
      elif i >= 75:
        self.df['A'][0]+=self.md[str(i)][0]
        self.df['A'][1]+=self.md[str(i)][1]
      elif i >= 70:
        self.df['A-'][0]+=self.md[str(i)][0]
        self.df['A-'][1]+=self.md[str(i)][1]
      elif i >= 65:
        self.df['B+'][0]+=self.md[str(i)][0]
        self.df['B+'][1]+=self.md[str(i)][1]
      elif i >= 60:
        self.df['B'][0]+=self.md[str(i)][0]
        self.df['B'][1]+=self.md[str(i)][1]
      elif i >= 55:
        self.df['B-'][0]+=self.md[str(i)][0]
        self.df['B-'][1]+=self.md[str(i)][1]
      elif i >= 50:
        self.df['C+'][0]+=self.md[str(i)][0]
        self.df['C+'][1]+=self.md[str(i)][1]
      elif i >= 45:
        self.df['C'][0]+=self.md[str(i)][0]
        self.df['C'][1]+=self.md[str(i)][1]
      elif i >= 35:
        self.df['C-'][0]+=self.md[str(i)][0]
        self.df['C-'][1]+=self.md[str(i)][1]
    return self.df

#done
  def getQCount(self):
    d={}
    for key,val in self.qd.items():
      d[key]=sum(val.values())
    return d

#done
  def getlines(self):
    return self.qd

#done
  def getDistributuions(self,modarate=0):
    # for i in range(100,-1,-1):
    #   if i+modarate>100:
    #     self.md[str(100)][1]+=self.md[str(i)][1]
    #   else:
    #     self.md[str(i+modarate)][1]+=self.md[str(i)][1]
    return self.md