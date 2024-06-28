# Creating Pie Charts => With Pyplot, you can use the pie() function to draw pie charts:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
""" Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:

The value divided by the sum of all values: x/sum(x) """

# LABELS AND STARTANGLE
# plt.pie(y, labels=mylabels, startangle=90)


# explode and shadow
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=mylabels, startangle=90, colors=mycolors, explode=myexplode, shadow=True)


plt.legend(title = "Four Fruits:")


plt.show()
