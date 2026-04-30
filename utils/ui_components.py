import streamlit as st
from utils.ai_tutor import AITutor

def run_training_module(topic_name, subtopics, session_key_prefix):
    st.markdown(f'<div class="main-header">{topic_name}</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Select a curated subtopic below to begin your AI Masterclass.</div>', unsafe_allow_html=True)
    
    # State flags
    mode_key = f"{session_key_prefix}_mode" # "syllabus", "learn", "test"
    sub_key = f"{session_key_prefix}_selected_subtopic"
    lesson_key = f"{session_key_prefix}_lesson"
    q_key = f"{session_key_prefix}_question"
    c_key = f"{session_key_prefix}_context"
    h_key = f"{session_key_prefix}_hint"
    e_key = f"{session_key_prefix}_eval"
    a_key = f"{session_key_prefix}_answer_text"
    
    if mode_key not in st.session_state:
        st.session_state[mode_key] = "syllabus"
        st.session_state[sub_key] = None
        st.session_state[lesson_key] = None
        st.session_state[q_key] = None
        st.session_state[c_key] = None
        st.session_state[h_key] = None
        st.session_state[e_key] = None
        st.session_state[a_key] = ""

    tutor = AITutor()

    # ==========================================
    # STAGE 0: SYLLABUS LIST
    # ==========================================
    if st.session_state[mode_key] == "syllabus":
        st.markdown("<br>", unsafe_allow_html=True)
        for i, sub in enumerate(subtopics):
            st.markdown(f"""
            <div class="premium-card">
                <h4 style="color: #00FF88; margin-bottom: 5px;">Module {i+1}: {sub}</h4>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Begin Module {i+1} 📖", key=f"{session_key_prefix}_start_{i}"):
                st.session_state[sub_key] = sub
                st.session_state[mode_key] = "learn"
                st.session_state[lesson_key] = None # Reset lesson to force generation
                st.session_state[q_key] = None
                st.session_state[e_key] = None
                st.rerun()

    # ==========================================
    # STAGE 1: LEARN MODE
    # ==========================================
    elif st.session_state[mode_key] == "learn":
        st.markdown(f"### 📖 Masterclass: {st.session_state[sub_key]}")
        
        if st.button("⬅️ Back to Syllabus", key=f"back_{session_key_prefix}"):
            st.session_state[mode_key] = "syllabus"
            st.rerun()
            
        st.markdown("---")
        
        if st.session_state[lesson_key] is None:
            with st.spinner("Generating 2026 Masterclass..."):
                lesson = tutor.generate_lesson(topic_name, st.session_state[sub_key])
                st.session_state[lesson_key] = lesson
                st.rerun()
        else:
            st.markdown(st.session_state[lesson_key])
            st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
            st.info("When you feel confident with this material, put your skills to the test.")
            if st.button("⚔️ Test My Knowledge", type="primary", key=f"test_{session_key_prefix}"):
                st.session_state[mode_key] = "test"
                with st.spinner("Generating hyper-realistic scenario..."):
                    resp = tutor.generate_question(topic_name, st.session_state[sub_key], st.session_state[lesson_key])
                    st.session_state[q_key] = resp.get("question", "")
                    st.session_state[c_key] = resp.get("context", "")
                    st.session_state[a_key] = ""
                    st.session_state[h_key] = None
                st.rerun()

    # ==========================================
    # STAGE 2: PRACTICE / TEST MODE
    # ==========================================
    elif st.session_state[mode_key] == "test":
        st.markdown(f"### ⚔️ Challenge: {st.session_state[sub_key]}")
        if st.button("⬅️ Back to Lesson", key=f"back2_{session_key_prefix}"):
            st.session_state[mode_key] = "learn"
            st.rerun()
            
        st.markdown("---")
        
        if st.session_state[q_key]:
            st.markdown(f"**Scenario:**  \n{st.session_state[q_key]}")
            if st.session_state[c_key]:
                st.code(st.session_state[c_key])
                
            # Hint mechanism
            if not st.session_state[e_key]:
                if st.button("💡 Need a Hint?", key=f"hint_{session_key_prefix}"):
                    with st.spinner("Analyzing context..."):
                        hint = tutor.generate_hint(st.session_state[q_key], st.session_state[c_key])
                        st.session_state[h_key] = hint
                
                if st.session_state[h_key]:
                    st.warning(f"**Hint:** {st.session_state[h_key]}")
            
            # User Answer
            if not st.session_state[e_key]:
                user_answer = st.text_area("Your 2026 Senior Data Scientist Response:", value=st.session_state[a_key], height=200, key=f"input_{session_key_prefix}")
                
                if st.button("Submit Answer", type="primary", key=f"sub_{session_key_prefix}"):
                    if len(user_answer.strip()) < 10:
                        st.error("Too short. Provide a comprehensive answer.")
                    else:
                        st.session_state[a_key] = user_answer
                        with st.spinner("Evaluating your response..."):
                            evaluation = tutor.evaluate_answer(
                                st.session_state[q_key], 
                                st.session_state[c_key], 
                                user_answer, 
                                topic_name
                            )
                            st.session_state[e_key] = evaluation
                            st.session_state.overall_score += evaluation.get("score", 0)
                            st.session_state.questions_answered += 1
                            st.rerun()
                            
            # Evaluation state
            else:
                st.markdown("### 🎯 AI Evaluation")
                eval_data = st.session_state[e_key]
                
                score = eval_data.get('score', 0)
                color = "green" if score >= 8 else "orange" if score >= 5 else "red"
                st.markdown(f"**Score:** <span style='color:{color}; font-size:24px; font-weight:bold;'>{score}/10</span>", unsafe_allow_html=True)
                
                st.markdown("#### Feedback")
                st.write(eval_data.get('feedback', 'No feedback provided.'))
                
                with st.expander("Show Ideal Senior Data Scientist Answer"):
                    st.success(eval_data.get('ideal_answer', 'No ideal answer provided.'))
                
                if st.button("Finish & Return to Syllabus", key=f"finish_{session_key_prefix}"):
                    st.session_state[mode_key] = "syllabus"
                    st.session_state[e_key] = None
                    st.rerun()
