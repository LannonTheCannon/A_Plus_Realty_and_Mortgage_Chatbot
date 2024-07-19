import streamlit as st
import pandas as pd
import altair as alt
import time

# Set page config
st.set_page_config(
    page_title="Streamlit Masterclass",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: linear-gradient(to right, #4e54c8, #8f94fb);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #4e54c8, #8f94fb);
    }
    .Widget>label {
        color: white;
        font-family: monospace;
    }
    .stTextInput>div>div>input {
        color: #4e54c8;
    }
    .stButton>button {
        color: #4e54c8;
        background-color: white;
        border-radius: 20px;
    }
    .stProgress .st-bo {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.DataFrame({
        'Element': ['Text', 'Button', 'Slider', 'Input', 'Chart'],
        'Usage': [90, 75, 60, 85, 70]
    })

def main():
    st.sidebar.title("🚀 Streamlit Masterclass")
    sections = [
        ':coffee: Home',
        "🛠 Setup",
        "🧱 Basic Elements",
        "🔢 Interactive App",
        "▶  Running the App",
        "🖐 Hands-on Activity",
        "🎓 Wrap-up",
        "🎨 CSS Wrapping"
    ]
    selected_section = st.sidebar.radio("Navigation", sections)

    if selected_section == ':coffee: Home':
        home()
    elif selected_section == "🛠 Setup":
        setup()
    elif selected_section == "🧱 Basic Elements":
        basic_elements()
    elif selected_section == "🔢 Interactive App":
        interactive_app()
    elif selected_section == "▶️ Running the App":
        running_app()
    elif selected_section == "🖐️ Hands-on Activity":
        hands_on_activity()
    elif selected_section == "🎓 Wrap-up":
        wrap_up()
    elif selected_section == "🎨 CSS Wrapping":  # New condition
        css_wrapping()

def home():
    st.title("Welcome to Streamlit Masterclass! 🎉")
    st.subheader("Empowering 6th-9th grade Python coders")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Streamlit is an amazing Python library that lets you create stunning web apps with ease. 
        In this masterclass, you'll learn:
        - 🔧 How to set up Streamlit
        - 🧱 Basic Streamlit elements
        - 🔢 Building interactive apps
        - 🚀 Running your Streamlit creations
        """)
        
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    
    st.info("Ready to begin your Streamlit journey? Navigate through the lessons using the sidebar! 👈")

def setup():
    st.title("🛠️ Setting Up Streamlit")
    st.write("Let's get your development environment ready!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Step 1: Install Streamlit")
        st.code("pip install streamlit")
        
    with col2:
        st.subheader("Step 2: Verify Installation")
        st.code("streamlit hello")
        
    st.subheader("Step 3: Create Your First App")
    st.code("""
    # Save this as 'hello_streamlit.py'
    import streamlit as st
    st.title("Hello, Streamlit!")
    st.write("Welcome to your first Streamlit app!")
    """)
    
    st.success("You're all set! Let's dive into the exciting world of Streamlit! 🎈")

def basic_elements():
    st.title("🧱 Basic Streamlit Elements")
    st.write("Explore the building blocks of Streamlit apps!")
    
    tab1, tab2, tab3 = st.tabs(["Text Elements", "Input Elements", "Display Elements"])
    
    with tab1:
        st.subheader("Text Elements")
        st.title("This is a title")
        st.header("This is a header")
        st.subheader("This is a subheader")
        st.text("This is plain text")
        st.markdown("This is **bold** and *italic* text")
        st.latex(r"e^{i\pi} + 1 = 0")
        
    with tab2:
        st.subheader("Input Elements")
        name = st.text_input("What's your name?")
        age = st.slider("How old are you?", 10, 15)
        st.write(f"Hello, {name}! You are {age} years old.")
        
    with tab3:
        st.subheader("Display Elements")
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
        
        data = load_data()
        chart = alt.Chart(data).mark_bar().encode(
            x='Element',
            y='Usage',
            color=alt.value("#4e54c8")
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)

def interactive_app():
    st.title("🔢 Interactive Streamlit App")
    st.write("Let's build a fun calculator!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, step=0.1)
        num2 = st.number_input("Enter second number", value=0.0, step=0.1)
        operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])
        
    with col2:
        st.write("Result:")
        if st.button("Calculate", key="calc"):
            with st.spinner("Calculating..."):
                time.sleep(1)  # Simulating calculation time
                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                else:
                    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
                st.success(f"Result: {result}")
                st.balloons()

def running_app():
    st.title("▶️ Running Your Streamlit App")
    st.write("Time to see your creation come to life!")
    
    st.code("streamlit run your_app_name.py")
    
    st.info("Make sure you're in the correct directory in your terminal or command prompt.")
    
    with st.expander("Pro Tips"):
        st.markdown("""
        - Use `streamlit run --server.port 8080 your_app.py` to specify a port
        - Enable auto-reloading with `streamlit run --server.runOnSave true your_app.py`
        - For more options, try `streamlit run --help`
        """)

def hands_on_activity():
    st.title("🖐️ Hands-on Activity")
    st.write("Now it's your turn to create something awesome!")
    
    st.code("""
import streamlit as st
import random

st.title("Guess the Number Game")

 # Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Get the player's guess
guess = st.number_input("Guess a number between 1 and 100", min_value=1, max_value=100)

if st.button("Check my guess"):
    if guess == secret_number:
        st.success("Congratulations! You guessed it right!")
        st.balloons()
    elif guess < secret_number:
        st.warning("Try a higher number!")
    else:
        st.warning("Try a lower number!")
    """)
    
    st.success("Challenge: Can you add a feature to count the number of guesses?")

def wrap_up():
    st.title("🎓 Wrap-up")
    st.write("Congratulations on completing the Streamlit Masterclass!")
    
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    
    st.success("You've learned the basics of Streamlit and are now ready to create amazing web apps!")
    st.balloons()
    
    st.markdown("""
    Remember:
    - Streamlit turns data scripts into shareable web apps in minutes
    - All it takes is a few lines of Python code
    - The possibilities are endless!
    
    Keep exploring, keep coding, and most importantly, have fun! 🚀
    """)


def css_wrapping():
    st.title("🎨 Customizing Your Streamlit App with CSS Wrapping")
    st.write("Learn how to use CSS to make your Streamlit app look amazing!")

    st.header("1. Introduction")
    st.write("CSS is like the paint and decorations for your web page.")
    st.info("We'll see how CSS can transform the look of your Streamlit app.")

    st.header("2. Basic CSS in Streamlit")
    st.code("""
st.markdown('''
<style>
/* CSS goes here */
</style>
''', unsafe_allow_html=True)
    """)
    st.write("We use `unsafe_allow_html=True` to tell Streamlit it's okay to use our custom HTML and CSS.")

    st.header("3. Changing Text Color and Size")
    st.code("""
st.markdown('''
<style>
.big-red-text {
    color: red;
    font-size: 24px;
}
</style>
''', unsafe_allow_html=True)

st.markdown('<p class="big-red-text">This is big red text!</p>', unsafe_allow_html=True)
    """)
    st.markdown('<p style="color: red; font-size: 24px;">This is big red text!</p>', unsafe_allow_html=True)

    st.header("4. Styling Buttons")
    st.code("""
st.markdown('''
<style>
.stButton>button {
    color: white;
    background-color: purple;
    border-radius: 10px;
}
</style>
''', unsafe_allow_html=True)

st.button("Click me!")
    """)
    st.markdown('''
    <style>
    .stButton>button {
        color: white;
        background-color: purple;
        border-radius: 10px;
    }
    </style>
    ''', unsafe_allow_html=True)
    st.button("Click me!")

    st.header("5. Changing Background Color")
    st.code("""
st.markdown('''
<style>
.stApp {
    background-color: lightblue;
}
</style>
''', unsafe_allow_html=True)
    """)
    st.write("Note: This will change the background of the entire app.")

    st.header("6. Mini-Project: Theme Your App")
    st.write("Try creating a simple theme for your app using what you've learned.")
    st.write("Customize at least:")
    st.write("1. A title")
    st.write("2. A button")
    st.write("3. The background color")

    st.header("7. Wrap-up")
    st.write("Remember:")
    st.write("• CSS is about experimenting and having fun with design.")
    st.write("• Always consider readability when choosing colors.")
    st.write("• Keep practicing to create even more amazing Streamlit apps!")

if __name__ == "__main__":
    main()
