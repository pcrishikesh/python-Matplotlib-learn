import matplotlib.pyplot as ps

y_aex = [0,10,4,20]
y2_aex = [0,12 ,17, 25]
marker = "*"
ls = "--"
linewidth = "20.5"
color1 = "#0aff4b"
color2 = "#d6b654"


ps.plot(y2_aex, color2)
ps.plot( y_aex, color1)

ps.xlabel("hello guys")
ps.ylabel("hello friends")
ps.title("GUYZZ")
ps.grid()

ps.show()
