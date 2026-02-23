import numpy as np
from src.models.anomaly_model import AnomalyModel
from src.features.window_features import extract_features   
from src.generator.telementry_generator import generate_telemetry_data
from src.streaming.stream_processor import SlidingWindow

if __name__ == "__main__":
    window = SlidingWindow(window_size=20)
    model = AnomalyModel()
    generator = generate_telemetry_data(vehicle_id="VH001")
    
    feature_matrix = []
    
    for _ in range(2000):
        data = next(generator)
        win = window.updates(data)
        
        if len(win) < 20:
            continue
        
        features = extract_features(win)
        feature_matrix.append(features)
        
    X = np.array(feature_matrix)
    model.train_set(X)
    model.save("model/isolation_forest_model.pkl")

    print("Model training completed and saved to model/isolation_forest_model.pkl")