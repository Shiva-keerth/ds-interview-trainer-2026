from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Zero-Shot vs Few-Shot Prompting Strategies",
        "Chain of Thought (CoT) Prompting for Reasoning Tasks",
        "Prompt Injection & Security Vulnerabilities",
        "Evaluating LLM Outputs & Halucination Mitigation"
    ]
    run_training_module("Gen AI & Prompting", subtopics, "genai")
