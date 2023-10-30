import numpy as np
import pandas as pd

mylist = [1,2,3]
print(mylist)

np.arange(0,10,2)
print(np.arange(0,10,2))

arrayZero = np.zeros((5,5))
arrayShape = np.ones(shape=(3,2))
print(arrayZero)
print(arrayShape)

np.random.seed(101)
arrayRandom = np.random.randint(0,100,10)
print(arrayRandom)
print(arrayRandom.max())
print(arrayRandom.argmax())
print(arrayRandom.min())
print(arrayRandom.mean())

arrShape1 = arrayRandom.reshape((2,5))
print(arrShape1)

mat = np.arange(0,100).reshape(10,10)
print(mat)

col1 = mat[:,1]
print(col1)
print("col1 reverse: \n" + str(col1.reshape(10,1)))

line2 = mat[2,:]
print("line2: \n" + str(line2))
print("line2 reverse: \n" + str(line2.reshape(10,1)))


# print array n3
print(mat[0:3,0:3])

