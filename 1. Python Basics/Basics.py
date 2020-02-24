custList = ["Suvarna",42,"Amit",32,"Rohit",41,"Janhavi",42,"Deepa",49]

custList

prodList = [["Pen",10],
            ["Pencil",8],
            ["Eraser",5],
            ["Sharpner",10]]
prodList

custList[3]
custList[-7]

custList[3:7]
custList[-5:-2]
custList[:6]
custList[6:]

# Incremental
custList[0:5:2]
custList[::2]

custList[3]=34
custList[0:2]=["Sumedha",5]

custList=custList+["Girija",13]
del(custList[6:8])
custList

custList.append(["Deepika",32])
print(custList)

custList.append("Anushka")
custList.append(36)
print(custList)

### Inserting any element in the list
custList.insert(4,'Nitin')
custList.insert(5,48)

## Call by Reference
Customers=custList
Customers[1]=36
Customers

Customers.index("Rohit")

## Call by Value
Customers=custList.copy()
Customers[1]=66


import numpy
numpy.absolute(-8)

import numpy as np
np.absolute(-8)

from numpy import absolute
absolute(-8)

length = [23,34.5,6.7,90.4,45.3]
breadth = [21,23,45,65,12.3]

area = length * breadth

length + breadth

import numpy
lg = numpy.array(length)
bd = numpy.array(breadth)
area = lg * bd
area
lg + bd

### Using alias
import numpy as np
lg = np.array(length)
bd = np.array(breadth)
area = lg * bd
area
lg + bd

lg
lg>30
lg[lg>30]

a1 = np.array([[12,23,29,34],[89,92,82,56]])
a1
a1.shape
type(a1)
a1[0]
a1[0][2]
a1[0,2]
a1[:,1:3]

lg
type(lg)
np.mean(lg)
np.median(lg)
# Ascending
np.sort(lg) 

# Descending
-np.sort(-lg)

lg
type(np)
lg.mean()
lg.size
lg.sort()
lg

# Loading data using numpy.loadtxt()
boston = np.loadtxt("G:/Statistics (Python)/Datasets/Boston.csv",
                    delimiter=",",skiprows=1)
boston.shape

boston[0,2]

