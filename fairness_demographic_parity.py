# examples/fairness_demographic_parity.py
import numpy as np
from fairlearn.metrics import demographic_parity_difference

# Simulated true labels and predictions, with group membership (e.g., 0 and 1 represent two groups)
true_labels = np.array([1, 0, 1, 1, 0, 0, 1, 0])
predictions = np.array([1, 0, 0, 1, 0, 1, 1, 0])
sensitive_features = np.array([0, 0, 1, 1, 0, 0, 1, 1])

dp_diff = demographic_parity_difference(true_labels, predictions, sensitive_features=sensitive_features)
print(f"Demographic Parity Difference: {dp_diff:.4f}")
