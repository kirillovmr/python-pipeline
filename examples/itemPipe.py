import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))

from smart_pipeline import Pipeline

data = [1,2,3,4,5]

# Define an item function
def addOne(item):
    return item + 1

pl = Pipeline()

# Adds function into pipeline
pl.addItemPipe(addOne)
res = pl(data)

for item in res:
    print(item)