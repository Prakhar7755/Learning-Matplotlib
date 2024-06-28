import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)  # to generate random data

plt.hist(x)
plt.show()
