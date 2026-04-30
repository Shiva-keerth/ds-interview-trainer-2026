from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Vectorized Operations vs Standard Loops (Performance)",
        "Advanced Feature Engineering on Text/Dates",
        "Handling Missing Data (Imputation Strategies)",
        "Memory Optimization for Large Pandas DataFrames"
    ]
    run_training_module("Python & Pandas", subtopics, "pandas")
