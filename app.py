# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: Lebogang
"""

import streamlit as st

# App title and intro
st.title("Student Mental Wellness Dashboard")

st.markdown(
    """
    ### 📘 Motivation Behind the App

    This application is motivated by **Chapters 4 and 5** of my Honours research study, 
    which focused on the **statistical analysis of the onset of depression among university students**.

    The app is designed to translate statistical insights into a **simple, non-diagnostic tool** 
    that promotes **early awareness, self-reflection, and proactive support-seeking** among students.
    """
)

st.sidebar.title("🧠 MindTrack")
st.sidebar.write("Student Mental Wellness Dashboard")
st.sidebar.markdown("---")
st.sidebar.write("Daily Check-In")
st.sidebar.write("Wellness Score")
st.sidebar.write("Support & Feedback")

st.header("📝 Daily Wellness Check-In")

col1, col2 = st.columns(2)

with col1:
    mood = st.slider("Mood (1 = Very Low, 5 = Very Good)", 1, 5)
    sleep = st.slider("Hours of Sleep Last Night", 0, 10)

with col2:
    stress = st.slider("Stress Level (1 = Low, 5 = Very High)", 1, 5)
    energy = st.slider("Energy Level (1 = Very Low, 5 = Very High)", 1, 5)

st.header("📊 Wellness Score")

wellness_score = (mood * 20) + (energy * 15) + (sleep * 5) - (stress * 15)
wellness_score = max(0, min(100, wellness_score))

st.metric(label="Overall Wellness Score", value=f"{wellness_score}/100")
st.progress(wellness_score)

st.header("🚦 Wellness Feedback")

if wellness_score >= 70:
    st.success("You are doing well 🌱 Keep maintaining healthy habits.")

elif wellness_score >= 40:
    st.warning("You may be feeling somewhat overwhelmed. Consider rest and self-care.")

else:
    st.error("You may be at risk of burnout. Please consider seeking support.")

    if stress >= 4:
        st.info(
            "High stress levels detected. If these feelings persist, "
            "consider speaking to a trusted person or a professional."
        )

st.markdown("---")
st.caption(
   "💙 Disclaimer: This app does not diagnose mental health conditions. "
    "It is designed to encourage self-awareness, self-care, and self-love. "
    "Your feelings matter, and seeking support is a sign of strength."
)

