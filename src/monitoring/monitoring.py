def log_metrics(total, anomalies):
    if total > 0:
        print(f"processed {total} data points, detected {anomalies/total:.3f} anomalies")
    else:
        print("No data points processed.")