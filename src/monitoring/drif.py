import numpy as np

class DriftDetector:
    def __init__(self):
        self.reference_mean = None
        
    def update(self,feature_vector):
        current_mean = np.mean(feature_vector)
        if self.reference_mean is None:
            self.reference_mean = current_mean
            return False
        drift = abs(current_mean - self.reference_mean) > 0.5  # Simple threshold for drift detection
        return drift > 5
    