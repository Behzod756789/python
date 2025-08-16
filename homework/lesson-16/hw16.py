import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr1, "\n")

arr2 = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix from 2 to 10:\n", arr2, "\n")

arr3 = np.zeros(10)
print("Null Vector:", arr3)
arr3[6] = 11
print("Update sixth value to 11:", arr3, "\n")

arr4 = np.arange(12, 38)
print("Array with values from 12 to 38:\n", arr4, "\n")

arr5 = np.array([1, 2, 3, 4])
print("Original array:", arr5)
arr5 = arr5.astype(float)
print("Array converted to float:", arr5, "\n")

celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32
print("Values in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit, "\n")

arr7 = np.array([10, 20, 30])
arr7_appended = np.append(arr7, [40, 50, 60, 70, 80, 90])
print("Original array:", arr7)
print("After append values to the end of the array:", arr7_appended, "\n")

arr8 = np.random.randint(1, 100, 10)
print("Random array:", arr8)
print("Mean:", np.mean(arr8))
print("Median:", np.median(arr8))
print("Standard Deviation:", np.std(arr8), "\n")

arr9 = np.random.rand(10, 10)
print("10x10 Random Array:\n", arr9)
print("Minimum value:", arr9.min())
print("Maximum value:", arr9.max(), "\n")

arr10 = np.random.rand(3, 3, 3)
print("3x3x3 Array with Random Values:\n", arr10)
