import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_leaves_visualizer_body():
    st.header("Cherry Leaf Visualizer")

    st.info(
        f"**Business Requirement 1**\n"
        f"* The client is interested in conducting a study that visually "
        f"differentiates a **powdery mildew** infected leaf from a **healthy** leaf."
    )
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_var_healty = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_var_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        st.success(
            f" We notice that the signs of the causal pathogen are fairly distinctive. \n\n"
            f"Infected leaves display white powdery spots, which we can "
            f" intuitively differentiate from healthy leaves. \n\n"
            f"* Average, Variability, and Difference Images confirmed the hypothesis by "
            f"showing color differences within the center of each leaf image. \n\n"
            f"* Yet, there are no clear patterns to identify them by shape considering "
            f" the fact that when the infection is spread, leaves may become distorted, curling upward."
        )
        st.image(avg_var_healty, caption='Healty leaf - Avegare and Variability')
        st.image(avg_var_powdery_mildew,
                 caption='Powdery Mildew infected leaf - Average and Variability')
        st.write("---")

    # Show the difference between average and variability images
    if st.checkbox("Differences between average healthy and average powdery mildew infected leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.success(
            f" We notice that this study shows similar patterns as color differences in "
            f"the center of the leaf image, where we can intuitively differentiate one from another. \n\n "
            f"* Healthy leaf has more **green color saturation**, whereas powdery "
            f"mildew-infected leaf has a **muted green color** with white spots. \n\n"
        )
        st.warning(
            f"There are no clear patterns to identify them by shape.")

        st.image(diff_between_avgs, caption='Difference between average images')

    # Show the image montage
    if st.checkbox("Image Montage"):
        st.info(
            "* To create and refresh the montage, **click** on 'Create Montage' button")
        st.success(
            f"* The image montage helps to visualize the differences between healthy and "
            f"powdery mildew infected leaf. \n\n"
            f"* The infected leaf has white, powdery spots or patches across the surface."
        )
        my_data_dir = 'inputs/cherry_leaves/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label:", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    # create and display image montage
  sns.set_style("dark")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # check if your montage space is greater than subset size
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return


    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()

    st.pyplot(fig=fig)


  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")