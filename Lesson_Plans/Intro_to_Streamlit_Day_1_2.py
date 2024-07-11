import streamlit as st
import time
import pandas as pd
import plotly.express as px

# Set page config for a wider layout
st.set_page_config(layout="wide", page_title="Intro to Streamlit", page_icon="🚀")

# Custom CSS to improve the visual appeal
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #0e1117;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #ff4b4b;
        border: none;
    }
    .stTextInput>div>div>input {
        color: #0e1117;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🚀 Introduction to Streamlit")
    st.subheader("An interactive lesson for young Python coders")

    # Introduction
    st.header("1. 🌟 Introduction")
    st.write("Streamlit is a magical Python library that turns your code into beautiful web apps!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✨ Show Example App"):
            with st.expander("See the code", expanded=True):
                st.code("""
import streamlit as st

st.title("Hello, Streamlit!")
name = st.text_input("What's your name?")
if name:
    st.balloons()
    st.write(f"Hello, {name}!")
                """)
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)

    # Setup
    st.header("2. 🛠️ Setup")
    st.info("To install Streamlit, run this command in your terminal or command prompt:")
    st.code("pip install streamlit")
    st.success("Then create a new Python file for your project.")

    # Basic Streamlit elements
    st.header("3. 🧱 Basic Streamlit Elements")
    
    tab1, tab2, tab3 = st.tabs(["Text Elements", "Input Elements", "Display Elements"])
    
    with tab1:
        st.subheader("3.1 Text Elements")
        st.write("Streamlit offers various text elements:")
        st.title("This is a title")
        st.header("This is a header")
        st.subheader("This is a subheader")
        st.text("This is plain text")
        st.markdown("**This** is *markdown*")
        
    with tab2:
        st.subheader("3.2 Input Elements")
        name = st.text_input("Enter your name")
        age = st.slider("Select your age", 10, 15)
        if name and age:
            st.success(f"Hello, {name}! You are {age} years old.")
        
    with tab3:
        st.subheader("3.3 Display Elements")
        st.write("You can display images, charts, and more!")
        
        # Sample data for chart
        data = pd.DataFrame({
            'Fruit': ['Apples', 'Bananas', 'Cherries', 'Dates'],
            'Amount': [30, 21, 15, 10]
        })
        fig = px.bar(data, x='Fruit', y='Amount', title='Fruit Inventory')
        st.plotly_chart(fig)

    # Simple interactive app
    st.header("4. 🧮 Simple Interactive App")
    st.write("Let's create a colorful calculator:")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0)
    with col2:
        num2 = st.number_input("Enter second number", value=0)
    
    operation = st.select_slider("Choose operation", options=["+", "-", "*", "/"])
    
    if st.button("Calculate!", key="calc"):
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

    # Running the app
    st.header("5. 🏃‍♂️ Running the App")
    st.write("To run your Streamlit app:")
    st.code("streamlit run your_app_name.py")
    st.info("Make sure you're in the correct directory in your terminal or command prompt.")

    # Hands-on activity
    st.header("6. 🎨 Hands-on Activity")
    st.write("Now it's your turn! Try creating a simple Streamlit app.")
    with st.expander("See the template"):
        st.code("""
import streamlit as st

st.title("My First Streamlit App")

# Add your code here
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# Try adding more elements!
        """)

    # Wrap-up
    st.header("7. 🎉 Wrap-up")
    st.write("Congratulations! You've learned the basics of Streamlit.")
    st.write("Remember, you can create amazing web apps with just a few lines of Python code.")
    st.write("Keep exploring and have fun coding!")

    # Fun final element
    if st.button("Click for a surprise!"):
        st.snow()
        st.write("You're awesome! Happy coding! 🚀👩‍💻👨‍💻")

if __name__ == "__main__":
    main()
