import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file
import time
import random


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'powdery_mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    ## plot image on streamlit dashboard
    unique_key = f"plot_{int(time.time())}_{random.randint(1000, 9999)}"
    st.plotly_chart(fig, key=unique_key)


def resize_input_image(img, version):
    """
    reshape input images to avg. image size
    """
    
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    # use resampling LANCZOS filter
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255
    
    return my_image



def load_model_and_predict(my_image, version):
    """
    load & perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/mildew_detection_model.h5")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'healthy': 0, 'powdery_mildew': 1}.items()}

    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.info(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}**")

    return pred_proba, pred_class