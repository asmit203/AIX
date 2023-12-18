import joblib
import numpy as np
import os

class ModelManager:
    def __init__(self, filename=None):
        if os.path.exists(filename):
            self.filename=filename
        else:self.filename=None
        self._model=None
        self.prediction=None
        self._scaler=None
    
    def load(self):
        if self.filename!=None:
            loaded_model=joblib.load(self.filename)
            self._model=loaded_model

    def Load(self, filename):
        if os.path.exists(filename):
            self.filename=filename
            self.load()
        return self
    
    # method to load scalers like scikit-learn StandardScaler
    def load_scaler(self, filename):
        loaded_scaler=joblib.load(filename)
        self._scaler=loaded_scaler
    
    def predict(self, feature):
        feature=np.array([feature])

        if (self._model!=None):
            
            if (self._scaler!=None):
                prediction=self._scaler.transform(feature)

            prediction=self._model.predict(feature)[0]
            self.prediction=prediction

            return self.prediction
        
        else: return None
      
    def clear(self):
        self.filename=None
        self._model=None
        self.predict=None

    def isActive(self):
        return False if (self._model==None) else True