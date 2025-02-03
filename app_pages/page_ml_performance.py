import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    """
    This function displays ml performance page
    """
    st.header("ML Performance Metrics")

    version = 'v1'
    
    st.write("### Average Image size in dataset")

    average_image_size = plt.imread(f"outputs/{version}/avg_img_size.png")
    st.image(average_image_size, caption='Average Image Size - Width average: 256 Height average: 256')
    st.warning(
        f"The average image size in the provided dataset is: \n\n"
        f"* Width average: 256px \n"
        f"* Height average: 256px"
    )
    st.write("---")

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")

    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.success(
        f"* Train - healthy: 1472 images\n"
        f"* Train - powdery_mildew: 1472 images\n"
        f"* Validation - healthy: 210 images\n"
        f"* Validation - powdery_mildew: 210 images\n"
        f"* Test - healthy: 422 images\n"
        f"* Test - powdery_mildew: 422 images\n"
    )
    st.write("---")

    st.write("### Model History")
    st.info(
        f"The model learning curve is used to check the model for "
        f"overfitting and underfitting by plotting loss and accuracy."
    )
    col1, col2 = st.columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))

    st.write(
        f"> **The accuracy of ML model is %99** "
    )
    load_test_evaluation(version)