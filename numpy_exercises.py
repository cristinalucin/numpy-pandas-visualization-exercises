## a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

### 1. How many negative numbers are there?

np.negative(a)
len(a[a<0])

### 2. How many positive numbers are there?

np.positive(a)
len(a[a>0])

### 3. How many even positive numbers are there?

b= a[a>0]
b % 2 == 0
np.sum(b % 2 ==0)

### 4. If you were to add 3 to each data point, how many positive numbers would there be?

len(a[(a+3) >0])

### 5. If you squared each number, what would the new mean and standard deviation be?

a
a_squared = np.square(a)
new_mean = np.mean(np.square(a))
new_sd = np.std(np.square(a))
print(a_squared)
print(new_mean)
print(new_sd)

### 6. A common statistical operation on a dataset is centering. This means to adjust the data such that 
###the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set.
# ##See this link for more on centering.

a
print(a.mean())
center_function = lambda x: x - x.mean()
data_centered = center_function(a)
print(data_centered)
print(data_centered.mean())

### 7. Calculate the z-score for each data point.

print (a)
mean = np.mean(a)
std = np.std(a)
print('mean of the dataset is', mean)
print('std. deviation is', std)


z_scores = (a-np.mean(a) / np.std(a))
print (z_scores)

### 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py 
# ## and add your solutions.

### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_a = sum(a)

### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

### Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = np.mean(a)

### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = print(np.prod(a))

### Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = print(np.square(a))

 ### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
 
 # create a numpy array
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(ar)
odds_in_a = ar[ar % 2 != 0]
print (f'Here are the odds: {odds_in_a}')

### 8. Make a variable named evens_in_a. It should hold only the evens

ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(ar)
evens_in_a = ar[ar % 2 == 0]
print (f'Here are the evens: {evens_in_a}')

## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, 
# nd list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]
### Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
## **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
    
    
