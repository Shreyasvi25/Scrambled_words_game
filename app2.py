import streamlit as st
import random

# Sample word list
words = ["python", "streamlit", "calendar", "mobile", "interface", "github", "science", "scramble", "winner", "network"]

# Initialize session state
if "current_word" not in st.session_state:
    st.session_state.current_word = ""
    st.session_state.scrambled_word = ""

# Function to shuffle the letters
def scramble(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

# Function to pick a new word
def new_word():
    st.session_state.current_word = random.choice(words)
    st.session_state.scrambled_word = scramble(st.session_state.current_word)

# Title
st.title("🧠 Word Scramble Game")

# Button to get a new word
if st.button("🔁 New Word"):
    new_word()

# Show the scrambled word
if st.session_state.scrambled_word:
    st.subheader("🔤 Unscramble this:")
    st.markdown(f"### `{st.session_state.scrambled_word}`")

    user_input = st.text_input("Your Guess:")

    if st.button("✅ Check Answer"):
        if user_input.lower() == st.session_state.current_word.lower():
            st.success("🎉 Correct!")
        else:
            st.error(f"❌ Wrong! The correct word was: `{st.session_state.current_word}`")
