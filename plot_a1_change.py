import numpy as np
import pylab as pl
from matplotlib import collections  as mc

lines = [[(2, 1), (2, 2)], [(4, 2), (4, 8)], [(1, 4), (5, 8)]]
c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lc = mc.LineCollection(lines, colors=c, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
pl.show()
