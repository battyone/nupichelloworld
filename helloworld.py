from nupic.research.flat_spatial_pooler import FlatSpatialPooler as FP
from nupic.research.spatial_pooler import SpatialPooler
import numpy as np

print "hello"

flat=FP()
n=np.array([1]*1024)

print np.size(n)
flat.compute(n,True,n)
