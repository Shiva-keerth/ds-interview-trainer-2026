from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Bias-Variance Tradeoff in Production",
        "Overfitting vs Underfitting (Real-world indicators)",
        "Cross-validation Strategies for Imbalanced Data",
        "Choosing the Right Evaluation Metric (F1, ROC-AUC, PR-AUC)"
    ]
    run_training_module("Machine Learning Theory", subtopics, "ml_theory")
