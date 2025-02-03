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
        f"* 1. Cherry-Py wants to carry out a research to"
        f" visually distinguish between a cherry leaf that"
        f" has **powdery mildew** and one that is **healthy**.\n"
    )
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_var_healty = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_var_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        st.success(
            f" It is evident that the symptoms of the causing infection are quite different. \n\n"
            f"We can tell the difference between healthy and infected leaves  "
            f" by their white, powdery patches. \n\n"
            f"* Difference, Variability, and Average Images that displayed color variations "
            f"within each leaf image's center supported the theory. \n\n"
            f"* As the illness spreads, leaves may become deformed and curl upward, "
            f" but there are no obvious patterns to distinguish them by shape."
        )
        st.image(avg_var_healty, caption='Healty leaf - Average and Variability')
        st.image(avg_var_powdery_mildew,
                 caption='Powdery Mildew infected leaf - Average and Variability')
        st.write("---")

    # Show the difference between average and variability images
    if st.checkbox("Differences between average healthy and average powdery mildew infected leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.success(
            f" Similar patterns to color differences in the leaf image's center are observed in "
            f"this study, which allows us to distinguish between them intuitively. \n\n "
            f"* The **green color saturation** of a healthy leaf is higher than that of a leaf infected "
            f"with powdery mildew, which has white patches and a weaker green hue. \n\n"
        )
        st.warning(
            f"No distinct patterns exist to distinguish them by shape.")

        st.image(diff_between_avgs, caption='Difference between average images')

    # Show the image montage
    if st.checkbox("Image Montage"):
        st.info(
            "* Click the 'Create Montage' button to create and refresh the montage.")
        st.success(
            f"* The montage of images makes it easier to see how a leaf infected with powdery "
            f"mildew differs from one that is healthy. \n\n"
            f"* The surface of the infected leaf is covered in white, powdery patches or dots."
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