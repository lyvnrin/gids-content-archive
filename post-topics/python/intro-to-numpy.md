## 1: WHAT IS NUMPY?
NumPy (or Numerical Python) is a key library for numerical computing. It provides fast, mult-dimensional arrays and many mathematical functions, making it super handy for handling large datasets or doing complex calculations (GeeksforGeeks, 2017).  

Its main feature is the array, which is like a more powerful Python list. Arrays let you perform operations on entire datasets or matrices at once - faster and clean than loops.

## 2: USAGE OF NUMPY

**A. Creating Arrays**
```
import numpy as np

A = np.array([1,2,3,4])
print(A)
```

Arrays can be created from lists. They’re faster than regular Python lists and let you do maths directly.

**B. Array Operations**
```
A2 = np.array([5,6,7,8])
A_sum = A + A2
print(A_sum)
```

NumPy lets you add, subtract, multiply, or divide arrays element-wise without loops - perfect for large datasets.

**C. Working with Matrices**
```
matrix = np.array([[1,2],[3,4]])
transpose = matrix.T
print(transpose)
```

A matrix is just a 2D array of numbers. Transposing flips rows and columns. This is handy for:
* Reorganising data,
* Preparing datasets for analysis
* Aligning information in science, finance, engineering, etc.

**D. Generating Data**
```
random_nums = np.random.rand(3)
print(random_nums)
```

NumPy also helps generate sequences or random numbers,  useful for simulations, testing, or filling datasets quickly.

## 3: REAL-WORLD USE CASES
Numpy is used everywhere numbers are involved (Kumari, 2024).
* Data analysis: Process large datasets and perform calculations quickly.
* Scientific computing: Running simulations, experiments, or solving maths problems with arrays and matrices.
* Machine learning: Handling input data efficiently for models.

Even simple tasks like tracking daily temperatures or calculating averages across spreadsheets become faster with NumPy arrays.

## Citations
1. GeeksforGeeks. (2017, January 31). NumPy Introduction. GeeksforGeeks. https://www.geeksforgeeks.org/python/introduction-to-numpy/
Kumari, S. (2024, June 25). Empowering Scientific Computing in Python with NumPy. CloudThat Resources. https://www.cloudthat.com/resources/blog/empowering-scientific-computing-in-python-with-numpy

