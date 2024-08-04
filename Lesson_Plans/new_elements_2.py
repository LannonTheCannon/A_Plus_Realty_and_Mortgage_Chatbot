import streamlit as st
import random
import pandas as pd
import numpy as np
import altair as alt
import time
import plotly.express as px
import base64
import os

# Set page config
st.set_page_config(layout="wide", page_title="Streamlit Scavenger Hunt", page_icon="🔍")

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        color: black;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main h1, .main h2, .main h3, .main p, .main label, .main .stMarkdown {
        color: black !important;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #ff4b4b;
        border: none;
    }
    .stTextInput>div>div>input {
        color: black;
    }
    [data-testid="stSidebar"] {
        margin-top: 45px;
        color: white;
    }
    [data-testid="stMetricDelta"] {
        display: none;
    }
    .stAlert {
        color: black;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'questions_asked' not in st.session_state:
    st.session_state.questions_asked = 0
if 'current_element' not in st.session_state:
    st.session_state.current_element = None

# Define the elements
elements = [
    ("st.latex", "Renders LaTeX expressions", lambda: st.latex(r'''e^{i\pi} + 1 = 0''')),
    ("st.code", "Displays code with syntax highlighting", lambda: st.code("def hello_world():\n    print('Hello, World!')", language="python")),
    ("st.dataframe", "Displays an interactive dataframe", lambda: st.dataframe(pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5))))),
    ("st.table", "Displays a static table", lambda: st.table(pd.DataFrame(np.random.randn(5, 3), columns=['a', 'b', 'c']))),
    ("st.metric", "Displays a metric in a box", lambda: st.metric(label="Temperature", value="70 °F", delta="1.2 °F")),
    ("st.line_chart", "Displays a line chart", lambda: st.line_chart(pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c']))),
    ("st.echo", "Displays code and its output", lambda: st.echo()(print)("Hello, World!")),
    ("st.caption", "Displays smaller, muted text", lambda: st.caption("This is a caption")),
    ("st.json", "Displays JSON-formatted data", lambda: st.json({"foo": "bar", "baz": "boz"})),
    ("st.image", "Displays an image", lambda: st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)),
    ("st.audio", "Displays an audio player", lambda: st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")),
    ("st.video", "Displays a video player", lambda: st.video("https://youtu.be/B2iAodr0fOo")),
    ("st.map", "Displays a map", lambda: st.map(pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']))),
    ("st.color_picker", "Displays a color picker", lambda: st.color_picker("Pick a color", "#00f900")),
    ("st.expander", "Creates an expandable container", lambda: st.expander("Expand me!").write("This is hidden until expanded.")),
    ("st.spinner", "Displays a loading spinner", lambda: st.spinner("Loading...")),
    ("st.progress", "Displays a progress bar", lambda: st.progress(0.75)),
    ("st.error", "Displays an error message", lambda: st.error("This is an error message")),
    ("st.warning", "Displays a warning message", lambda: st.warning("This is a warning message")),
    ("st.info", "Displays an informational message", lambda: st.info("This is an informational message")),
    ("st.success", "Displays a success message", lambda: st.success("This is a success message")),
    ("st.altair_chart (scatter)", "Displays an interactive Altair scatter plot", lambda: st.altair_chart(alt.Chart(pd.DataFrame(np.random.randn(50, 2), columns=['x', 'y'])).mark_circle().encode(x='x', y='y'))),
]

def get_sidebar_style(sidebar_image_base64):
    return f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: url("data:image/png;base64,{sidebar_image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Main game function
def run_game():
    st.title("🔍 Streamlit Scavenger Hunt!")
    st.subheader("Guess the Streamlit Element")

    sidebar_image_path = os.path.join(os.path.dirname(__file__), "images", "boy_and_dog.png")
    sidebar_image_base64 = get_base64_of_bin_file(sidebar_image_path)
    st.markdown(get_sidebar_style(sidebar_image_base64), unsafe_allow_html=True)

    if st.session_state.current_element is None:
        st.session_state.current_element = random.choice(elements)

    st.write("What Streamlit function creates this element?")

    # Display the element
    st.session_state.current_element[2]()

    # Get user's guess
    user_guess = st.text_input("Your guess (e.g., st.button):")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit"):
            check_answer(user_guess)

    with col2:
        if st.button("Skip"):
            st.session_state.current_element = random.choice(elements)
            st.rerun()

    # Display score and progress
    st.sidebar.markdown(f"""<h3 style='color: white;
                        margin-top: 150px;
                        '>Game Progress</h3>""", unsafe_allow_html=True)
                        
    st.sidebar.markdown(f"""<h4 style='color: white;
                        '>Score: {st.session_state.score}</h4>""", unsafe_allow_html=True)
                        
    st.sidebar.markdown(f"""<h4 style='color: white;
                        '>Questions Asked: {st.session_state.questions_asked}</h4>""", unsafe_allow_html=True)
    
    # Display a progress bar
    progress = st.session_state.questions_asked / 20  # Assuming 20 questions per game
    st.sidebar.progress(progress)

    if st.session_state.questions_asked >= 20:
        end_game()

def check_answer(user_guess):
    if user_guess.lower() == st.session_state.current_element[0]:
        st.success("Correct! 🎉")
        st.balloons()
        st.session_state.score += 1
    else:
        st.error(f"Not quite. It was {st.session_state.current_element[0]}")
        st.info(f"Description: {st.session_state.current_element[1]}")

    st.session_state.questions_asked += 1
    st.session_state.current_element = random.choice(elements)
    time.sleep(2)  # Give user time to see the result
    st.rerun()

def end_game():
    st.title("🏆 Game Over!")
    st.write(f"Your final score: {st.session_state.score} out of {st.session_state.questions_asked}")
    
    # Calculate percentage
    percentage = (st.session_state.score / st.session_state.questions_asked) * 100
    st.write(f"You got {percentage:.2f}% correct!")

    # Give a rating based on percentage
    if percentage >= 90:
        st.success("Outstanding! You're a Streamlit expert! 🌟")
    elif percentage >= 70:
        st.success("Great job! You're well on your way to mastering Streamlit! 😊")
    elif percentage >= 50:
        st.info("Good effort! Keep practicing and you'll improve! 👍")
    else:
        st.info("Nice try! Streamlit has a lot to offer. Keep exploring! 💪")

    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.questions_asked = 0
        st.session_state.current_element = None
        st.rerun()

# Run the game
run_game()
