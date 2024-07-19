import streamlit as st

def main():
    st.title('Learn to Code: From Websites to AI ')

    # Sidebar with expandable sections
    st.sidebar.title('Lesson Sections')

    # Section 1: Introduction to Coding
    with st.sidebar.expander('1. Introduction to Coding in Streamlit'):
        intro_section = st.radio(
                'Choose a subsection:',
                ['1.1 What is coding?',
                 '1.2 Setup',
                 '1.3 Basic Streamlit Elements',
                 '1.4 Simple Interactive App',
                 '1.5 Running the App',
                 '1.6 Hands-on Activity',
                 '1.7 Wrap-up',],
                key='intro'
            )

    # Section 2: Web Development Basics
    with st.sidebar.expander("2. Web Development Basics"):
        web_section = st.radio(
            "Choose a subsection:",
            ["2.1 HTML fundamentals", "2.2 CSS styling", "2.3 JavaScript basics"],
            key="web"
        )

    # Section 4: Introduction to AI and LLMs
    with st.sidebar.expander("4. AI and Language Models"):
        ai_section = st.radio(
            "Choose a subsection:",
            ["4.1 What is AI?", "4.2 Understanding LLMs", "4.3 Creating a simple chatbot"],
            key="ai"
        )

    # Section 5: Projects and Quizzes
    with st.sidebar.expander("5. Projects and Quizzes"):
        project_section = st.radio(
            "Choose a subsection:",
            ["5.1 Website project", "5.2 Chatbot project", "5.3 Final quiz"],
            key="projects"
        )

    
    # Main content area
    if "1." in intro_section:
        display_intro_content(intro_section)
##    elif "2." in web_section:
##        display_web_content(web_section)
##    elif "3." in python_section:
##        display_python_content(python_section)
##    elif "4." in ai_section:
##        display_ai_content(ai_section)
##    elif "5." in project_section:
##        display_project_content(project_section)

def display_intro_content(subsection):
    if subsection == "1.1 What is coding?":
        st.header("What is Coding?")
        st.write("Coding is the process of creating instructions for comuters...")
    elif subsection == "1.2 Setup":
        st.header("Basic Coding Concepts")
        st.write("Let's explore variables, loops, and conditionals...")
    elif subsection == "1.3 Basic Streamlit Elements":
        st.header("Your First Program")
        st.write("Let's write a 'Hello, World!' program...")
    elif subsection == "1.4 Simple Interactive App":
        st.header("Your First Program")
        st.write("Let's write a 'Hello, World!' program...")
    elif subsection == "1.5 Running the App":
        st.header("Your First Program")
        st.write("Let's write a 'Hello, World!' program...")
    elif subsection == "1.6 Hands-on Activity":
        st.header("Your First Program")
        st.write("Let's write a 'Hello, World!' program...")
    elif subsection == "1.7 Wrap-up":
        st.header("Your First Program")
        st.write("Let's write a 'Hello, World!' program...")
        
# Similarly, create functions for other sections:
# def display_web_content(subsection):
# def display_python_content(subsection):
# def display_ai_content(subsection):
# def display_project_content(subsection):

if __name__ == "__main__":
    main()
