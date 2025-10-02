# array operations
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print("Addition:", c)
d= a*b
print("Multiplication:",d)
e=a+10
print("Broadcasting (adding 10):",e)
print("Sum of elements:",np.sum(a))
print("Mean of elements:",np.mean(a))

#indexing and slicing
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[0])
print(arr[1:4])
arr[2:4]=[10,20]
print(arr)


#  reshaping
import numpy as np
arr=np.arange(1,13)
print("Original array:",arr)
reshaped_arr=arr.reshape(3,4)
print("Reshaped array (3x4):\n",reshaped_arr)
flattened_arr= reshaped_arr.flatten()
print("Flattened array:", flattened_arr)

