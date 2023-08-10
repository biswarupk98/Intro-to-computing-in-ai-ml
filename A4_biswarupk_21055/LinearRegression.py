import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self) -> None:
        self._coeff = None
        self._intercept = None
        

    def __repr__(self) -> str:
        return "Linear Regression Model from  Parent Class"

    def predict(self, X_new):
        """Output model prediction.

        Arguments:
        X_new: 1D or 2D numpy array
        """
        if len(X_new.shape) == 1: # check if X is 1D or 2D array
            X_new = X_new.reshape(-1,1) #reshape to column vector if 1D 

        # Code starts
        self._predicted = self._intercept +  X_new.dot(self._coeff)
        self._Xnew = X_new
        # Code Ends
        return self._predicted
    
    
    def error_metrics(self):
        self._fit  = np.dot(self._feature,self._coeff)+self._intercept
        self._residue = self._target - self._fit

        # Code starts
        self._sse = np.sum(np.matmul(self._residue,self._residue))
        
        # Code Ends
        print(f"Sum of squared error for best fit: {self._sse}\n")
        
        # Code starts
        self._mse = self._sse / len(self._feature)
        
        # Code Ends
        print(f"Mean squared error for best fit: {self._mse}\n")
    
    def fit_plot(self):
        #
        #
        # Fill your code here
        #
        #
        # Code Starts
        X_plot = np.array([[-100],[100]])
        Y_plot = np.array([[-100],[100]])
        plt.plot(X_plot,Y_plot,"r--",linestyle ="dashed")
        
       
        plt.scatter(self._target, self._fit, color = "blue",s = 35, marker='o', alpha=.45)
        plt.xlabel("True Values")
        plt.ylabel("fit values")
        plt.title("True vs Fit values")
        
        # Code Ends
        plt.savefig("Fit_Plot.jpg")
        plt.show()

        