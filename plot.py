import matplotlib.pyplot as plt
from function import add

x = list(range(10))
y = add(x,x)

plt.plot(x,y)
plt.savefig("plot.png")
