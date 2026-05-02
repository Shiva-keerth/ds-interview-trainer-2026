from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Modern Tokenization Strategies (BPE, WordPiece)",
        "Word Embeddings vs Contextualized Embeddings",
        "Handling Sarcasm and Nuance in Sentiment Analysis",
        "Fine-tuning vs Prompting for Specific NLP Tasks"
    ]
    run_training_module("NLP Basics", subtopics, "nlp")
