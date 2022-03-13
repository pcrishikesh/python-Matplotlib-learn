import matplotlib.pyplot as mp

x = [5,10,15]
y = [10,20,30]

mp.subplot(2,2,1)
mp.plot(x,y)
mp.grid()

mp.subplot(2,2,2)
mp.plot(x,y)
mp.grid()

mp.subplot(2,2,3)
mp.plot(x,y)
mp.grid()

mp.subplot(2,2,4)
mp.plot(x,y)
mp.grid()


mp.show()



