from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Window Functions for Time-Series Analysis",
        "Complex JOINs on Incomplete/Dirty Data",
        "Query Optimization (Explain Plans & Indexing)",
        "CTEs and Subqueries for Multi-step Analytics"
    ]
    run_training_module("Advanced SQL", subtopics, "sql")
