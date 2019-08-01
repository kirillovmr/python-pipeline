from tqdm import tqdm
import time

class Pipeline:
    def __init__(self):
        self.pipes = []
    
    # Applies all the functions in pipeline to each element. Returns modified array
    def __call__(self, data):
        for (func, pipeType) in self.pipes:
            if pipeType == 'i':
                data = list(map(func, tqdm(data, desc=func.__name__)))
            elif pipeType == 'd':
                data = list(filter(func, tqdm(data, desc=func.__name__)))
            elif pipeType == 's':
                (reducer,printer,initializer) = func
                self.__reduce(reducer, printer, tqdm(data, desc=reducer.__name__), initializer)
                time.sleep(2) # To display stats normally
        return data
    
    # Adds function to Pipe.process pipeline
    def addItemPipe(self, func):
        if hasattr(func, '__call__'):
            # arg func is <class 'function'>
            self.pipes.append((func, 'i'))
            
    def addDataPipe(self, func):
        if hasattr(func, '__call__'):
            # arg func is <class 'function'>
            self.pipes.append((func, 'd'))
            
    def addStatPipe(self, reducer, printer, initializer):
        if hasattr(reducer, '__call__') and hasattr(printer, '__call__'):
            # arg func is <class 'function'>
            self.pipes.append(((reducer,printer,initializer),'s'))
            
    def __reduce(self, reducer, printer, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            try:
                initializer = next(it)
            except StopIteration:
                raise TypeError('reduce() of empty sequence with no initial value')
        accum_value = initializer
        for x in it:
            accum_value = reducer(accum_value, x)
        # Last iteration
        printer(accum_value)