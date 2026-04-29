import streamlit as st
import os

st.set_page_config(page_title="2026 DS Interview Trainer", page_icon="🧠", layout="wide")

# ==========================================
# SUPER PREMIUM UI INJECTION
# ==========================================
st.markdown("""
<style>
    /* Global Typography from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Dashboard container styles */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f1f5f9;
    }
    
    /* Header styling */
    .main-header {
        font-size: 3rem;
        background: -webkit-linear-gradient(45deg, #00FF88, #60A5FA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #94a3b8;
        margin-top: 5px;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Transform Radio Buttons into Premium Tab Pills */
    div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        padding: 12px 15px;
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid rgba(255,255,255,0.05);
        transition: all 0.2s ease;
        cursor: pointer;
    }
    div[role="radiogroup"] > label:hover {
        background: rgba(255, 255, 255, 0.1);
        border-left: 4px solid #00FF88;
        transform: translateX(4px);
    }
    
    /* Hide the actual circular radio indicator completely */
    div[role="radiogroup"] > label > div:first-child {
        display: none; 
    }
    /* Style the text inside the radio tabs */
    div[role="radiogroup"] > label p {
        font-weight: 600;
        color: #e2e8f0;
        margin-left: 0px !important;
        font-size: 0.95rem;
    }
    
    /* Cards and Containers */
    .premium-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .premium-card:hover {
        transform: translateY(-2px);
        border: 1px solid rgba(0, 255, 136, 0.4);
    }
    
    /* Score Badge */
    .score-badge {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        padding: 15px 20px;
        border-radius: 12px;
        font-size: 2rem;
        color: white;
        font-weight: 800;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.4);
        margin: 20px 0;
    }
    
    /* Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.4);
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
        box-shadow: 0 6px 8px -1px rgba(59, 130, 246, 0.6);
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# State initialization
if "overall_score" not in st.session_state:
    st.session_state.overall_score = 0
if "questions_answered" not in st.session_state:
    st.session_state.questions_answered = 0

# ==========================================
# SIDEBAR CURRICULUM NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: white;'>📋 30-Day Syllabus</h2>", unsafe_allow_html=True)
    
    module = st.radio(
        "Select Module:",
        [
            "🏠 Home Dashboard",
            "📊 P1: SQL Trainer",
            "📈 P1: Stats & Probability",
            "🤖 P1: Machine Learning Theory",
            "🐼 P1: Python + Pandas",
            "⚙️ P1: ML Algorithms",
            "👀 P2: EDA & Data Viz",
            "🧠 P2: Deep Learning",
            "🗣️ P2: NLP Basics",
            "💼 P2: Case Studies",
            "🔥 P3: Git Basics",
            "✨ P3: Gen AI / Prompting",
            "🚀 Bonus: Project Deployment (Free & Paid)",
            "⏱️ Ultimate Mock Interview"
        ]
    )
    
    st.markdown("---")
    st.markdown("<h3 style='color: white;'>Your Progress</h3>", unsafe_allow_html=True)
    if st.session_state.questions_answered > 0:
        avg_score = st.session_state.overall_score / st.session_state.questions_answered
        st.markdown(f'<div class="score-badge">{avg_score:.1f}/10</div>', unsafe_allow_html=True)
        st.caption(f"Tested on {st.session_state.questions_answered} scenarios")
    else:
        st.info("Start training to generate your 2026 DS Score.")

# ==========================================
# MAIN ROUTING
# ==========================================
if module == "🏠 Home Dashboard":
    st.markdown('<div class="main-header">2026 Data Scientist Trainer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Learn concepts via AI Masterclasses, then test your skills with hyper-realistic scenarios.</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-card">
        <h3 style='color: #60A5FA;'>Welcome to the New Architecture</h3>
        <p>This system replaces generic answering with heavily structured learning. Here is how it works:</p>
        <ol>
            <li>Select a topic from the sidebar (All 11 skills from your 30-day roadmap are included).</li>
            <li>Choose a subtopic curated specifically for 2026 interviews.</li>
            <li><strong>Learn Mode:</strong> Absorb a 2-minute masterclass generated by the AI tutor on exactly what you need to know.</li>
            <li><strong>Practice Mode:</strong> Immediately face a difficult, predictive scenario based on the masterclass.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

else:
    # Dynamically import the module based on selection
    try:
        if module == "📊 P1: SQL Trainer":
            from modules import sql_trainer
            sql_trainer.render()
            
        elif module == "🤖 P1: Machine Learning Theory":
            from modules import ml_theory
            ml_theory.render()
            
        elif module == "🐼 P1: Python + Pandas":
            from modules import python_pandas
            python_pandas.render()
            
        elif module == "📈 P1: Stats & Probability":
            from modules import stats_probability
            stats_probability.render()
            
        # Phase 1 & 2 & 3 Routings Complete
        elif module == "⚙️ P1: ML Algorithms":
            from modules import ml_algorithms
            ml_algorithms.render()
        elif module == "👀 P2: EDA & Data Viz":
            from modules import eda
            eda.render()
        elif module == "🧠 P2: Deep Learning":
            from modules import deep_learning
            deep_learning.render()
        elif module == "🗣️ P2: NLP Basics":
            from modules import nlp
            nlp.render()
        elif module == "💼 P2: Case Studies":
            from modules import case_studies
            case_studies.render()
        elif module == "🔥 P3: Git Basics":
            from modules import git_basics
            git_basics.render()
        elif module == "✨ P3: Gen AI / Prompting":
            from modules import genai_prompting
            genai_prompting.render()
        elif module == "🚀 Bonus: Project Deployment (Free & Paid)":
            from modules import deployment
            deployment.render()
        elif module == "⏱️ Ultimate Mock Interview":
            from modules import mock_interview
            mock_interview.render()
            
    except Exception as e:
        st.error(f"Error loading module: {e}")
