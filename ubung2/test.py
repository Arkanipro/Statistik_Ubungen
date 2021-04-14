import csv
from enum import Enum
class Sex_(Enum):
    Male = 1
    Female = 2

csvdatei=open('americans.csv')
csv_reader_object = csv.reader(csvdatei, delimiter=',')
CaseID,Age,Sex,BMI,Height_In,Weight_lb,Height_cm,Weight_kg,Groceries=[],[],[],[],[],[],[],[],[]
for row in csv_reader_object:
    CaseID.append(row[1])
    Age.append(row[2])
    Sex.append(row[3])
    BMI.append(row[4])
    Height_In.append(row[5])
    Weight_lb.append(row[6])
    Height_cm.append(row[7])
    Weight_kg.append(row[8])
    Groceries.append(row[9])
#extract 100 data points!
CaseID_,Age_,Sex_,BMI_,Height_In_,Weight_lb_,Height_cm_,Weight_kg_,Groceries_=[],[],[],[],[],[],[],[],[]
import numpy 
import pandas
import scipy.stats
rng = numpy.random.default_rng(1337)
idxES=rng.integers(low=1, high=len(CaseID)-1, size=100)
for m in range(len(idxES)):
    i=idxES[m]
    #print(str(m)+" - "+str(i))
    CaseID_.append(int(CaseID[i]))
    Age_.append(int(Age[i]))
    Sex_.append(int(Sex[i]))
    BMI_.append(float(BMI[i]))
    Height_In_.append(int(Height_In[i]))
    Weight_lb_.append(int(Weight_lb[i]))
    Height_cm_.append(float(Height_cm[i]))
    Weight_kg_.append(float(Weight_kg[i]))
    Groceries_.append(1.0 if bool(Groceries[i])==True else 0.0)
#for i in range(len(CaseID_)):
#    print(str(CaseID_[i])+", "+str(Age_[i])+", "+str(Sex_[i])+", "+str(BMI_[i])+", "+str(Height_In_[i])+", "+str(Weight_lb_[i])+", "+str(Height_cm_[i])+", "+str(Weight_kg_[i])+", "+str(Groceries_[i]))    

#mean, median, mode and standard deviation

df=pandas.DataFrame({
'Index':['mean','median','mode','standard deviation'],
'CaseID':[numpy.mean(CaseID_),numpy.median(CaseID_),scipy.stats.mode(CaseID_,axis=None)[0][0],numpy.std(CaseID_)],
'Age':[numpy.mean(Age_),numpy.median(Age_),scipy.stats.mode(Age_,axis=None)[0][0],numpy.std(Age_)],
'Sex':[numpy.mean(Sex_),numpy.median(Sex_),scipy.stats.mode(Sex_,axis=None)[0][0],numpy.std(Sex_)],
'BMI':[numpy.mean(BMI_),numpy.median(BMI_),scipy.stats.mode(BMI_,axis=None)[0][0],numpy.std(BMI_)],
'Height(in)':[numpy.mean(Height_In_),numpy.median(Height_In_),scipy.stats.mode(Height_In_,axis=None)[0][0],numpy.std(Height_In_)],
'Weight(lb)':[numpy.mean(Weight_lb_),numpy.median(Weight_lb_),scipy.stats.mode(Weight_lb_,axis=None)[0][0],numpy.std(Weight_lb_)],
'Height(cm)':[numpy.mean(Height_cm_),numpy.median(Height_cm_),scipy.stats.mode(Height_cm_,axis=None)[0][0],numpy.std(Height_cm_)],
'Weight(kg)':[numpy.mean(Weight_kg_),numpy.median(Weight_kg_),scipy.stats.mode(Weight_kg_,axis=None)[0][0],numpy.std(Weight_kg_)],
'Does Groceries':[numpy.mean(Groceries_),numpy.median(Groceries_),scipy.stats.mode(Groceries_,axis=None)[0][0],numpy.std(Groceries_)]
})

print(df)
#print("mean:\nCaseID\tAge\tSex\tBMI\tHeight (in)\tWeight (lb)\tHeight (cm)\tWeight (kg)\tDoesGroceries")
#print(str(numpy.mean(CaseID_))+"\t"+str(numpy.mean(Age_))+"\t"+str(numpy.mean(Sex_)))    
