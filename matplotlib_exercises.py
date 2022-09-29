#import pyplot module as alias plt
import matplotlib.pyplot as plt  

#import other libraries 
import numpy as np
import math
from random import randint
import random
import pandas as pd
%config InlineBackend.figure_format = 'retina'

# 1 Use matplotlib to plot the following equation:
#y = x ** 2 − x + 2
# You'll need to write the code that generates the x and y points.
#Add an anotation for the point 0, 0, the origin.

x = list(range(-49, 50))
y = [(x ** 2 - x + 2) for x in x]
plt.scatter(x, y)
plt.title('Parabola')
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.annotate('Origin', xy=(0, 0), xytext=(0, 300),
             arrowprops={'facecolor': 'blue'})
plt.show()

#save the figure
#plt.savefig('figure1.png')

### 2. Create and label four separate charts for the following equations (choose a range for x that makes sense)

# y=√x
x = list(range(0, 100))
y= [np.sqrt(x) for x in x]
fig, ax = plt.subplots()
ax.set_title('$y=√x$')
ax.plot(x, y)
plt.show()

#y=2**x
x = list(range(0, 10))
y = [(2 ** x) for x in x]
fig, ax = plt.subplots()
ax.set_title('$y=2^x$')
ax.plot(x, y)
plt.show()

#y=x**3
x = list(range(0, 10))
y= [(x ** 3) for x in x]
fig, ax = plt.subplots()
ax.set_title('$y=x^3$')
ax.plot(x, y)
plt.show()

# 1/(x+1)
x = list(range(0, 10))
y = [(1/(n+1)) for n in x]
fig, ax = plt.subplots()
ax.set_title('$1/(x+1)$')
ax.plot(x, y)
plt.show()

# 3 Combine the figures you created in the last step into one large figure with 4 subplots.
x = list(range(0, 10))
y1 = [(2 ** x) for x in x]
y2 = [(x ** 3) for x in x]
y3 = [np.sqrt(x) for x in x]
y4 = [(1/(n+1)) for n in x]

plt.figure(figsize = (10,6))
plt.suptitle('More Math Functions')

plt.subplot(221)
plt.plot(x, y1,color = 'r', ls = '--')
plt.title('$y=2^x$')

plt.subplot(222)
plt.plot(x, y2,color = 'b', ls = '--', marker = '^')
plt.title('$y=x^3$')

plt.subplot(223)
plt.plot(x, y3,color = 'g', ls = '--', marker = 'o')
plt.title('$y=√x$')

plt.subplot(224)
plt.plot(x, y4,color = 'm', ls = '--', marker = 'v')
plt.axhline(0, color = 'm')
plt.fill_between(x, y4, color = 'm', alpha= 0.9)
plt.title('$1/(x+1)$')

# alpha = controls transperancy

plt.tight_layout()
plt.show()

#4 Combine the figures you created in the last step into one figure where each of the 4 
# equations has a different color for the points. Be sure to include a legend and an appropriate title for the figure.

x = range(0, 5)
two_squared = [(2 ** x) for x in x]
sqr_rt_x = [(x ** 3) for x in x]
x_cubed = [np.sqrt(x) for x in x]
inverse_x_plus_one = [(1/(n+1)) for n in x]

plt.figure(figsize=(14, 6)) # (width, height)

plt.plot(x, two_squared, c='blue', label='$y=2^x$')
plt.plot(x, sqr_rt_x, c='orange', label ='$y=x^3$')
plt.plot(x, x_cubed, c='green', label='$y=√x$')
plt.plot(x, inverse_x_plus_one, c='red', label='$1/(x+1)$')


plt.legend(loc='upper right')
plt.title('Four Functions Together')
plt.xlabel('$x$')

plt.show()

