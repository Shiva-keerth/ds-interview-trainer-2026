# 🧠 2026 Data Scientist Interview Trainer

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)
![Groq](https://img.shields.io/badge/AI_Engine-Groq_Llama3-orange)

An elite, highly predictive AI-powered interview preparation platform specifically engineered to simulate the rigorous interview standards of Top Tier Tech companies in 2026. 

Traditional textbook definitions are outdated. This platform uses the **Groq API (llama-3.3-70b-versatile)** to generate hyper-realistic, scenario-based questions focusing on business logic, production failures, and edge cases.

## ✨ Core Features

* **30-Day Curated Syllabus:** Covers 11 critical skill domains required for 2026 Data Science roles.
* **AI Masterclasses:** Generates dense, 500-700 word lessons highlighting core concepts, business use-cases, and common "Fresher Traps".
* **Predictive Scenario Testing:** Replaces generic questions with complex, moderately difficult production scenarios.
* **Senior Data Scientist Persona:** The AI acts as a highly critical senior interviewer, grading answers out of 10 and providing an "Ideal Answer" for comparison.
* **Premium UI:** Features a dynamic, modern dashboard built entirely within Streamlit using custom CSS injection.

## 🗂️ Modules Included

* **Phase 1 (Fundamentals):** SQL Trainer, Statistics & Probability, Python + Pandas, ML Theory
* **Phase 2 (Advanced):** ML Algorithms, EDA & Data Viz, Deep Learning, NLP Basics, Case Studies
* **Phase 3 (Industry & Ops):** Git Basics, Gen AI / Prompting, Project Deployment
* **Ultimate Mock Interview:** Mixed domain, rapid-fire scenario testing.

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* A valid `GROQ_API_KEY`

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Shiva-keerth/ds-interview-trainer-2026.git
cd ds-interview-trainer-2026
```

2. Install the required dependencies:
```bash
pip install streamlit groq python-dotenv
```

3. Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_api_key_here
```

4. Launch the application:
```bash
streamlit run app.py
```

## 🏗️ Architecture

The application relies on a modular architecture:
* `app.py`: Main routing and premium UI CSS injection.
* `utils/ai_tutor.py`: The core LLM engine containing the strict prompt engineering required for the 2026 persona.
* `utils/ui_components.py`: The reusable Learn/Test state machine UI workflow.
* `modules/`: Individual skill domains dynamically injected into the core UI workflow.

## 🤝 Contributing
This project is currently maintained by Shiva-keerth. Contributions, issues, and feature requests are welcome.

## 📜 License
Distributed under the MIT License.
