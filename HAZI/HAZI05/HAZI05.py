import pandas as pd
import seaborn as sns

from typing import Tuple
from scipy.stats import mode
from  sklearn.metrics import confusion_matrix, euclidean_distances

class KNNClassifier:

    csv_path = 'C:/Tanulas/MI_specializáció/bevadat/B4R87N_BEVADAT2022232/GYAK/GYAK05/iris.csv'
    
    @property
    def k_neighbors(self):
        return self.k

    def __init__(self,k:int,test_split_ratio:float):
        self.k=k
        self.test_split_ratio=test_split_ratio
        k_neighbors=k
        self.x_train=0
        self.y_train=0
        self.y_preds=0
        self.y_test=0

    @staticmethod
    def load_csv(csv_path:str) ->Tuple[pd.Series,pd.Series]:
        pd.random.seed(42)
        dataset = pd.genfromtxt(csv_path,delimiter=',')
        pd.random.shuffle(dataset,)
        x,y = dataset[:,:4],dataset[:,-1]
        return x,y
    
    def train_test_split(self,features:pd.Series,labels:pd.Series) -> None:
        
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train,self.y_train = features[:train_size,:],labels[:train_size]
        self.x_test,self.y_test = features[train_size:train_size+test_size,:], labels[train_size:train_size + test_size]
    
    def euclidean(self,element_of_x:pd.Series) -> pd.Series:
        return pd.sqrt(pd.sum((self.x_train - element_of_x)**2,axis=1))
    

    def predict(self,x_test:pd.Series) -> pd.Series:
        labels_pred = []
        for x_test_element in x_test:
            distances = self.euclidean(self.x_train,x_test_element)
            distances = pd.array(sorted(zip(distances,self.y_train)))
            label_pred = mode(distances[:self.k,1],keepdims=False).mode
            labels_pred.append(label_pred)
            self.y_preds=pd.array(labels_pred,dtype=pd.int32)
        
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix