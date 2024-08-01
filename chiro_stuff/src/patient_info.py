# patient_info.py
# This script will handle all functions related to patient information input and storage
#
#=======================================================================================

import streamlit as st
from utils.data_handler import save_patient_info

def patient_info_page():
    st.title("Patient Information")

    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name")
        patient_id = st.text_input("Patient ID")
        dob = st.date_input("Date of Birth")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact_number = st.text_input("Contact Number")
        email = st.text_input("Email Address")

    with col2:
        visit_date = st.date_input("Visit Date")
        visit_time = st.time_input("Visit Time")
        occupation = st.text_input("Occupation")
        height_ft = st.number_input('Height (feet)', min_value=0.0, step=1.0)
        height_in = st.number_input('Height (inches)', min_value=0.0, step=1.0)
        weight_lbs = st.number_input("Weight (lbs)", min_value=0.0, step=1.0)

    st.subheader("Emergency Contact")
    emergency_name = st.text_input("Emergency Contact Name")
    emergency_relation = st.text_input("Relationship to Patient")
    emergency_number = st.text_input("Emergency Contact Number")

    st.subheader("Medical History")
    medical_history = st.text_area("Any relevant medical history or conditions")
    current_medications = st.text_area("Current Medications")
    allergies = st.text_area("Known Allergies")

    st.subheader("Lifestyle Factors")
    exercise_frequency = st.selectbox("Exercise Frequency",
                                      ["None", "1-2 times/week", "3-4 times/week", "5+ times/week"])
    exercise_types = st.multiselect("Types of Exercise",
                                    ["Walking", "Running", "Swimming", "Weightlifting", "Yoga", "Other"])
    sleep_hours = st.slider("Average Hours of Sleep per Night", 0, 12, 7)
    stress_level = st.slider("Stress Level (0-10)", 0, 10, 5)

    st.subheader("Previous Chiropractic Care")
    previous_chiro = st.radio("Have you received chiropractic care before?", ["Yes", "No"])
    if previous_chiro == "Yes":
        previous_chiro_details = st.text_area("Please provide details of previous chiropractic care")

    st.subheader("Current Complaint")
    primary_complaint = st.text_area("Primary reason for visit")
    pain_onset = st.date_input("When did the pain/discomfort start?")
    pain_cause = st.text_input("What caused the pain/discomfort? (if known)")

    st.subheader("Pain Characteristics")
    pain_frequency = st.selectbox("Pain Frequency", ["Constant", "Intermittent", "Occasional"])
    pain_intensity = st.slider("Pain Intensity (0-10)", 0, 10, 5)
    pain_quality = st.multiselect("Pain Quality", ["Sharp", "Dull", "Aching", "Burning", "Tingling", "Numbness"])

    st.subheader("Consent and Agreements")
    consent = st.checkbox("I consent to chiropractic examination and treatment")
    privacy_agreement = st.checkbox("I have read and agree to the privacy policy")

    if st.button("Save Patient Information"):
        if consent and privacy_agreement:
            save_patient_info(patient_name, patient_id, dob, gender, # First Time Patient Inforation 
                              contact_number, email, visit_date, visit_time,
                              occupation, height_ft, height_in, weight_lbs,
                              emergency_name, emergency_relation, emergency_number, # Emergency contact information
                              medical_history, current_medications, allergies, # Medical History
                              exercise_frequency, exercise_types, sleep_hours, stress_level, # Lifestyle Factors
                              previous_chiro, # Previous Chiropractic Care
                              primary_complaint, pain_onset, pain_cause, # Current Complaint
                              pain_frequency, pain_intensity, pain_quality, # Pain Characteristics
                              consent, privacy_agreement) # Consent and Agreements
            st.success("Patient information saved successfully!")
            
        else:
            st.error("Please provide consent and agree to the privacy policy before saving.") 
