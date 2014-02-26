"""A simple program that demonstrates the working of the spatial pooler"""
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

from nupic.research.spatial_pooler import SpatialPooler as SP
import numpy as np
from random import randrange

class Example():
  
  """A class to hold our code. Going object oriented"""
  
  def __init__(self, inputShape, columnDimensions):
    """
     Parameters:
     ----------
     _inputShape	:	The size of the input. The product of the first and second elements of this parameter determines the size of the input vectors
     _columnDimensions:	The size of the 2 dimensional array of columns
     """
    self.inputShape = inputShape
    self.columnDimensions = columnDimensions
    self.inputSize = np.array(inputShape).prod()
    self.columnNumber = np.array(columnDimensions).prod()
    self.inputArray = np.zeros(self.inputSize)
    self.activeArray = np.zeros(self.columnNumber)

    self.sp = SP(self.inputShape, 
		 self.columnDimensions,
		 potentialRadius = self.inputSize,
		 numActiveColumnsPerInhArea = int(0.02*self.columnNumber),
		 globalInhibition = True,
		 synPermActiveInc = 0.01
		 )
    
  def create_input(self):
    """create a random input vector"""
    
    #clear the inputArray to zero before creating a new input vector
    self.inputArray[0:] = 0
    
    for i in range(self.inputSize):
      #randrange returns 0 or 1
      self.inputArray[i] = randrange(2)
      
  def run(self):
    """Run the spatial pooler with the input vector"""
    
    #activeArray[column]=1 if column is active after spatial pooling
    self.sp.compute(self.inputArray, True, self.activeArray)
    
    print self.activeArray.nonzero() 
    
example = Example((32, 32), (64, 64))

#Trying random vectors
for i in range(3):
  example.create_input()
  example.run()
  
#Trying identical vectors
for i in range(3):
  example.run()