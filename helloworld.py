from nupic.research.flat_spatial_pooler import FlatSpatialPooler as FP
from nupic.research.spatial_pooler import SpatialPooler
import numpy as np
from random import randrange

print "hello"

flat=FP()
n=np.array([0])
act=np.array([0])
for i in range(1023):	#An array of 0s and 1s generated randomly. 1024 long
  n=np.append(n,[randrange(2)])
for i in range(64*64):
  active=np.append(active,[0])	#64*64 because that is the number of columns. Created just to supply it as a parameter to compute()
 
print np.size(n) 
print np.size(act)
flat.compute(n,True,act)
flat.printFlatParameters()