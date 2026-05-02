from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Identifying Data Leakage & Hidden Biases during EDA",
        "Visualizing High-Dimensional Data (PCA & t-SNE)",
        "Outlier Detection & Treatment Strategies",
        "Translating Visual Insights to Business Actions"
    ]
    run_training_module("EDA & Data Visualization", subtopics, "eda")
