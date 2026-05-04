from utils.ui_components import run_training_module

def render():
    subtopics = [
        "Free: Deploying Streamlit Apps via Community Cloud",
        "Free/Paid: Web Services via Render or Railway (Docker)",
        "Paid: AWS EC2 & SageMaker for Production ML Models",
        "Architecture: Wrapping ML Models in FastAPI"
    ]
    run_training_module("Model & App Deployment Strategies", subtopics, "deploy")
