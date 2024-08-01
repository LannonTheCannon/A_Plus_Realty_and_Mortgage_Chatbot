# progress_tracker.py
# This script will handle all the functions related to progression visualizations for the selected
# patients.
#
# [Notes]
# -Patient Info-
# Age (calculated from DOB)
# BMI (calculated from height and weight)
# Stress Level (Bar chart or guage)
# Exercise frequency (Pie Chart)
# Sleep Hours (Bar Chart or Gauge)
# Pain Intensity (Gauge or Slider Visualization)

# -SOAP Notes-
# Pain level (gauge or slider visualization)
# Pain location (body heat map)
# Range of Motion measurements (radar chart)
# Orthopedic test results (grouped bar chart)
# Treatment provided (pie chart)
# Prognosis (simple text display or color-coded indicator)

# -Treatment Plan-
# Treatment modalities (bar chart)
# Chiropractic techniques (bar chart)
# Treatment areas (body diagram with highlighted areas)
# Exercises (bubble chart or treemap)
# Outcome measures (grouped bar chart)
# Lifestyle changes (radar chart)

# [Integrated Visualizations]
# A timeline showing patient visits, pain levels, and treatments over time (this would
# be more useful once you have multiple SOAP notes for a patient)
# A comparison chart showing the patient's progress in various metrics (pain level, ROM,
# etc.) from there first time to their most recent visit.
# A dashboard summarizing key patient information, recent SOAP notes, and current treatment
# plan.
# a network diagram showing the relationship between symptoms, treatments, and outcomes

#=======================================================================================

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import json
from datetime import datetime

# progress_tracker.py
# This script will handle all the functions related to progression visualizations for the selected
# patients.
#
# [Notes]
# -Patient Info-
# Age (calculated from DOB)
# BMI (calculated from height and weight)
# Stress Level (Bar chart or guage)
# Exercise frequency (Pie Chart)
# Sleep Hours (Bar Chart or Gauge)
# Pain Intensity (Gauge or Slider Visualization)

# -SOAP Notes-
# Pain level (gauge or slider visualization)
# Pain location (body heat map)
# Range of Motion measurements (radar chart)
# Orthopedic test results (grouped bar chart)
# Treatment provided (pie chart)
# Prognosis (simple text display or color-coded indicator)

# -Treatment Plan-
# Treatment modalities (bar chart)
# Chiropractic techniques (bar chart)
# Treatment areas (body diagram with highlighted areas)
# Exercises (bubble chart or treemap)
# Outcome measures (grouped bar chart)
# Lifestyle changes (radar chart)

# [Integrated Visualizations]
# A timeline showing patient visits, pain levels, and treatments over time (this would
# be more useful once you have multiple SOAP notes for a patient)
# A comparison chart showing the patient's progress in various metrics (pain level, ROM,
# etc.) from there first time to their most recent visit.
# A dashboard summarizing key patient information, recent SOAP notes, and current treatment
# plan.
# a network diagram showing the relationship between symptoms, treatments, and outcomes

#=======================================================================================

import streamlit as st
from streamlit_elements import elements, dashboard, mui, nivo
import json
from datetime import datetime

def load_patient_data():
    with open('./data/patient_info_23456.json', 'r') as f:
        patient_info = json.load(f)
    with open('./data/soap_notes__240731.json', 'r') as f:
        soap_notes = json.load(f)
    with open('./data/treatment_plan_awdawd_20240717.json', 'r') as f:
        treatment_plan = json.load(f)
    return patient_info, soap_notes, treatment_plan

def progress_tracker_page():
    st.title("Patient Dashboard")
    patient_info, soap_notes, treatment_plan = load_patient_data()

    with elements("dashboard"):
        layout = [
            dashboard.Item("patient_overview", 0, 0, 4, 2),
            dashboard.Item("pain_metrics", 4, 0, 4, 2),
            dashboard.Item("range_of_motion", 0, 2, 4, 3),
            dashboard.Item("treatment_plan", 4, 2, 4, 3),
            dashboard.Item("lifestyle_factors", 0, 5, 4, 2),
            dashboard.Item("soap_notes", 4, 5, 4, 2)
        ]

        with dashboard.Grid(layout):
            with mui.Paper(key="patient_overview", sx={"p": 2}):
                mui.Typography(f"Patient: {patient_info['patient_name']}", variant="h6")
                mui.Typography(f"ID: {patient_info['patient_id']}")
                mui.Typography(f"DOB: {patient_info['dob']}")
                mui.Typography(f"Occupation: {patient_info['occupation']}")

            with mui.Paper(key="pain_metrics", sx={"p": 2}):
                mui.Typography("Pain and Discomfort", variant="h6")
                with mui.Box(sx={"height": 200}):
                    nivo.Radar(
                        data=[{
                            "metric": location,
                            "value": soap_notes['pain_level']
                        } for location in soap_notes['pain_location']],
                        keys=["value"],
                        indexBy="metric",
                        valueFormat=">-.2f",
                        margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                        borderColor={"from": "color"},
                        gridLabelOffset=36,
                        dotSize=10,
                        dotColor={"theme": "background"},
                        dotBorderWidth=2,
                        colors={"scheme": "nivo"},
                        blendMode="multiply",
                        motionConfig="wobbly"
                    )

            with mui.Paper(key="range_of_motion", sx={"p": 2}):
                mui.Typography("Range of Motion", variant="h6")
                with mui.Box(sx={"height": 300}):
                    rom_data = [
                        {"joint": "Cervical Spine", "flexion": soap_notes['cervical_spine_flexion'], "extension": soap_notes['cervical_spine_extension']},
                        {"joint": "Thoracic Spine", "flexion": soap_notes['thoracic_spine_flexion'], "extension": soap_notes['thoracic_spine_extension']},
                        {"joint": "Lumbar Spine", "flexion": soap_notes['lumbar_spine_flexion'], "extension": soap_notes['lumbar_spine_extension']},
                        {"joint": "Shoulders", "flexion": soap_notes['shoulders_flexion'], "extension": soap_notes['shoulders_extension']},
                        {"joint": "Hips", "flexion": soap_notes['hips_flexion'], "extension": soap_notes['hips_extension']}
                    ]
                    nivo.Bar(
                        data=rom_data,
                        keys=["flexion", "extension"],
                        indexBy="joint",
                        groupMode="grouped",
                        margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                        padding={0.3},
                        valueScale={"type": "linear"},
                        indexScale={"type": "band", "round": True},
                        colors={"scheme": "nivo"},
                        axisBottom={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                        axisLeft={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                        labelSkipWidth={12},
                        labelSkipHeight={12},
                        labelTextColor={"from": "color", "modifiers": [["darker", 1.6]]},
                        legends=[
                            {
                                "dataFrom": "keys",
                                "anchor": "bottom-right",
                                "direction": "column",
                                "justify": False,
                                "translateX": 120,
                                "translateY": 0,
                                "itemsSpacing": 2,
                                "itemWidth": 100,
                                "itemHeight": 20,
                                "itemDirection": "left-to-right",
                                "itemOpacity": 0.85,
                                "symbolSize": 20,
                                "effects": [{"on": "hover", "style": {"itemOpacity": 1}}]
                            }
                        ]
                    )

            with mui.Paper(key="treatment_plan", sx={"p": 2}):
                mui.Typography("Treatment Plan", variant="h6")
                mui.Typography(f"Start Date: {treatment_plan['plan_start_date']}")
                mui.Typography(f"Duration: {treatment_plan['plan_duration']}")
                mui.Typography(f"Initial Phase: {treatment_plan['initial_phase']}")
                mui.Typography(f"Maintenance Phase: {treatment_plan['maintenance_phase']}")
                mui.Typography("Treatment Modalities:", variant="subtitle1")
                for modality in treatment_plan['treatment_modalities']:
                    mui.Typography(f"• {modality}")

            with mui.Paper(key="lifestyle_factors", sx={"p": 2}):
                mui.Typography("Lifestyle Factors", variant="h6")
                mui.Typography(f"Sleep: {patient_info['sleep_hours']} hours/night")
                mui.Typography(f"Exercise Frequency: {patient_info['exercise_frequency']}")
                mui.Typography(f"Exercise Types: {', '.join(patient_info['exercise_types'])}")
                mui.Typography(f"Stress Level: {patient_info['stress_level']}/10")

            with mui.Paper(key="soap_notes", sx={"p": 2}):
                mui.Typography("Latest SOAP Note", variant="h6")
                mui.Typography(f"Visit Date: {soap_notes['visit_date']}")
                mui.Typography(f"Chief Complaint: {soap_notes['chief_complaint']}")
                mui.Typography(f"Diagnosis: {soap_notes['diagnosis']}")
                mui.Typography(f"Prognosis: {soap_notes['prognosis']}")
                mui.Typography(f"Follow-up: {soap_notes['follow_up']}")

