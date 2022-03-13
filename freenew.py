import matplotlib.pyplot as pl

x = [2,10,12,15,19]
y = [105,134,156,167,178]

color_for_dot = [10,20,50,70,90]

pl.scatter(x,y, c=color_for_dot, cmap="viridis")

pl.colorbar()
pl.show()