import numpy as np

class StandardScaler:
    def __init__(self):
        self.mean=None
        self.std=None
    def transform(self,x):
        self.mean=np.mean(x,axis=0)
        self.std=np.std(x,axis=0)
        self.range=x-self.mean
        return self.range/self.std



