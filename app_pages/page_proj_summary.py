import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():
    # https://en.wikipedia.org/wiki/Powdery_mildew

    logo = plt.imread('docs/company_logo.png')
    st.image(logo)

    st.write("## Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Our client **Farmy & Foods** is facing a challenge where their"
        f" cherry plantations present powdery mildew. Powdery mildew "
        f"is a fungal disease that affects a wide range of plants."
        f" Powdery mildew diseases are caused by many different species "
        f"of ascomycete fungi in the order Erysiphales. It is one of the"
        f" easier plant diseases to identify, as the signs of"
        f" the causal pathogen are quite distinctive. "
        f"Infected plants display white powdery spots on the leaves and stems."
        f" When severe, the disease may reduce plant growth and flowering.\n\n"
        f"Currently, the detection process for the client is manual"
        f" verification if a given cherry tree contains powdery mildew"
        f" which takes a minute per tree. The company has thousands of"
        f" cherry trees located on multiple farms across the country. "
        f"To save time in this process, the IT team suggested an ML "
        f"system that detects instantly, using a leaf tree image, "
        f"if it is healthy or has powdery mildew.\n\n")

    st.write(
        f"**Project Dataset**\n\n"
        f"> The dataset is a collection of cherry leaf images provided "
        f"by Farmy & Foods, taken from their crops. The available image dataset "
        f"contains 4208 images of healthy and powdery mildew-infected leaves,"
        f" and it is split evenly for healthy cherry"
        f" leaves and mildew-infected leaves."
    )

    st.caption(
        f"* Dataset source: [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )

    st.success(
        f"**The project has 2 business requirements:**\n"
        f"* 1. The client is interested in conducting a study "
        f"to visually differentiate a cherry leaf that is healthy "
        f"from one that contains powdery mildew. \n"
        f"* 2. The client is interested in telling whether a given cherry"
        f" leaf is infected by powdery mildew or not."
        )

    st.warning(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/SerraKD/mildew-detection)")