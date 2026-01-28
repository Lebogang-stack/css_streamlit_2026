# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello!")

st.title("Welcome to my first App")

st.write("Your first streamlit App")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)

st.write(f"You picked: {number}")
