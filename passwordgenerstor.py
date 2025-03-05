"""import streamlit as st
import random
import string

def password_generator(length,use_digits,use_special):
    characters= string.ascii_letters  # upeer or lower case provide krta ha all letters 

    if use_digits:
        characters +=string.digits  #  provides 1_9
    if use_special:
        characters +=string.punctuation  # special charcters (/ @ # $ % ^ & * ? )
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password generator")
length = st.slider("**Select you're Password's length**" , min_value=4,max_value=32,value=12)
use_digits=  st.checkbox("Include Digits")
use_special= st.checkbox("Include special Characters")
if st.button("Generator Password"):
    password = password_generator(length,use_digits,use_special)
    st.write(f"Generated Password: {password}")
 


st.markdown("---")
st.markdown("_Made with ❤️ by Yasmeen Nazeer_")

"""

import streamlit as st
import random
import string

# Custom CSS for better visibility and styling
st.markdown("""
    <style>
    .stApp {
        background-color:rgb(49, 48, 48);  /* Dark background */
        color:rgb(245, 57, 120);            /* White text for contrast */
    }
    .stButton>button {
        background-color:rgb(239, 75, 129); /* Dark pink button */
        color: black !important;   /* Black text */
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        cursor: pointer;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #C2185B; /* Darker pink on hover */
    }
    .stMarkdown h1 {
        color: #E91E63;            /* Dark pink heading */
        text-align: center;
    }
    .stMarkdown p {
        color: white;              /* White text */
    }
    .password-box {
        background-color:rgb(245, 57, 120); /* Dark pink background */
        color: black;              /* Black text */
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to generate password
def password_generator(length, use_digits, use_special):
    characters = string.ascii_letters  # Upper and lower case letters

    if use_digits:
        characters += string.digits  # Digits 0-9
    if use_special:
        characters += string.punctuation  # Special characters
    return ''.join(random.choice(characters) for _ in range(length))

# App Title
st.title("Password Generator")
st.markdown("---")

# User Inputs
length = st.slider("**Select your Password's length**", min_value=4, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Generate Password
if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special)
    # Display the generated password with styling
    st.markdown(f'<div class="password-box">Generated Password: {password}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("_Made with ❤️ by Yasmeen Nazeer_")
