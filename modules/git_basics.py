from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Resolving Complex Merge Conflicts in Jupyter Notebooks",
        "Branching Strategies for Data Science Teams (GitFlow)",
        "Version Control for Data and ML Models (DVC basics)",
        "Writing Standardized Commit Messages and PR Reviews"
    ]
    run_training_module("Git Basics", subtopics, "git")
