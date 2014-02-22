from nupic.research.flat_spatial_pooler import FlatSpatialPooler as FP
from nupic.research.spatial_pooler import SpatialPooler
import numpy as np
import sys
from random import randrange

class Example:
  
  def __init__(self):
    
    self.inputArray=np.zeros(32*32)	#Will be our input. Initializing to zeros 
    self.activeArray=np.zeros(64*64)	#To be passed to compute. Initialized to 0. The result, that is the active columns, will be represented by this array (later)
    self.flat=FP()			#An instance of our flat spatial pooler. A flat spatial pooler does not implement topology. More details will be added
    
  def create_input(self):
    #We clear the already existing inputArray before we create a new one
    self.inputArray[0:]=0
    
    for i in range(1023):
      self.inputArray[i]=randrange(2)	#randrange() returns a random integer within the range. In this case, its either 0 or 1
    
  def run(self):
    #Apply the input vector to the spatial pooler
    #What happens is that, flat.compute() does all the calculations and set the indices of activeArray is 1 if the corresponding column is active
    #For example, if column 1248 is a winner, then activeArray[1248]=1
    self.flat.compute(self.inputArray,True,self.activeArray)
    #To see the active columns
    self.print_results()  
    
    
  def print_results(self):
    #Get the results of the spatial pooling
    #Printing the columns that are active after each step
    for i in range(4096):	
      if self.activeArray[i]!=0:
	print i,
    print "\n*****Next set*****"
    


#Running our example  
example=Example()

for i in range(10):	#We supply 10 different input vectors
  example.create_input()
  example.run()		

    
    
    
    
    
    
