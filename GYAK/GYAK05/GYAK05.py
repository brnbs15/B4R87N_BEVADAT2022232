import numpy as np
import seaborn as sns

from typing import Tuple
from scipy.stats import mode
from  sklearn.metrics import confusion_matrix

class KNNClassifier:

    csv_path = 'C:/Tanulas/MI_specializáció/bevadat/B4R87N_BEVADAT2022232/GYAK/GYAK05/iris.csv'

    def __init__(self,k:int,test_split_ratio:float):
        self.k=k
        self.test_split_ratio=test_split_ratio

    def load_csv(csv_path:str) ->Tuple[np.ndarray,np.ndarray]:
        np.random.seed(42)
        dataset = np.genfromtxt(csv_path,delimiter=',')
        np.random.shuffle(dataset,)
        x,y = dataset[:,:4],dataset[:,-1]
        return x,y
    
    x,y = load_csv(csv_path)
    
    np.mean(x,axis=0),np.var(x,axis=0)
    
    np.nanmean(x,axis=0),np.nanvar(x,axis=0)

    x[np.isnan(x)] = 3.5
    x.shape

    np.mean(x,axis=0),np.var(x,axis=0)
    
    (x > 13.0).sum(), (x < 0.0).sum()

    x[np.where(np.logical_or(x > 13.0,x < 0.0))]

    less_than = np.where(x < 0.0)
    higher_than = np.where(x > 13.0)
    less_than,higher_than

    y = np.delete(y,np.where(x < 0.0)[0],axis=0)
    y = np.delete(y,np.where(x > 13.0)[0],axis=0)
    x = np.delete(x,np.where(x < 0.0)[0],axis=0)
    x = np.delete(x,np.where(x > 13.0)[0],axis=0)
    x.shape,y.shape


    def train_test_split(features:np.ndarray,labels:np.ndarray,test_split_ratio:float) -> None:
        
        test_size = int(len(features) * test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        x_train,y_train = features[:train_size,:],labels[:train_size]
        x_test,y_test = features[train_size:train_size+test_size,:], labels[train_size:train_size + test_size]
        return (x_train,y_train,x_test,y_test)
    
    def euclidean(points:np.ndarray,element_of_x:np.ndarray) -> np.ndarray:
        return np.sqrt(np.sum((points - element_of_x)**2,axis=1))
    

    def predict(x_train:np.ndarray,y_train:np.ndarray,x_test:np.ndarray,k:int) -> np.ndarray:
        labels_pred = []
        for x_test_element in x_test:
            distances = euclidean(x_train,x_test_element)
            distances = np.array(sorted(zip(distances,y_train)))
            label_pred = mode(distances[:k,1],keepdims=False).mode
            labels_pred.append(label_pred)
            return np.array(labels_pred,dtype=np.int32)
        
    def accuracy(y_test:np.ndarray,y_preds:np.ndarray) -> float:
        true_positive = (y_test == y_preds).sum()
        return true_positive / len(y_test) * 100
    
    def plot_confusion_matrix(y_test:np.ndarray,y_preds:np.ndarray):
        conf_matrix = confusion_matrix(y_test,y_preds)
        sns.heatmap(conf_matrix,annot=True) 
    


