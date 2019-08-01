# Python Data Pipeline

Process any type of data in your projects easily, control the flow of your data!

![Python 3.5, 3.6, 3.7](https://img.shields.io/badge/python-3.5%2C%203.6%2C%203.7-blue.svg)
[![PyPI version](https://badge.fury.io/py/smart-pipeline.svg)](https://badge.fury.io/py/smart-pipeline)

---

### Installation
Install `smart-pipeline` with:
``` bash
pip install -U smart-pipeline
```

### Usage
Package 'smart_pipeline' provides a Pipeline class:
``` python
# Import Pipeline class
from smart_pipeline import Pipeline

# Create an instance
pl = Pipeline()
```

Pipeline class has 3 types of pipes: item, data and stat.

**Item pipe** modifies each item in dataset without changing the whole population of data:
```python
data = [1,2,3,4,5]

# Define an item function
def addOne(item):
    return item + 1

# Adds function into pipeline
pl.addItemPipe(addOne)
# Pass the data through pipeline
res = pl(data)

# res = [2,3,4,5,6]
```

**Data pipe** is a filter:
``` python
data = [1,2,3,4,5]

def onlyOdd(item):
    return False if item%2==0 else True

pl.addDataPipe(onlyOdd)
res = pl(data)

# res = [1,3,5]
```

**Stat pipe** reduces over the data, passing the accumulated value to each element:
``` python
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
pl.addStatPipe(countNumberStat, printNumberStat, { "total":0, "even":0, "odd":0 })
pl(data)

# Output:
# 5 items were processed in total.
# 2 of them are even.
# 3 of them are odd
```

---
### [Check out some examples](https://github.com/kirillovmr/python-pipeline/tree/master/examples)
---

If this library solved some of your problems, please consider starring the project 😉

And feel free to create pull requests!