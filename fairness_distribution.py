# examples/fairness_distribution.py
import numpy as np

def compute_group_distribution(predictions, sensitive_features):
    groups = np.unique(sensitive_features)
    distributions = {}
    for group in groups:
        group_preds = predictions[sensitive_features == group]
        distributions[group] = np.mean(group_preds)  # e.g., mean probability of positive prediction
    return distributions

# Example data
predictions = np.array([0.9, 0.3, 0.8, 0.2, 0.7, 0.4, 0.95, 0.1])
sensitive_features = np.array([0, 0, 1, 1, 0, 0, 1, 1])

distributions = compute_group_distribution(predictions, sensitive_features)
print("Prediction distributions by group:", distributions)
