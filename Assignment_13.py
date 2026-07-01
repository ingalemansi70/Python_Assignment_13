#Question 1
import numpy as np
# a)
arr_1d = np.array([10,20,30,40,50])
# b) 
arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print("One dimensional Array : ",arr_1d) 
print("Two dimensional Array(3*3) : ",arr_2d)


#Question 2)
#a)
zero_arr = np.zeros(8)
print("1 Dimensional array with 8 zeros : ",zero_arr)
#b)
twoD_arr1 = np.ones((4,4))
print("4*4 array with 1 is : ",twoD_arr1)
#c)
twoD_arr2 = np.zeros((3,3))
print("3*3 array with 0 is : ",twoD_arr2)

# Question 3)
#a)
arr = np.arange(0,20)
print("Array with Numbers from 0 to 20 (step 1) : ",arr)
#b)
even_arr = np.arange(10,51,2)
print("Array of Even numbers from 10 to 50 :",even_arr)
#c)
new_arr = np.arange(5,100,5)
print("Array of Numbers from 5 to 100 with step of 5 : ",new_arr)





