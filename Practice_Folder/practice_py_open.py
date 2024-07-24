# Practice File for New Folder
# Streamlit Portfolio Development
import streamlit as st

# Homepage
st.title('Welcome to Lannon\'s Streamlit Portfolio')
st.write('Python Developer | Streamlit Enthusiast | Educator')
# st.image('')

# About Me
st.header('About Me')
st.write('I\'m a passionate Python developer with 7 years of experience...')
st.subheader('Skills')
skills = ['Python','Streamlit','Data Analysis','Desktop Application Development','Full Stack Development', 'Machine Learning']
for skill in skills:
    st.write(f'- {skill}')

# Projects Showcase
st.header('My Projects')
projects = {
    'Project 1': 'Description of project 1',
    'Project 2': 'Description of project 2',
    
}

for project, description in projects.items():
    with st.expander(project):
        st.write(description)
        st.button(f'View {project}')

# Interactive Demo
st.header('Interactive Demo')
st.write('Try out this mini-app I built with Streamlit!')

# Tutorial section
st.header('Latest Tutorials')
tutorials = ['How to build a dashboard in Streamlit', 'Data Visualization with Streamlit']
selected_tutorial = st.selectbox('Choose a tutorial', tutorials)
st.write(f'Content for {selected_tutorial}')

# Testimonials
st.header('What Others Say')
testimonials = {
    'John Doe': 'Great teacher, explained complex concepts simply.',
    'Jane Smith': 'Helped our company build an amazing dashboard.'
}

# Contact Information
st.header('Get in Touch')
st.write('Email: khaulannon@gmail.com')
st.write('LinkedIn: https://www.linkedin.com/in/lannon-khau/')
st.write('Github: https://github.com/LannonTheCannon')

# My Resume
st.header('My Resume')
#st.download_button(
    #label = 'Download Resume',
    #data = open()
    #file_name='resume.pdf',
    #mime='application/pdf'
#)



