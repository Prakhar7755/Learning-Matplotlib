import matplotlib.pyplot as plt
import numpy as np
""" cSpell:disable """
"""       SYNTAX
x = []
y = []
plt.bar(x, y)
plt.show()
 """
x = ["Python", "C", "Java", "TypeScript"]
y = [85, 65, 75, 60]
z = [45, 55, 45, 50]
c = ['y', 'b', 'm', 'r']

plt.xlabel("Languages", fontsize=15)
plt.ylabel("Popularity", fontsize=15)
plt.title("LET'S SEE", fontsize=15)


# plt.bar(x, y, width=0.5, color=c,align="edge")
# plt.bar(x, y, width=0.5, color=c,align="center")
# plt.bar(x, y, width=0.5, color=c,edgecolor="black",linewidth=5,linestyle=":",alpha=0.3);

width = 0.6

plt.barh(x, y, width, color="r", label="Programming Languages")

plt.barh(x, z, width, color="green", label="Programming Languages 2")

plt.legend()
plt.show()
