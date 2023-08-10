from LinearRegression1D import *
from NormalEquation import *
from sklearn import datasets


M = 1 #No. of features. Set M = 1 to test LinearRegression1D
N = 100 #No. of Samples

x, y, coef = datasets.make_regression(n_samples=N,#number of samples
                                      n_features=M,#number of features
                                      n_informative=M,#number of useful features 
                                      noise=25,#bias and standard deviation of the guassian noise
                                      coef=True,#true coefficient used to generated the data
                                      random_state=42) #set for same data 


#mlr = LinearRegression1D() #Un-comment to fit using LinearRegression1D
mlr = NormalEquation()   #Un-comment to fit using NormalEquation
mlr.fit(x,y)
mlr.error_metrics()
mlr.fit_plot()                                    



