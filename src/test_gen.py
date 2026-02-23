from src.generator.telementry_generator import generate_telemetry_data

gen = generate_telemetry_data("TEST123")
print(next(gen))