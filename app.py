import streamlit as st
# Assuming maigret.py has been structured as a module or package
# and has a function named `run_maigret` that takes a nickname and returns results
from maigret import run_maigret

st.title("Maigret Web Version")
nickname_input = st.text_input("Enter nickname", "…")
if st.button("Start"):
    nickname = nickname_input.title()
    try:
        # Directly call a function from maigret.py (assuming it's structured appropriately)
        result = run_maigret(nickname)
        st.text_area("Results", result, height=300)
    except Exception as e:
        st.error(f"An error occurred: {e}")
