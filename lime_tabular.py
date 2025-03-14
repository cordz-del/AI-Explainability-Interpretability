# examples/lime_tabular_example.py
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from lime.lime_tabular import LimeTabularExplainer

# Load dataset and train a classifier
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
class_names = iris.target_names

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

# Create a LIME Tabular Explainer
explainer = LimeTabularExplainer(X, feature_names=feature_names, class_names=class_names, discretize_continuous=True)

# Choose an instance to explain
i = 25
exp = explainer.explain_instance(X[i], clf.predict_proba, num_features=2)
exp.show_in_notebook(show_table=True)
