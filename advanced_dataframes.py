#Import
import pandas as pd
import numpy as np
from pydataset import data
np.random.seed(123)

## Exercise 1

# 1 Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)

# Create a function named get_db_url. It should accept a username, hostname, password, and database name 
#  and return a url connection string 
# formatted like in the example at the start of this lesson.
#from env import host, user, password
def get_db_url(db):
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return url

## 3 Use your function to obtain a connection to the employees database.

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)

sql = '''
SELECT
    *
FROM employees
'''
employees_df = pd.read_sql(sql, url)
employees_df.head()


#7 How many rows and columns do you have in each DataFrame? Is that what you expected?
employees_df.shape

sql = '''
SELECT
    *
FROM titles
'''
titles_df = pd.read_sql(sql, url)
titles_df.head()

titles_df.shape

# 8 Display the summary statistics for each DataFrame.
print(titles_df.describe)

# 9 How many unique titles are in the titles DataFrame?
titles_df.title.unique()

#10 What is the oldest date in the to_date column?
#titles_df.sort_values(by='to_date' == )
titles_df[titles_df.to_date == titles_df.to_date.min()]

#11 What is the most recent date in the to_date column?
#titles_df[titles_df.to_date == titles_df.to_date.max()]
titles_df.sort_values(by=['to_date'], ascending = False)

## Exercises II

#Copy the users and roles DataFrames from the examples above.
# 1 Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# 2 What is the result of using a right join on the DataFrames?
# Perform an outer join specifying the left and right DataFrame keys.

users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)


# 3 What is the result of using an outer join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)

# 4 What happens if you drop the foreign keys from the DataFrames and try to merge them?

pd.merge(users, roles,
        how='outer',
        indicator=True)


# 5 Load the mpg dataset from PyDataset.
mpg = data('mpg') # load the dataset and store it in a variable


# 6 Output and read the documentation for the mpg dataset.
data('mpg', show_doc=True) # view the documentation for the dataset

# 7 How many rows and columns are in the dataset?
mpg.shape

# 8 Check out your column names and perform any cleanup you may want on them.
mpg.rename(columns={'cty': 'city'}, inplace = True)
mpg.rename(columns={'hwy': 'highway'}, inplace = True)
mpg.rename(columns={'cyl': 'cylinder'}, inplace = True)
mpg.rename(columns={'trans': 'transmission'}, inplace = True)
mpg.rename(columns={'displ': 'displacement'}, inplace = True)
mpg.rename(columns={'drv': 'drive'}, inplace = True)
mpg.head()

# 9 Display the summary statistics for the dataset.
print(mpg.describe()) 
print(mpg.info())

# 10 How many different manufacturers are there?
#mpg_makes = mpg["manufacturer"].unique()
make_unique = mpg['manufacturer'].nunique() 
#or
mpg.manufacturer.nunique()

# 11 How many different models are there?
model_unique = mpg['model'].nunique() 
#or
mpg.model.nunique()

# 12 Create a column named mileage_difference like you did in the DataFrames exercises; 
# this column should contain the difference between highway and city mileage for each car.

mpg = mpg.assign(mileage_difference = (mpg['highway']-mpg['city'])) 
#or
mpg ['mileage_difference'] = mpg.highway - mpg.city

# 13 Create a column named average_mileage like you did in the DataFrames exercises; this is the 
# mean of the city and highway mileage.
# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg["average_mileage"] = (mpg.highway + mpg.city) /2
#or
mpg = mpg.assign(average_mileage = (mpg['highway'] + mpg['city']) / 2) 
#try this harmonic mean
mpg['average_mileage'] = round (2/ ((1/mpg.highway) + (1/mpg.city)), 2)

# 14 Create a new column on the mpg dataset named is_automatic that holds boolean values denoting 
# whether the car has an automatic transmission.
mpg.transmission.unique()
mpg["is_automatic"] = mpg["transmission"].str.contains("auto")

# 15 Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg.groupby("manufacturer").average_mileage.mean().nlargest()
# Honda

#16 Do automatic or manual cars have better miles per gallon?
# Choose only two columns for my subset.

mpg['transmission_catgeory'] = np.where (mpg.transmission.str.contains('auto'),'automatic', 'manual')


## Exercises Part III

# 1 Use your get_db_url function to help you explore the data from the chipotle database.
def get_db_url():
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    return url

orders_df = pd.read_sql('SELECT * FROM orders', url)
orders_df

# 2 What is the total price for each order?
#change datatype of column, clean columns
#orders_df['item_price'] = orders_df['item_price'].str.replace('$', '')
#orders_df['item_price'] = orders_df['item_price'].astype(float)
order_totals = orders_df.groupby('order_id').item_price.sum()
#or orders_df['item_price'] = orders_df['item_price'].str.replace('$', '').astype[float]

# 3 What are the most popular 3 items?
orders_df.groupby('item_name').quantity.sum().sort_values(ascending = False).head(3)

# 4 Which item has produced the most revenue?
item_revenue = orders_df.groupby('item_name').item_price.sum()
item_revenue.nlargest(1)

# 5 Join the employees and titles DataFrames together.

from env import host, user, password
url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    
def get_db_url():
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    return url

sql = '''
SELECT
    *
FROM employees
'''
employees = pd.read_sql(sql, url)
employees.head()

sql = '''
SELECT
    *
FROM titles
'''
titles = pd.read_sql(sql, url)
titles.head()

from env import host, user, password
url = f'mysql+pymysql://{user}:{password}@{host}/employees'

# 5 Join the employees and titles DataFrames together.
# Perform an outer join specifying the left and right DataFrame keys.

#employees.merge(titles, left_on='emp_no', right_on='emp_no', how='inner', indicator=True)
merged_df = employees.merge(titles, left_on='emp_no', right_on='emp_no', how='inner')

def get_db_url(db):
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return url

# 6 For each title, find the hire date of the employee that was hired most recently with that title.
merged_df.groupby("title").hire_date.max()

# 7 Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas 
# code to perform the manipulations.)

#sql = '''
#SELECT
#    *
#FROM departments
#'''
#departments = pd.read_sql(sql, url)
#departments.head()
dept_title_query = '''
                    SELECT t.emp_no,
                    t.title,
                    t.to_date,
                    d.dept_name
                    FROM departments AS d
                    JOIN dept_emp AS de USING(dept_no)
                    JOIN titles as t USING(emp_no)

'''
dept_titles = pd.read_sql(dept_title_query, get_db_url('employees'))
dept_titles.head()

get_db_url('employees')

