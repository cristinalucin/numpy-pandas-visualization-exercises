### Use the iris database to answer the following quesitons:

1. What does the distribution of petal lengths look like?
2. Is there a correlation between petal length and petal width? Use http://guessthecorrelation.com/ as a hint to how we could visually determine if a correlation exists between two numeric columns.
3. Would it be reasonable to predict species based on sepal width and sepal length? For this, you'll visualize two numeric columns through the lense of a categorical column.
4. Which features would be best used to predict species?


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data

sns.set_context('notebook') # other settings include paper/poster/talk 
sns.set_style("ticks") # other styles include darkgrid/dark/whitegrid/white

#Load directly from sns dataset
iris = sns.load_dataset('iris')
sns.set_theme()  # https://seaborn.pydata.org/generated/seaborn.set_theme.html

data('iris', show_doc = True)
iris.head()

# 1. What does the distribution of petal lengths look like?

sns.displot(iris.petal_length)
plt.show()


# 2. Is there a correlation between petal length and petal width? Use http://guessthecorrelation.com/
# as a hint to how we could visually determine if a correlation exists between two numeric columns.

#sns.relplot(data = iris, x = 'petal_length', y = 'petal_width', palette= ['r', 'red'])
sns.relplot(data = iris, x = 'petal_length', y = 'petal_width', hue = 'species')

# There is a strong correlation between petal length and width

# 3. Would it be reasonable to predict species based on sepal width and sepal length? For this, 
# you'll visualize two numeric columns through the lense of a categorical column.

sns.relplot(data = iris, x = 'sepal_length', y = 'sepal_width', hue = 'species')

#I believe it would be reasonable to predict species based on sepal length and width, 
# particularly with a setosa species.Versicolor and virginica have a correlation as well, but seem to be harder
# to distinuish.

# 4. Which features would be best used to predict species?
sns.pairplot(data = iris, hue = 'species')


# 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set.

# Load directly from sns dataset
anscombe = sns.load_dataset('anscombe')

# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. 
# What do you notice?
anscombe.groupby("dataset").agg(['min', 'mean', 'max'])

# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
#  FacetGrid with 'col'
sns.relplot(data = anscombe, x = 'x',
            y = 'y',
            col = 'dataset')

# 2. Load the InsectSprays dataset and read it's documentation.
insect_sprays = data('InsectSprays')

insect_sprays.head(10)

# Create a boxplot that shows the effectiveness of the different insect sprays.

sns.catplot(data = insect_sprays, x = 'spray', y = 'count', kind = 'box')

# 3 Load the swiss dataset and read it's documentation. The swiss dataset is available from pydatset 
# rather than seaborn. 
swiss = data('swiss')
swiss.head()

#swiss["Catholic"].describe()
# Create an attribute named is_catholic that holds a boolean value of whether or not the province 
# is Catholic. (Choose a cutoff point for what constitutes catholic)
#is_catholic = [swiss.Catholic >= 50]
# Create the new column based on an existing column.

swiss['is_catholic'] = swiss.Catholic > 50

# Does whether or not a province is Catholic influence fertility?
# sns.boxplot (x='is_catholic', y= 'Fertility', data=swiss)
# sns.pairplot(data = swiss, hue = 'Fertility',  corner = True)
swiss.corr().Fertility

