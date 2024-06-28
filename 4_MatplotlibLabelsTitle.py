import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# FONTS FOR TITLE AND LABELS
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# TITLE AND LABELS WITH FONT AND LOCATIONS
plt.title("Sports Watch Data", fontdict=font1, loc='right')
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)


plt.plot(x, y, c="red", lw=2, ls="-")
plt.show()
