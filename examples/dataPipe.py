import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))

from smart_pipeline import Pipeline

data = [1,2,3,4,5]

# Define a data function
def onlyOdd(item):
    return False if item%2==0 else True

pl = Pipeline()

# Adds function into pipeline
pl.addDataPipe(onlyOdd)
res = pl(data)

for item in res:
    print(item)