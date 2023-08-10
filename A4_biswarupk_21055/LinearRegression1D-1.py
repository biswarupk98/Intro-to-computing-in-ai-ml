from LinearRegression import *

class LinearRegression1D(LinearRegression):
    
    def fit(self,X,y):
        
        self._feature = X
        self._target = y
        m = len(X)
        
        # Code starts
        #self._coeff = (np.sum(self._target)*np.sum(np.matmul(self._feature,self._feature)) - np.sum(self._feature)*np.sum(np.matmul(self._feature,self._target)))/(m * np.sum(np.matmul(self._feature,self._feature)) - (np.sum(self._feature))**2)
        
        self._intercept = (sum(y)*sum(X**2) - sum(X)*np.matmul(y,X))/(m*sum(X**2)-(sum(X))**2)
        
        self._coeff = (m*np.matmul(y,X) - sum(X)*sum(y))/(m*sum(X**2)-(sum(X))**2) 
        # Code Ends
        print(f"Fit intercept: {self._intercept}\n")
        print(f"Fit coefficients: {self._coeff}\n")
        
