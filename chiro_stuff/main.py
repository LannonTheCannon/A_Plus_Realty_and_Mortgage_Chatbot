# main.py
# This script will be the primary Streamlit app file. It will import and call functions from
# other modules.
#
#============================================================================================

import streamlit as st
from src.patient_info import patient_info_page
from src.soap_info import soap_notes_page
from src.treatment_plan_info import treatment_plan_page
from src.progress_tracker_info import progress_tracker_page

import pandas as pd
import altair as alt
from datetime import datetime, timedelta
import random
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(page_title="Body RES Patient Tracker", page_icon="🦴", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: linear-gradient(to right, #f0f0f0, #e6e9f0);
    }
    .main > div {
        padding: 2rem;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        color: white;
        background-color: #3498db;
        border-radius: 5px;
    }
    .stSelectbox>div>div>div {
        background-color: #ecf0f1;
    }
    .stTextInput>div>div>input {
        background-color: #ecf0f1;
    }
    .stDataFrame {
        border: 1px solid #bdc3c7;
    }
</style>
""", unsafe_allow_html=True)


# Dummy data for demonstration
@st.cache_data
def load_patient_data(patient):
    # This is dummy data - replace with actual database query
    date_range = pd.date_range(start='2024-01-01', end='2024-03-04', freq='7D')
    num_points = len(date_range)

    return pd.DataFrame({
        'Date': date_range,
        'Pain Level': [7, 6, 6, 5, 5, 4, 3, 3, 2, 2][:num_points],
        'Neck ROM (degrees)': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75][:num_points],
        'Lower Back ROM (degrees)': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65][:num_points],
        'Oswestry Disability Index': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15][:num_points],
        'Treatment Satisfaction': [3, 4, 4, 5, 5, 6, 7, 8, 9, 9][:num_points]
    })

def main():
    st.sidebar.title("🦴 Body RES")
    pages = [
        "Patient Information",
        "SOAP Notes",
        "Treatment Plan",
        "Progress Tracker",
        'Patient Summary'
    ]
    selection = st.sidebar.radio("Go to", pages)

    if selection == "Patient Information":
        patient_info_page()
    elif selection == "SOAP Notes":
        soap_notes_page()
    elif selection == "Treatment Plan":
        treatment_plan_page()
    elif selection == "Progress Tracker":
        progress_tracker_page()
    elif selection == "Patient Summary":
        patient_summary()

##
##@st.cache_data
##def load_patient_data(patient):
##    # This is dummy data - replace with actual database query
##    date_range = pd.date_range(start='2024-01-01', end='2024-03-04', freq='7D')
##    num_points = len(date_range)
##
##    return pd.DataFrame({
##        'Date': date_range,
##        'Pain Level': [7, 6, 6, 5, 5, 4, 3, 3, 2, 2][:num_points],
##        'Neck ROM (degrees)': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75][:num_points],
##        'Lower Back ROM (degrees)': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65][:num_points],
##        'Oswestry Disability Index': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15][:num_points],
##        'Treatment Satisfaction': [3, 4, 4, 5, 5, 6, 7, 8, 9, 9][:num_points]
##    })


##def progress_tracker():
##    st.title("Patient Progress Tracker")
##
##    # Patient Selection
##    patient_name = st.selectbox("Select Patient", ["John Doe", "Jane Smith",
##                                                   "Alex Johnson"])  # This would be populated from your database
##
##    # Date Range Selection
##    col1, col2 = st.columns(2)
##    with col1:
##        start_date = st.date_input("Start Date")
##    with col2:
##        end_date = st.date_input("End Date")
##
##    try:
##        df = load_patient_data(patient_name)
##        df = df[(df['Date'] >= pd.Timestamp(start_date)) & (df['Date'] <= pd.Timestamp(end_date))]
##
##        if df.empty:
##            st.warning("No data available for the selected date range.")
##            return
##
##        # Overall Progress Summary
##        st.header("Overall Progress Summary")
##        col1, col2, col3 = st.columns(3)
##        with col1:
##            initial_pain = df['Pain Level'].iloc[0]
##            current_pain = df['Pain Level'].iloc[-1]
##            pain_change = initial_pain - current_pain
##            st.metric("Pain Level Change", f"{pain_change}", f"{pain_change}")
##        with col2:
##            initial_odi = df['Oswestry Disability Index'].iloc[0]
##            current_odi = df['Oswestry Disability Index'].iloc[-1]
##            odi_change = initial_odi - current_odi
##            st.metric("ODI Change", f"{odi_change}%", f"{odi_change}%")
##        with col3:
##            initial_satisfaction = df['Treatment Satisfaction'].iloc[0]
##            current_satisfaction = df['Treatment Satisfaction'].iloc[-1]
##            satisfaction_change = current_satisfaction - initial_satisfaction
##            st.metric("Satisfaction Change", f"{satisfaction_change}", f"{satisfaction_change}")
##
##        # Pain Level Over Time
##        st.subheader("Pain Level Over Time")
##        pain_chart = alt.Chart(df).mark_line().encode(
##            x='Date',
##            y='Pain Level',
##            tooltip=['Date', 'Pain Level']
##        ).properties(width=700, height=300)
##        st.altair_chart(pain_chart, use_container_width=True)
##
##        # Range of Motion Progress
##        st.subheader("Range of Motion Progress")
##        rom_chart = make_subplots(specs=[[{"secondary_y": True}]])
##        rom_chart.add_trace(go.Scatter(x=df['Date'], y=df['Neck ROM (degrees)'], name="Neck ROM"), secondary_y=False)
##        rom_chart.add_trace(go.Scatter(x=df['Date'], y=df['Lower Back ROM (degrees)'], name="Lower Back ROM"),
##                            secondary_y=True)
##        rom_chart.update_layout(title_text="Range of Motion Over Time")
##        rom_chart.update_xaxes(title_text="Date")
##        rom_chart.update_yaxes(title_text="Neck ROM (degrees)", secondary_y=False)
##        rom_chart.update_yaxes(title_text="Lower Back ROM (degrees)", secondary_y=True)
##        st.plotly_chart(rom_chart, use_container_width=True)
##
##        # Oswestry Disability Index Progress
##        st.subheader("Oswestry Disability Index Progress")
##        odi_chart = alt.Chart(df).mark_line().encode(
##            x='Date',
##            y='Oswestry Disability Index',
##            tooltip=['Date', 'Oswestry Disability Index']
##        ).properties(width=700, height=300)
##        st.altair_chart(odi_chart, use_container_width=True)
##
##        # Treatment Satisfaction
##        st.subheader("Treatment Satisfaction")
##        satisfaction_chart = alt.Chart(df).mark_line().encode(
##            x='Date',
##            y='Treatment Satisfaction',
##            tooltip=['Date', 'Treatment Satisfaction']
##        ).properties(width=700, height=300)
##        st.altair_chart(satisfaction_chart, use_container_width=True)
##
##        # Body Heat Map
##        st.subheader("Pain Location Heat Map")
##        # This is a placeholder. In a real app, you'd use a proper heat map library or custom visualization
##        st.image("https://via.placeholder.com/400x600.png?text=Body+Heat+Map+Placeholder")
##
##        # Progress Notes
##        st.subheader("Progress Notes")
##        progress_notes = st.text_area("Add progress notes for this visit")
##
##        # Next Steps
##        st.subheader("Next Steps")
##        next_steps = st.text_area("Outline next steps in the treatment plan")
##
##        if st.button("Save Progress Update"):
##            st.success("Progress update saved successfully!")
##
##        # Option to generate a progress report
##        if st.button("Generate Progress Report"):
##            st.success("Progress report generated!")
##            # Here you would typically generate a PDF report
##            st.download_button(
##                label="Download Progress Report",
##                data="This is where the actual progress report document would be generated",
##                file_name="progress_report.pdf",
##                mime="application/pdf"
##            )
##
##    except Exception as e:
##        st.error(f"An error occurred while loading or processing the data: {str(e)}")
##        return


def patient_summary():
    st.title("Patient Summary")

    # Simulating patient selection from a database
    patient_name = st.selectbox("Select Patient", ["John Doe", "Jane Smith", "Alex Johnson"])

    # Dummy data for demonstration
    patient_info = {
        "John Doe": {
            "Age": 45,
            "Gender": "Male",
            "Initial Consultation": "2024-01-15",
            "Chief Complaint": "Lower back pain",
            "Total Visits": 12,
            "Last Visit": "2024-07-20"
        },
        "Jane Smith": {
            "Age": 32,
            "Gender": "Female",
            "Initial Consultation": "2024-02-03",
            "Chief Complaint": "Neck stiffness",
            "Total Visits": 8,
            "Last Visit": "2024-07-18"
        },
        "Alex Johnson": {
            "Age": 28,
            "Gender": "Non-binary",
            "Initial Consultation": "2024-03-10",
            "Chief Complaint": "Shoulder pain",
            "Total Visits": 6,
            "Last Visit": "2024-07-22"
        }
    }

    # Display patient information
    if patient_name in patient_info:
        st.header(f"Summary for {patient_name}")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Patient Information")
            for key, value in patient_info[patient_name].items():
                st.write(f"**{key}:** {value}")

        with col2:
            st.subheader("Treatment Progress")
            # Dummy progress data
            progress_data = pd.DataFrame({
                'Metric': ['Pain Level', 'ROM Improvement', 'Patient Satisfaction'],
                'Initial': [8, 0, 5],
                'Current': [3, 40, 9]
            })
            st.dataframe(progress_data)

        # Treatment history chart
        st.subheader("Treatment History")
        start_date = datetime.strptime(patient_info[patient_name]["Initial Consultation"], "%Y-%m-%d")
        end_date = datetime.strptime(patient_info[patient_name]["Last Visit"], "%Y-%m-%d")
        date_range = pd.date_range(start=start_date, end=end_date, freq='W')
        num_weeks = len(date_range)

        # Generate dummy pain levels that match the number of weeks
        pain_levels = [8] + [max(1, int(8 - i * 0.5)) for i in range(1, num_weeks)]
        pain_levels = pain_levels[:num_weeks]  # Ensure it matches the length of date_range

        history_data = pd.DataFrame({
            'Date': date_range,
            'Pain Level': pain_levels
        })

        chart = alt.Chart(history_data).mark_line().encode(
            x='Date',
            y='Pain Level',
            tooltip=['Date', 'Pain Level']
        ).properties(width=700, height=300)
        st.altair_chart(chart, use_container_width=True)

        # Recent SOAP notes
        st.subheader("Recent SOAP Notes")
        soap_notes = [
            {"Date": "2024-07-22", "S": "Patient reports reduced pain", "O": "Improved ROM in lower back",
             "A": "Progressing well", "P": "Continue with current treatment plan"},
            {"Date": "2024-07-15", "S": "Slight increase in pain after gardening", "O": "Mild tenderness in lower back",
             "A": "Minor setback due to overexertion", "P": "Advise on proper body mechanics for gardening"}
        ]
        for note in soap_notes:
            with st.expander(f"SOAP Note - {note['Date']}"):
                st.write(f"**Subjective:** {note['S']}")
                st.write(f"**Objective:** {note['O']}")
                st.write(f"**Assessment:** {note['A']}")
                st.write(f"**Plan:** {note['P']}")

        # Upcoming appointments
        st.subheader("Upcoming Appointments")
        upcoming_appointments = [
            {"Date": "2024-07-29", "Time": "10:00 AM", "Type": "Follow-up"},
            {"Date": "2024-08-12", "Time": "2:30 PM", "Type": "Re-evaluation"}
        ]
        for appt in upcoming_appointments:
            st.write(f"**{appt['Date']} at {appt['Time']}** - {appt['Type']}")

        # Treatment recommendations
        st.subheader("Current Treatment Recommendations")
        st.write("1. Continue with spinal adjustments twice a week")
        st.write("2. Perform prescribed exercises daily")
        st.write("3. Use heat therapy before bed")
        st.write("4. Maintain proper posture during work hours")

        # Generate report button
        if st.button("Generate Comprehensive Patient Report"):
            st.success("Comprehensive patient report generated!")
            st.download_button(
                label="Download Patient Report",
                data="This is where the actual patient report document would be generated",
                file_name=f"{patient_name}_report.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("Please select a patient to view their summary.")

if __name__ == "__main__":
    main()
