import matplotlib.pyplot as plt
import numpy as np
""" 
The subplot() Function
The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
"""
# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
plt.subplot(2, 1, 1)
plt.title("SALES")
plt.plot(x, y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
plt.subplot(2, 1, 2)
plt.title("INCOME")
plt.plot(x, y)


""" 
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
"""
plt.suptitle("MY SHOP")
plt.show()
