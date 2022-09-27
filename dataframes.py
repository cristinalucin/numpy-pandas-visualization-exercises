#Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

#1. Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

stud_df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(stud_df)


#a. Create a column named passing_english that indicates whether each student has a passing grade in english.
stud_df.english >= 70
stud_df['passing_english'] = stud_df.english >= 70
stud_df

#b. Sort the english grades by the passing_english column. How are duplicates handled?
stud_df.sort_values(by='passing_english', ascending=False)
# Duplicates are sorted by index


#c. Sort the english grades first by passing_english and then by student name. All the students that are 
# failing english should be first, and within the students that are failing english they should be ordered 
# alphabetically. The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
stud_df.sort_values(by=['passing_english', 'name'])

#d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how 
# we did in the last step.
stud_df.sort_values(by=['passing_english','english'], ascending=[False,False])

# e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is 
# the average of the math, english, and reading grades.
stud_df.assign(overall_grade = ((stud_df['math'] + stud_df['english'] + stud_df['reading']) / 3)).round(2)

#2 Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
#data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable

# How many rows and columns are there?
mpg_df.shape

# What are the data types of each column?
mpg_df.info
mpg_df.dtypes

# Summarize the dataframe with .info and .describe
mpg_df.describe

# Rename the cty column to city
mpg_df.rename(columns={'cty': 'city'}, inplace = True)

# Rename the hwy column to highway
mpg_df.rename(columns={'hwy': 'highway'}, inplace = True)

# Do any cars have better city mileage than highway mileage?
mask = mpg_df.city > mpg_df.highway
len(mpg_df[mask])

# Create a column named mileage_difference this column should contain 
# the difference between highway and city mileage for each car.
mpg_df = mpg_df.assign(mileage_difference = (mpg_df['highway']-mpg_df['city'])) 
mpg_df

# Which car (or cars) has the highest mileage difference?
mpg_df.sort_values(by='mileage_difference', ascending = False)
mpg_df.nlargest(5, columns=['mileage_difference'])

# Which compact class car has the lowest highway mileage? The best?
#compact cars variable
compact_cars_df = mpg_df[mpg_df['class'] == 'compact']
# lowest highway mileage of compact
compact_cars_df[compact_cars_df.highway == compact_cars_df.highway.min()]
# highest highway mileage of compacy
compact_cars_df[compact_cars_df.highway == compact_cars_df.highway.max()]

# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg_df["average_mileage"] = (mpg_df.highway + mpg_df.city) /2
mpg_df

# Which dodge car has the best average mileage? The worst?
dodge_df = mpg_df[mpg_df['manufacturer'] == 'dodge']
dodge_df

#best
dodge_df[dodge_df.average_mileage == dodge_df.average_mileage.max()]

#worst
dodge_df[dodge_df.average_mileage == dodge_df.average_mileage.min()]

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals_df = data('Mammals') 

# How many rows and columns are there?
mammals_df.shape
#107 rows, 4 columns

# What are the data types?
mammals_df.dtypes

# Summarize the dataframe with .info and .describe
mammals_df.info()
mammals_df.describe()

# What is the the weight of the fastest animal?
fastest_animal = mammals_df.speed.max()
mammals_df.weight[mammals_df.speed == mammals_df.speed.max()]

## What is the overal percentage of specials?
# getting all specials
mammals_df.specials[mammals_df.specials == True].count()
round(((mammals_df.specials[mammals_df.specials == True].count()) / (len(mammals_df.specials)) * 100), 2)

## How many animals are hoppers that are above the median speed? What percentage is this?
hoppers_df = mammals_df[mammals_df.hoppers == True]
hoppers_df[hoppers_df.speed > mammals_df.speed.median()]

