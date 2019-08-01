import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))

from smart_pipeline import Pipeline

data = [1,2,3,4,5]

# Function that goes over all items in dataset
def countNumberStat(stats, item):
    stats["total"] += 1
    if item%2==0:
        stats["even"] += 1
    else:
        stats["odd"] += 1
    return stats

# Function to be called at the end with accumulated stats
def printNumberStat(stats):
    print(stats["total"], "items were processed in total.")
    print(stats["even"], "of them are even.")
    print(stats["odd"], "of them are odd")

# Make sure to pass initial state as 3rd argument
pl = Pipeline()
pl.addStatPipe(countNumberStat, printNumberStat, { "total":0, "even":0, "odd":0 })
pl(data)
