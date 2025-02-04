import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)

def page_mildew_detector_body():
    # mildew detector page

    st.header("Powdery Mildew Detection")
    st.success(
        f"**Business Requirement 2**\n"
        f"* Farmy and Foods wants to know if the cherry leaf in the picture is **healthy** or if it has"
        f" **powdery mildew**.")

    st.write('---')

    st.info(
        f" Download images of both healthy and leaves with powdery mildew for the real-time prediction. \n\n"
        f"* Images can be downloaded from **[kaggle.com](https://www.kaggle.com/codeinstitute/cherry-leaves)**"
    )
    st.write(
        f"> **Upload an image of the leaf sample to get real-time predictions. You can choose multiple options.**"
    )
    images_buffer = st.file_uploader(' ',
                                     accept_multiple_files=True)

    st.write(
        f"> Click the **Make Prediction** button to view prediction results"
    )
    predict_button = st.button("Make Prediction")

    if predict_button:
        make_live_predict(images_buffer)

def make_live_predict(images_buffer):
    # upload images and make live predictions

    if images_buffer is not None:
        # DataFrame to hold results
        df_report = pd.DataFrame([])
        
        # Display a progress bar for multiple predictions
        progress_bar = st.progress(0)
        total_images = len(images_buffer)
        
        for idx, image in enumerate(images_buffer):
            img_pil = Image.open(image)
            st.info(f"Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v2'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)

            # Plot prediction results
            plot_predictions_probabilities(pred_proba, pred_class)

            # Add result to DataFrame
            df_report = pd.concat([df_report, pd.DataFrame([{"Name": image.name, "Result": pred_class}])], ignore_index=True)

            # Update progress bar
            progress_bar.progress((idx + 1) / total_images)

        # Once all predictions are done
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)

            # Make results downloadable as CSV
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)