import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Streamlit Quiz", page_icon="🧠", layout="wide")

# Custom CSS
st.markdown("""
<style>
    body {
        color: #333;
        background-color: #f0f8ff;
    }
    .stApp {
        background-image: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
    }
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        color: #1e3799;
        text-align: center;
        text-shadow: 2px 2px 4px #ffffff;
    }
    .question-font {
        font-size: 24px !important;
        color: #192a56;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #273c75;
        border-radius: 20px;
        font-size: 18px;
        font-weight: bold;
        border: 2px solid #ffffff;
        padding: 10px 25px;
    }
    .stRadio>label {
        color: #192a56;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Quiz questions
questions = [
    {
        "question": "What command do you use to install Streamlit?",
        "options": ["pip install streamlit", "conda install streamlit", "apt-get install streamlit", "npm install streamlit"],
        "correct": "pip install streamlit"
    },
    {
        "question": "Which Streamlit function is used to display a title?",
        "options": ["st.header()", "st.title()", "st.subheader()", "st.text()"],
        "correct": "st.title()"
    },
    {
        "question": "How do you run a Streamlit app?",
        "options": ["python app.py", "streamlit run app.py", "flask run app.py", "django-admin runserver"],
        "correct": "streamlit run app.py"
    },
    {
        "question": "Which function is used to create a button in Streamlit?",
        "options": ["st.button()", "st.create_button()", "st.input_button()", "st.click()"],
        "correct": "st.button()"
    },
    {
        "question": "What does st.write() do?",
        "options": ["Only writes text", "Writes text to a file", "Can display text, data, and other objects", "Creates a text input field"],
        "correct": "Can display text, data, and other objects"
    },
    {
        "question": "Which function creates a slider input?",
        "options": ["st.slide()", "st.input_slider()", "st.slider()", "st.range()"],
        "correct": "st.slider()"
    },
    {
        "question": "How do you add an image to your Streamlit app?",
        "options": ["st.picture()", "st.img()", "st.show_image()", "st.image()"],
        "correct": "st.image()"
    },
    {
        "question": "Which function is used to create a dropdown select box?",
        "options": ["st.dropdown()", "st.select()", "st.choose()", "st.selectbox()"],
        "correct": "st.selectbox()"
    },
    {
        "question": "How do you create a sidebar in Streamlit?",
        "options": ["st.sidebar", "st.create_sidebar()", "st.side_panel()", "st.add_sidebar()"],
        "correct": "st.sidebar"
    },
    {
        "question": "Which function displays a success message?",
        "options": ["st.success()", "st.message_success()", "st.display_success()", "st.show_success()"],
        "correct": "st.success()"
    },
    {
        "question": "How do you get text input from a user in Streamlit?",
        "options": ["st.input()", "st.get_text()", "st.text_input()", "st.user_input()"],
        "correct": "st.text_input()"
    },
    {
        "question": "Which function is used to display code in Streamlit?",
        "options": ["st.display_code()", "st.show_code()", "st.code()", "st.syntax()"],
        "correct": "st.code()"
    },
    {
        "question": "How do you create columns in Streamlit?",
        "options": ["st.columns()", "st.create_columns()", "st.divide()", "st.split()"],
        "correct": "st.columns()"
    },
    {
        "question": "Which function is used to display a warning message?",
        "options": ["st.alert()", "st.caution()", "st.warning()", "st.notify()"],
        "correct": "st.warning()"
    },
    {
        "question": "How do you add a checkbox in Streamlit?",
        "options": ["st.checkbox()", "st.tick()", "st.boolean()", "st.toggle()"],
        "correct": "st.checkbox()"
    }
]

st.markdown('<p class="big-font">Streamlit Quiz 🧠</p>', unsafe_allow_html=True)

# Initialize session state for score
if 'score' not in st.session_state:
    st.session_state.score = 0

# Display questions
for i, question in enumerate(questions):
    st.markdown(f'<p class="question-font">Question {i+1}: {question["question"]}</p>', unsafe_allow_html=True)
    answer = st.radio(f"Choose your answer for question {i+1}:", question["options"], key=f"q{i}")
    
    # Use columns to create space between questions
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button(f"Submit Answer for Question {i+1}", key=f"submit{i}"):
            if answer == question["correct"]:
                st.success("Correct! 🎉")
                st.session_state.score += 1
                st.balloons()
            else:
                st.error("Oops! That's not right. The correct answer is: " + question["correct"])
    
    st.markdown("---")  # Add a separator between questions

# Display final score
st.markdown(f'<p class="big-font">Your Final Score: {st.session_state.score}/15</p>', unsafe_allow_html=True)

# Reset button
if st.button("Reset Quiz"):
    st.session_state.score = 0
    st.experimental_rerun()

# Sidebar content
st.sidebar.markdown('<p class="question-font">Streamlit Fun Facts</p>', unsafe_allow_html=True)
fun_facts = [
    "Streamlit was first released in October 2019!",
    "Streamlit is completely free and open-source!",
    "You can deploy Streamlit apps for free using Streamlit Cloud!",
    "Streamlit was created by machine learning experts!",
    "Streamlit automatically updates your app when you save changes to your code!"
]
st.sidebar.info(random.choice(fun_facts))
