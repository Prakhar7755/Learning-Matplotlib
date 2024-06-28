import matplotlib.pyplot as plt
import numpy as np

sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# day one, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y, color =  '#88c999',s = sizes)


# day two, the age and speed of 15 cars:
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

plt.scatter(x, y, color =  'r',s = sizes)

""" NOTE : The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter. """

""" By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives. """


#  ColorMap




plt.title("Scatter Graph")
plt.xlabel("Car Age")
plt.ylabel("speed")
plt.scatter(x, y)
plt.show()
