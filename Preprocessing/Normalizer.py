import numpy as np

class MinMaxNormalizer:
    def __init__(self):
        self.min=None
        self.max=None
    def transform(self, X):
        self.min=np.min(X,axis=0)
        self.max=np.max(X,axis=0)
        self.range=self.max-self.min
        self.range[self.range==0]=1
        return (X-self.min)/self.range

    