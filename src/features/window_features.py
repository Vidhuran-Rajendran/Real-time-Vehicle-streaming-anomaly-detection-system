import numpy as np

def extract_features(window):
    temps = [x["engine_temp"]for x in window]
    rpms = [x["rpm"] for x in window]
    vib = [x["vibration"] for x in window]
    
    return [
        np.mean(temps),
        np.std(temps),
        np.mean(rpms),
        np.std(rpms),
        np.mean(vib),
        np.std(vib)
    ]