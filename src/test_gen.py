from src.generator.telementry_generator import generate_telemetry_data

# quick sanity check to ensure generator yields correct keys
if __name__ == "__main__":
    gen = generate_telemetry_data("TEST123")
    sample = next(gen)
    print(sample)
    assert 'vehicle_id' in sample, "Expected 'vehicle_id' key in telemetry data"
    print("Generator produces correct key.")