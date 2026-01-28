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





st.write("A simple app to help students reflect on their mental wellness.")
st.write("This app does not provide medical diagnosis.")

st.header("Daily Wellness Check-In")

# Sliders for mental wellness inputs
mood = st.slider("Mood (1 = Very Low, 5 = Very Good)", 1, 5)
stress = st.slider("Stress Level (1 = Low, 5 = Very High)", 1, 5)
sleep = st.slider("Hours of Sleep Last Night", 0, 10)
energy = st.slider("Energy Level (1 = Very Low, 5 = Very High)", 1, 5)

# Display selected values
st.write("### Your Inputs")
st.write(f"Mood: {mood}")
st.write(f"Stress: {stress}")
st.write(f"Sleep: {sleep} hours")
st.write(f"Energy: {energy}")

# Wellness score calculation
wellness_score = (mood * 20) + (energy * 15) + (sleep * 5) - (stress * 15)

# Keep score within 0–100
wellness_score = max(0, min(100, wellness_score))

st.header("Wellness Score")
st.progress(wellness_score)
st.write(f"Your wellness score is: **{wellness_score}/100**")

# Feedback based on score
st.header("Wellness Feedback")

if wellness_score >= 70:
    st.success("You are doing well 🌱 Keep maintaining healthy habits.")
elif wellness_score >= 40:
    st.warning("You may be feeling a bit overwhelmed. Consider resting and self-care.")
else:
    st.error("You may be at risk of burnout. Please consider reaching out for support.")

if stress >= 4:
        st.info(
            "You indicated high stress levels. If this continues, consider "
            "talking to a trusted friend, family member, or a professional."
        )

