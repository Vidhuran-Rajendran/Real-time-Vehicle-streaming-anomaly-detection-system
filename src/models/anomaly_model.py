from sklearn.ensemble import IsolationForest
import joblib

class AnomalyModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.02, random_state=42)
        
    def train_set(self,X):
        self.model.fit(X)
    
    def scores(self,X):
        return self.model.predict([X])[0]
    
    def save(self,path):
        joblib.dump(self.model,path)
        
    def load(self,path):
        self.model = joblib.load(path)
        