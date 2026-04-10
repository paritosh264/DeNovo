import numpy as np 
from sklearn.model_selection import train_test_split
class train_test_split:
    def __init__(self,x,y,test_size=0.2,random_state=None,suffle=True):
        self.x=x
        self.y=y
        self.random_state=random_state
        self.suffle=suffle
        self.testsize=test_size
        if self.random_state!=None:
        
                 np.random.seed(self.random_state)
        indexes=np.arange(len(x))
        if(self.suffle==True):
                 np.random.shuffle(indexes)
                 size=int(len(x)*(1-self.testsize))
                 xtrain=x[indexes[:size]]
                 xtest=x[indexes[size:]]
                 ytrain=y[indexes[:size]]
                 ytest=y[indexes[size:]]
        else:
                 size=int(len(x)*self.testsize)
                 xtrain=x[indexes[:size]]
                 xtest=x[indexes[size:]]
                 ytrain=y[indexes[:size]]
                 ytest=y[indexes[size:]]
               
        self.result=(xtrain ,xtest,ytrain,ytest)
    def __iter__(self):
           return iter(self.result)
    
