#to display qr
import cv2
#for read csv data
import pandas as pd
#to fond log values and use polyfit function
import numpy as np
#to plot graph
from matplotlib import pyplot as plt
#to create qr
import pyqrcode as qr
#read csv file by pandas
df=pd.read_csv('/home/niteesh/proj/python/group project/covidcases.csv')
#find value of a and b in y=a(e)^bx using numpy
g=np.polyfit(df.SINO,np.log(df.CASES),1)
#a[0]=b,a[1]=a hence x is input i.e days y is out put i.e, covid cases
print(g)
#title for graph
plt.title('covid cases in India')
#for x lable
plt.xlabel('days (feb-15 1st case in india)')
#for y lable
plt.ylabel('cases (0.1 = 1M)')
#for plor graph
plt.plot(df.SINO,df.CASES)
#for show the graph

#hence we know ln(y)=log(a)+b(x) a,b known by substituting x values we get y
# y are cases x are days formulae is by adding e on both sides
#y=((2.7182)**a[1]+(2.7182)**a[0]*x)
z=input('day:')
x=float(z)
#a[0],a[1]==0.087,2.429 is float hence
b=float(0.087)
a=float(2.429)
print(a,b)
y=(a*(2.7)**(x*b))
o=int(y)
print(o)
#to create answer in qr
a=qr.create(o)
#save qr as picture
a.png('/home/niteesh/proj/python/group project/output qr.png',scale=6)
#options to choose
print('to show graph enter graph to show qr enter qr')
v=input('options:')
if v=='graph':
    plt.show()
if v=='qr':
    img2=cv2.imread('/home/niteesh/proj/python/group project/output qr.png')
    #to show qr
    cv2.imshow('qr',img2)
    #milliseconds to show pic
    cv2.waitKey(200000)
else:
    print('wrong option')