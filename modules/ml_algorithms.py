from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Random Forest vs Gradient Boosting (XGBoost/LightGBM)",
        "Tuning Hyperparameters for Tree-based Models",
        "Support Vector Machines (SVM) Kernels & Margins",
        "K-Means Clustering vs DBSCAN in practice"
    ]
    run_training_module("ML Algorithms", subtopics, "ml_algo")
