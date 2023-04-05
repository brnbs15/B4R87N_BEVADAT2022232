import pandas as pd
import seaborn as sns

from typing import Tuple
from scipy.stats import mode
from  sklearn.metrics import confusion_matrix, euclidean_distances

class KNNClassifier:

    
    @property
    def k_neighbors(self):
        return self.k

    def __init__(self,k:int,test_split_ratio:float):
        self.k=k
        self.test_split_ratio=test_split_ratio


    @staticmethod
    def load_csv(csv_path:str) -> Tuple[pd.DataFrame,pd.DataFrame]:
        df = pd.read_csv(csv_path)
        df = df.sample(random_state=42,frac=1)  
        x = df.iloc[:,:-1]
        y = df.iloc[:,-1]
        return x,y
    
    def train_test_split(self,features:pd.DataFrame,labels:pd.DataFrame) -> None:
        
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        x_train,y_train = features.iloc[:train_size,:],labels.iloc[:train_size]
        x_test,y_test = features.iloc[train_size:,:],labels.iloc[train_size:]
        self.x_train, self.y_train, self.x_test, self.y_test = x_train, y_train, x_test, y_test
    
    def euclidean(self,element_of_x:pd.DataFrame):
        return ((self.x_train - element_of_x)**2).sum(axis=1)**0.5
    
    def predict(self,x_test:pd.DataFrame):
        labels_pred = []
        for x_test_row in x_test.iterrows():
              distances = self.euclidean(x_test_row)
              distances = pd.DataFrame(sorted(zip(distances,self.y_train)))

              label_pred = mode(distances.iloc[:self.k,1],keepdims=False)
              labels_pred.append(label_pred)

        self.y_preds = pd.DataFrame(labels_pred).iloc[:,0]

    def accuracy(self)->float:
        true_positive = (self.y_test.reset_index(drop=True) == self.y_preds.reset_index(drop=True)).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix
    