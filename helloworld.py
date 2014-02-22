from nupic.research.flat_spatial_pooler import FlatSpatialPooler as FP
import numpy as np

print "hello"

flat=FP((2,2))
n=np.array([1]*1024)

print np.size(n)
flat.compute(n,True,n)
