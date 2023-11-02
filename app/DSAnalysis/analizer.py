import numpy as np
import pandas as pd
from statistics import mean
class Analizer:
    def __init__(self,ca_weight,max_qs,final_weights,marks) -> None:
        self.ca_weight = ca_weight
        self.max_qs = max_qs
        self.final_weights = final_weights
        self.data = marks
        pass
    def analyse(self):
        self.self.data['FinalMarks'] = round(((100-self.ca_weight)*self.self.data['Total'] + self.ca_weight*self.self.data['CA_marks'])/100)
        d={}
        for col in self.data.columns:
            if(col=='FinalMarks'):
                d[f'{col}']={}
                d[f'{col}']['grades']={}
                d[f'{col}']['grades']['A+']=self.data[pd.notna(self.data[col]) & self.data[col]>=85][col].count()
                d[f'{col}']['grades']['A']=self.data[pd.notna(self.data[col])&(self.data[col]>=75)&(self.data[col]<85)][col].count()
                d[f'{col}']['grades']['A-']=self.data[pd.notna(self.data[col]) &(self.data[col]>=70)&(self.data[col]<75)][col].count()
                d[f'{col}']['grades']['B+']=self.data[pd.notna(self.data[col]) &(self.data[col]>=65)&(self.data[col]<70)][col].count()
                d[f'{col}']['grades']['B']=self.data[pd.notna(self.data[col]) &(self.data[col]>=60)&(self.data[col]<65)][col].count()
                d[f'{col}']['grades']['B-']=self.data[pd.notna(self.data[col]) &(self.data[col]>=55)&(self.data[col]<60)][col].count()
                d[f'{col}']['grades']['C+']=self.data[pd.notna(self.data[col]) &(self.data[col]>=50)&(self.data[col]<55)][col].count()
                d[f'{col}']['grades']['C']=self.data[pd.notna(self.data[col]) &(self.data[col]>=45)&(self.data[col]<50)][col].count()
                d[f'{col}']['grades']['C-']=self.data[pd.notna(self.data[col]) &(self.data[col]>=35)&(self.data[col]<45)][col].count()
                d[f'{col}']['grades']['W']=self.data[pd.notna(self.data[col]) &(self.data[col]<35)][col].count()
            elif(col=='Total'):
                d['writtenExam']={}
                d['writtenExam']['repeat']=self.data.loc[self.data['Total'] < 35, 'Index'].tolist()
                d['writtenExam']['repeatCount']=len(d['writtenExam']['repeat'])
                d['writtenExam']['absent']=self.data.loc[pd.isna(self.data['Total']), 'Index'].tolist()
                d['writtenExam']['absentCount']=len(d['writtenExam']['absent'])
            elif(col=='CA_marks'):
                d['CA']={}
                d['CA']['repeat']=self.data.loc[self.data['CA_marks'] < 35, 'Index'].tolist()
                d['CA']['repeatCount']=len(d['CA']['repeat'])
                d['CA']['absent']=self.data.loc[pd.isna(self.data['CA_marks']), 'Index'].tolist()
                d['CA']['absentCount']=len(d['writtenExam']['absent'])
            elif(col!='Index'):
                d[f'{col}']={}
                d[f'{col}']['marks']=self.data[self.data[col].notna()][col].values
                d[f'{col}']['maximum']=max(d[f'{col}']['marks'])
                d[f'{col}']['minimum']=min(d[f'{col}']['marks'])
                d[f'{col}']['mean']=mean(d[f'{col}']['marks'])
                d[f'{col}']['answers']=len(d[f'{col}']['marks'])
        return d
