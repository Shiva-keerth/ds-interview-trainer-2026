from utils.ui_components import run_training_module

def render():
    subtopics = [
        "CNN vs RNN Architectural Differences",
        "Mitigating Vanishing/Exploding Gradients",
        "Understanding Transformers & Attention Mechanisms",
        "Transfer Learning Best Practices in 2026"
    ]
    run_training_module("Deep Learning Basics", subtopics, "dl")
