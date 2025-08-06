# Placeholder for app.py
import streamlit as st
from utils.whisper_record import transcribe_audio
from utils.evaluate_answer import evaluate_answer
from utils.export_report import save_feedback_pdf

st.title("🎤 AI Interview Simulator")

uploaded_audio = st.file_uploader("Upload your interview audio", type=["mp3", "wav", "m4a"])

if uploaded_audio:
    st.audio(uploaded_audio)
    transcript = transcribe_audio(uploaded_audio)
    st.subheader("📝 Transcript")
    st.write(transcript)

    st.subheader("🧠 Feedback")
    feedback = evaluate_answer(transcript)
    st.text(feedback)

    if st.button("📥 Download PDF Report"):
        save_feedback_pdf(feedback)
        st.success("✅ Report saved as 'interview_feedback.pdf'")
