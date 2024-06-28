import matplotlib.pyplot as plt
import numpy as np
# Linestyle -  You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:


y = np.array([3, 8, 1, 10])

# plt.plot(y, linestyle='dotted')
# plt.plot(y, linestyle='dashed')
# plt.plot(y, ls=':')
# plt.plot(y, ls='--')


# LINECOLOR :  You can use the keyword argument color or the shorter c to set the color of the line:

# plt.plot(y, ls='--',color="yellow")
# plt.plot(y, ls='-.',c="#4CAF50")






# LINE WIDTH -  You can use the keyword argument linewidth or the shorter lw to change the width of the line.


plt.plot(y, ls='-',c="#4CAF50",lw="20.5")

plt.show()
