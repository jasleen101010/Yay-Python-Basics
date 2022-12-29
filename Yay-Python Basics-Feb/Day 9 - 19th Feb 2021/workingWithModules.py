# Importing the Modules
import pyModules as pymod                        # [Renaming the Module]
from collections import Counter                  # Built-In Module
import numpy as np

# Working with Content of that Particular Module
print(pymod.randomFunction(7, 8))
print(pymod.anotherFunction(7, 8))
print(pymod.randomVariable)

# Working with Built-In Modules
aParticularList = [1, 2, 3, 1, 2, 3, 1, 1 , 1, 4]
print(f"Getting Occurences for 1: {Counter(aParticularList)[1]}")

# Working with Externally Installed Modules
numpyArray = np.arange(5)
print(f"Numpy Array: {numpyArray}")
