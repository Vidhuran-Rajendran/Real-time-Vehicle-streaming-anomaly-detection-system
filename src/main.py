from src.monitoring.logger import log_event
from src.monitoring.drif import DriftDetector
from src.models.anomaly_model import AnomalyModel
from src.features.window_features import extract_features   
from src.generator.telementry_generator import generate_telemetry_data
from src.streaming.stream_processor import SlidingWindow

window = SlidingWindow(window_size=20)
drift_detector = DriftDetector()
model = AnomalyModel()
model.load(r"E:\training\streamin_anomaly\model\isolation_forest_model.pkl")

generator = generate_telemetry_data(vehicle_id="VH001")

for data in generator:
    win = window.updates(data)
    
    if len(win) < 20:
        continue
    features = extract_features(win)
    anomaly = model.scores(features)
    drift = drift_detector.update(features)
    log_event(data['vehicle_id'], anomaly, drift)