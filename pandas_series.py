## Pandas Series Exercises

##import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits

#1. Determine the number of elements in fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits.size


#2 Output only the index from fruits.
list(fruits.index) # wrapping it in list gives the index values

#3 Output only the values from fruits.
print(fruits.values)
len(fruits.values)

#4 Confirm the data type of the values in fruits.
fruits.dtype # Capital O in pandas means object

#5 Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5)

fruits.tail(3)

fruits.sample(2)

#METHODS
str.capitalize? # how to get documentation on pandas/python methods

# 6 Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()

# 7 Run the code necessary to produce only the unique string values from fruits.
# set casting on values would be set(fruits.values)
fruits.unique()

# 8 Determine how many times each unique string value occurs in fruits.
fruits.nunique()

# 9 Determine the string value that occurs most frequently in fruits.
fruit_counts = fruit_series.value_counts()
print(max(fruit_counts))
fruit_counts.nlargest(n = 1, keep='all')

#another way
fruits.value_counts().head(1)

## 10 Determine the string value that occurs least frequently in fruits.
fruits.value_counts().tail(1)
# another way that includes all smallest values
fruits.value_counts().nsmallest(n=1, keep='all')

### Value_counts will output a new pandas series
    - The content (values) of this value counts series is now the number of times an element pops us 
                and the index is the original thing that it was counting from our origin series. in this case value_counts gives us a series of string literal indexes associated with integer

### Exercises Part 2

# 1 Capitalize all the string values in fruits.
fruits.str.capitalize()

#2 Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')
# fancier way with concatination, 'count of a' string literal, plus string count
fruits.apply(lambda x: x + 'count of a: ' + str(x.count('a')))

#3 Output the number of vowels in each and every string value.
fruits.str.count(r'[aeiou]')

# 4 Write the code to get the longest string value from fruits.
# this gets all length: fruits.str.len()
# this gets us the biggest: 
fruits.str.len().max()
# use this for comparison to get a boolean:
bool_mask = fruits.str.len() == fruits.str.len().max()
# think of square brackets as the english word "where"
fruits[bool_mask]

# 5 Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >=5]

#6 Find the fruit(s) containing the letter "o" two or more times.
# if you want to use two string methods, make sure you specify .str ahead of each invocation
fruits[fruits.str.lower().str.count('o') >=2]

# 7 Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains("berry")]
#other fancy way
fruits[fruits.apply(lambda x: 'berry' in x)]

# 8 Write the code to get only the string values containing the substring "apple".
fruit_series[fruit_series.str.contains("apple")]
#other fancy way
fruits[fruits.apply(lambda x: 'apple' in x)]

#9 Which string value contains the most vowels?
fruits[fruits.str.count('a|e|i|o|u').max()]

### Exercises Part III
Use pandas to create a Series named letters from the following string. The easiest way to make this string into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.

random_letters =     'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
list(random_letters)
random_list = list(random_letters)
random_series = pd.Series(random_list)
print(random_series)

# 1 Which letter occurs the most frequently in the letters Series?
random_series[random_series.value_counts().max()]
#or
random_series.value_counts().head(1)
#or
random_series.value_counts().idxmax() #idx max gives us the index associated with 

# 2 Which letter occurs the Least frequently?
random_series[random_series.value_counts().min()]
# or
random_series.value_counts().nsmallest(n=1, keep='all')

# 3 How many vowels are in the Series?
vowels = list('aeiou')
random_series[random_series.isin(vowels)].count()
#or
def is_vowel(some_word):
    return some_word in ['a','e','i','o','u']
random_series.str.lower().apply(is_vowel).sum()

### ~ means apply the idea of 'not' to every instance in the series output by my vowel check 

# 4 How many consonants are in the Series?
#random_series.size - random_series[random_series.isin(vowels)].count()
(~random_series.str.lower().apply(is_vowel)).sum()

# 5 Create a Series that has all of the same letters but uppercased.
upper_letters = random_series.str.upper()
print(upper_letters)

# 6 Create a bar plot of the frequencies of the 6 most commonly occuring letters.
random_series.value_counts().head(6).plot(kind='barh')
plt.title('Top Six Letters')
plt.show()

# Use pandas to create a Series named numbers from the following list:
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 1 What is the data type of the numbers Series?
type(numbers) #series

# 2 How many elements are in the number Series?
numbers.size

#3 Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
def currency_to_float(amount):
    return float(amount.strip('$').replace(',', ''))
numbers = numbers.apply(currency_to_float)
numbers
#another way
#numbers = numbers.str.replace('$','').str.replace(',','').astype(float)

# 4 Run the code to discover the maximum value from the Series.
max_value = numbers.max()
max_value

#5 Run the code to discover the minimum value from the Series.
min_value = numbers.min()
min_value

# 6 What is the range of the values in the Series?
range_value = max_value - min_value
range_value

# 7 Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(numbers, 4).value_counts().sort_index()

#8 Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
pd.cut(numbers, 4).value_counts().sort_index().plot(kind='barh')


# Use pandas to create a Series named exam_scores from the following list:
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 1 How many elements are in the exam_scores Series?
exam_scores.size

# 2 Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.max(), exam_scores.min(), exam_scores.mean(), exam_scores.median()

# 3 Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

# 4 Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curved_grade = exam_scores + (100-exam_scores.max())
curved_grade.max()

# 5 Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
bin_edges = [0, 70, 75, 80, 90, 100]
bin_labels = ['F', 'D', 'C', 'B', 'A']
letter_grades = pd.cut(curved_grade, bins=bin_edges,labels=bin_labels)

letter_grades

# 6 Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_grades.value_counts().sort_index().plot.barh()
plt.title('Curved Letter Grade Distribution')
plt.show()

