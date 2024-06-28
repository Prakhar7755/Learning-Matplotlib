import matplotlib.pyplot as plt
import numpy as np


y = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(y,"o")
# plt.plot(y,marker="o")
# plt.plot(y,marker="*")
# plt.plot(y,marker="3")


# FORMAT STRINGS fmt    marker/line/color

# plt.plot(y, 'o:r')
# plt.plot(y, 'o-.r')
# plt.show()

"""     Line Reference
Line Syntax	Description
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line

Note: If you leave out the line value in the fmt parameter, no line will be plotted.
"""

#  COLOR REFERENCE
""" The short color value can be one of the following:

Color Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White """


#   MARKER SIZE You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
""" 
plt.plot(y,marker="o", markersize=20)
plt.plot(y,marker="o", ms=20)
plt.show()
 """


# MARKER COLOR - You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
""" 
plt.plot(y,marker="o",ms=20,mec="r")
"""

#  You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
plt.plot(y, marker="o", color="yellow", ms=20, mfc="green", mec="red")


plt.show()
