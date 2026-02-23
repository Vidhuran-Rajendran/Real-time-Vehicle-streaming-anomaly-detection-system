import numpy as np
import time

def generate_telemetry_data(vehicle_id):
    # Simulate telemetry data for a vehicle
    while True:
        yield {
            'vehicel_id': vehicle_id,
            'engine_temp':np.random.normal(loc=90, scale=5),  # Simulate engine temperature
            'rpm': np.random.normal(loc=3000, scale=500),  # Simulate RPM
            'vibration': np.random.normal(0.3,0.05),
            'timestamp': time.time()
        }
        
        time.sleep(0.5)  # Simulate delay between telemetry data points