# examples/shap_tree_example.py
import shap
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Load data and train model
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Create TreeExplainer and compute SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Plot summary for one class (e.g., class 0)
shap.summary_plot(shap_values[0], X, feature_names=iris.feature_names)
