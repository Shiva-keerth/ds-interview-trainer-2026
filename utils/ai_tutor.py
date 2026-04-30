import os
import json
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

class AITutor:
    def __init__(self):
        self.api_key = os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            st.error("GROQ_API_KEY is missing. Please add it to your .env file.")
            st.stop()
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"
        
        # System prompt setting the standard to 2026 and predicting trends
        self.system_prompt = """
        You are an elite, highly critical Senior Data Scientist conducting interviews for Top Tier Tech companies in the year 2026.
        Your goal is to rigorously test a fresher Data Scientist. 
        
        CRITICAL INSTRUCTIONS:
        1. Context: It is 2026. The field of Data Science expects freshers to not just know theory, but practical implementation, 
           business logic, edge cases, scalability, and integration with modern architectures (LLMs, scalable systems).
        2. Trend Prediction: You should generate questions that are not just standard 2020s questions, but predictive 
           of the challenges they will face in upcoming 2026/2027 interviews. Focus on nuanced, real-world problems.
        3. No easy textbook definitions. Present scenario-based questions, code debugging, or architectural trade-offs.
        """

    def _call_groq(self, prompt, json_mode=False):
        try:
            kwargs = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
            }
            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}
                
            response = self.client.chat.completions.create(**kwargs)
            content = response.choices[0].message.content
            
            if json_mode:
                return json.loads(content)
            return content
        except Exception as e:
            st.error(f"Error communicating with AI: {e}")
            return None

    def generate_lesson(self, main_topic, subtopic):
        prompt = f"""
        You are a Senior Data Scientist at a Top Tech Company in 2026 compiling an internal wiki.
        Teach a highly condensed, hyper-practical "Masterclass" on this exact subtopic: "{subtopic}" (Category: {main_topic}).
        
        Requirements:
        1. Keep it concise but comprehensive (around 500-700 words). Ensure all underlying concepts needed to understand this topic are briefly covered.
        2. Explain the core concept simply.
        3. Explain the BUSINESS USE-CASE (Why do companies care about this in 2026?).
        4. Provide an extremely clear Python/SQL code snippet demonstrating it in practice.
        5. Add a "Interview Trap" warning (What do freshers usually get wrong about this?).
        
        Format as beautiful Markdown. Do NOT wrap it in a JSON block, just output the raw markdown.
        """
        return self._call_groq(prompt, json_mode=False)

    def generate_question(self, topic, subtopic, lesson_text=None):
        prompt = f"""
        Generate ONE highly realistic, moderately difficult scenario-based interview question for a Fresher Data Scientist 
        applying in 2026. The topic is: {topic}. The specific focus must be: {subtopic}.
        """
        
        if lesson_text:
            prompt += f"""
        CRITICAL CONSTRAINT: The user has just read the following masterclass on the topic. The scenario you generate MUST be solvable using MAINLY the concepts, theories, and techniques taught in this text. You are testing if they understood this specific lesson, do NOT require major outside knowledge that wasn't covered.
        
        <masterclass>
        {lesson_text}
        </masterclass>
        """

        prompt += """
        Requirements:
        1. Base it on real-world practical datasets, business contexts, or common production failures.
        2. Do NOT ask for simple definitions. Ask them to solve a problem.
        3. Make it predictive of mid-to-late 2026 interview trends for this topic.
        
        Return ONLY a JSON object with this exact format:
        {
            "question": "The detailed scenario and question text",
            "context": "Any brief background data or code snippet if necessary (or empty string)"
        }
        """
        result = self._call_groq(prompt, json_mode=True)
        return result if result else {"question": "Could not generate question.", "context": ""}

    def generate_hint(self, question, context):
        prompt = f"""
        The user is struggling with this interview question:
        Question: {question}
        Context: {context}
        
        Provide a very short, conceptual hint to point them in the right direction without giving away the direct answer.
        Keep it under 2 sentences. Do not use markdown backticks around the text.
        """
        return self._call_groq(prompt, json_mode=False)

    def evaluate_answer(self, question, context, user_answer, topic):
        prompt = f"""
        Topic: {topic}
        Question: {question}
        Context: {context}
        User's Answer: {user_answer}
        
        Evaluate the user's answer critically as a Senior Data Scientist in 2026. 
        Freshers are expected to be sharp, precise, and practical.
        
        Return ONLY a JSON object with this exact format:
        {{
            "score": <an integer from 0 to 10>,
            "feedback": "A concise paragraph explaining what was good and what was missing/wrong.",
            "ideal_answer": "A clear, beautifully structured ideal answer they should have given."
        }}
        """
        result = self._call_groq(prompt, json_mode=True)
        return result if result else {"score": 0, "feedback": "Evaluation failed.", "ideal_answer": ""}
