import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_answer(transcript, role="Software Engineer"):
    prompt = f"""
    You are an AI interviewer for a {role} position. Analyze the following interview answer:

    \"{transcript}\"

    Give feedback on:
    - Confidence
    - Relevance
    - Communication
    - Structure

    Format:
    Strengths:
    Weaknesses:
    Suggestions:
    Score (out of 10):
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

