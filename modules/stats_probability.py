from utils.ui_components import run_training_module

def render():
    subtopics = [
        "A/B Testing (Sample size & Statistical Significance)",
        "Understanding p-values & Type I/Type II Errors",
        "Normal vs Skewed Distributions in Real Data",
        "Bayes' Theorem Applications in Data Science"
    ]
    run_training_module("Statistics & Probability", subtopics, "stats")
