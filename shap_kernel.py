# examples/shap_kernel_example.py
import shap
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Load data and train model
iris = load_iris()
X, y = iris.data, iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Create KernelExplainer (using a small subset for efficiency)
explainer = shap.KernelExplainer(model.predict_proba, X[:50])
shap_values = explainer.shap_values(X[:5])

# Plot SHAP values for the first instance
shap.force_plot(explainer.expected_value[0], shap_values[0][0], iris.feature_names, matplotlib=True)
plt.show()
