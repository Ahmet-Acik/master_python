import numpy as np

a_array = [1, 2, 3, 4, 5]
print(f"a_array: ", a_array)  # [1, 2, 3, 4, 5]
print(a_array[2])
print(a_array[1:3])
print(a_array[::-1])
print(a_array[::2])

np_array = np.array([1, 2, 3, 4, 5])
print(f"np_array: ", np_array)  # [1 2 3 4 5]
print(f"type(np_array)", type(np_array))  # <class 'numpy.ndarray'>
print(
    f"np_array[2] : {np_array}, type(np_array[2]), :  {type(np_array[2])}"
)  # np_array[2] : [1 2 3 4 5], type(np_array[2]), :  <class 'numpy.int64'>
print(f"np_array[1:3] : {np_array[1:3]})")  # np_array[1:3] : [2 3])
print(f"np_array[:-2] : {np_array[:-2]})")  # np_array[:-2] : [1 2 3])
np_array[2] = 100
print(f"np_array[2] = 100 : {np_array}")  # np_array[2] = 100 : [  1   2 100   4   5]

np_mdarray = np.array([[[1, 2, 3], [4, 5, 6]]])

print(f"np_mdarray: {np_mdarray}")  # np_mdarray: [[1 2 3]  [4 5 6]]
print(f"np_mdarray: \n{np_mdarray}")
np_mdarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"np_mdarray: \n{np_mdarray}")
print(f"np_mdarray.shape: {np_mdarray.shape}")  # np_mdarray.shape: (3, 3)
print(f"np_mdarray.ndim: {np_mdarray.ndim}")  # np_mdarray.ndim: 2
print(f"np_mdarray.size: {np_mdarray.size}")  # np_mdarray.size: 9
print(f"np_mdarray.dtype : {np_mdarray.dtype}")  # np_mdarray.dtype : int64

np_mdarray = np.array([[1, 2, 3], [4, "Hello", 6], [7, 8, 9]])
np_mdarray_int = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int64)
print(f"np_mdarray: \n{np_mdarray.dtype}")  # np_mdarray:   <U21
print(
    type(np_mdarray[2][2])
)  # <class 'numpy.str_'> why not int64 ? because of "Hello" string value in the array
print(np_mdarray[2][2])  # 9
print(np_mdarray[1][1])  # Hello
print(np_mdarray[1][2])  # 6
