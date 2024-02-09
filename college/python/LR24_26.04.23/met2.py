import pylab
from mpl_toolkits.mplot3d import Axes3D

def makeData():
    x = pylab.arange(-10, 10, 0.5)
    y = pylab.arange(-10, 10, 0.5)
    xgrid, ygrid = pylab.meshgrid(x, y)
    zgrid = pylab.sin(xgrid * 0.3) * pylab.cos(ygrid * 0.75)
    return xgrid, ygrid, zgrid

if __name__ == "__main__":
    fig = pylab.figure()
    axes = fig.add_subplot(projection='3d')
    axes.plot_surface(*makeData(), rstride=1, cstride=1)
    pylab.show()