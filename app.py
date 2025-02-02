import streamlit as st
from app_pages.multi_page import MultiPage

# Load pages scripts
from app_pages.page_proj_summary import page_summary_body
from app_pages.page_proj_hypothesis import page_project_hypothesis_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_ml_performance import page_ml_performance_metrics


app = MultiPage(app_name="Mildew Detection in Cherry Leaves :cherries:")

# Add app pages using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("Leaf Visualizer", page_leaves_visualizer_body)
app.add_page("Powdery Mildew Detector", page_mildew_detector_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

# Run the app
app.run()