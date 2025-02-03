import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():
    # https://en.wikipedia.org/wiki/Powdery_mildew

    st.write("## Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Our client **Cherry-Py** is dealing with powdery mildew on their"
        f" cherry orchards. A fungus called powdery mildew damages a variety"
        f" of plants. Numerous species of ascomycete fungi belonging to the"
        f" Erysiphales order are responsible for powdery mildew infections."
        f" Because the symptoms of the causing pathogen are so different,"
        f" it is one of the simpler plant diseases to recognize. The leaves"
        f" and stems of infected plants have white, powdery patches. When" 
        f" the disease is severe, it can hinder plant growth and flowering.\n\n"
        f"Cherry-Py's current method of detecting whether a particular"
        f" cherry tree has powdery mildew is manual verification, which"
        f" takes a minute per tree. On several farms around the nation,"
        f" the corporation owns thousands of cherry trees. The IT team "
        f" proposed an ML system that uses an image of a leaf tree to"
        f" instantaneously determine if it is healthy or has powdery mildew"
        f" in order to save time in this procedure.\n\n"
    )

    st.write(
        f"**Project Dataset**\n\n"
        f" The dataset consists of a set of photos of cherry leaves that"
        f" were collected from Cherry-Py's farms. The 4208 photos of"
        f" powdery mildew-infected and healthy leaves in the provided"
        f" picture dataset are evenly distributed between mildew-infected"
        f" and healthy cherry leaves."
    )

    st.caption(
        f"* Dataset source: [kaggle.com](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )

    st.success(
        f"**The project has 2 business requirements:**\n"
        f"* 1. Cherry-Py wants to carry out a research to"
        f" visually distinguish between a cherry leaf that"
        f" has powdery mildew and one that is healthy.\n"
        f"* 2. Cherry-Py wants to know if the cherry leaf"
        f" in the picture is healthy or if it has powdery mildew.\n"
    )

    st.warning(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://)")