from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Framing a Business Problem as an ML Problem",
        "Designing Metrics for Recommender Systems",
        "Balancing False Positives vs False Negatives in Production",
        "Evaluating the Financial ROI of an ML Model"
    ]
    run_training_module("Case Studies & Business Thinking", subtopics, "cases")
