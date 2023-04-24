import numpy as np


class LinearRegression:

    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.m = 0
        self.c = 0
        self.epochs = epochs
        self.lr = lr
        self.casualties = []

    def fit(self, X: np.array, Y: np.array):
        n = float(len(X)) 
        
        for i in range(self.epochs): 
            Y_pred = self.m * X + self.c

            leftovers = Y - Y_pred
            loss = np.sum(leftovers ** 2)
            self.casualties.append(loss)
            m_derivative= (-2/n) * sum(X * leftovers)
            c_derivative = (-2/n) * sum(leftovers)
            self.m = self.m - self.lr * m_derivative 
            self.c = self.c - self.lr * c_derivative
        return self.casualties
        
    def predict(self, X):
        return self.m * X + self.c
    
    def evaluate(self, X, Y):
        prediction = self.predict(X)
        return np.mean((prediction - Y)**2)
    