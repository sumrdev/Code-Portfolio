#opgave 1
import numpy as np

#opgave 2
print(np.__version__)
print(np.show_config)

#opgave 3
vector = np.zeros(10)
print(vector)

#ogpave 4
print(vector.size * vector.itemsize, "bytes")
print(vector.nbytes, "bytes")

#opgave 6
vector2 = np.zeros(10)
vector2[4] = 1
print(vector2)

#opgave 7
vector3 = np.linspace(10,49,40)
print(vector3)

#opgave 8
vector4 = np.linspace(0,9,10)
print(np.flip(vector4))

#opgave 9
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.linspace(0,8,9).reshape(3,3)
print(arr)
print(arr2)

#ogpave 10
arr3 = np.array([1,2,0,0,4,0])
print(np.nonzero(arr3))

#opgave 11
arr4 = np.identity(3)
print(arr4)

#opgave 12
arr5 = np.random.rand(3,3,3)
print(arr5)

#opgave13
arr6 = np.random.rand(10,10)
print(arr6.min(),arr6.max())

#opgave14
arr7 = np.random.rand(30)
print(arr7.mean())

#opgave 15
arr8 = np.ones((5,5))
arr8[1:-1,1:-1] = 0
print(arr8)

#opgave 16
arr9 = np.ones((5,5))
arr9 = np.pad(arr9,pad_width=1)
print(arr9)

#opgave 17
print(0 * np.nan, np.nan == np.nan, np.inf > np.nan, np.nan-np.nan,np.nan in set([np.nan]), )

#opgave 18
