# examples/lime_text_example.py
from lime.lime_text import LimeTextExplainer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample dataset
texts = [
    "I love this product, it's amazing!",
    "This is the worst experience I've ever had.",
    "Absolutely fantastic service.",
    "I am very disappointed and upset."
]
labels = [1, 0, 1, 0]  # 1: positive, 0: negative

# Create a text classification pipeline
vectorizer = TfidfVectorizer()
classifier = LogisticRegression()
pipeline = make_pipeline(vectorizer, classifier)
pipeline.fit(texts, labels)

explainer = LimeTextExplainer(class_names=["negative", "positive"])
idx = 1  # Explain the second sample
exp = explainer.explain_instance(texts[idx], pipeline.predict_proba, num_features=6)
exp.show_in_notebook(text=True)
