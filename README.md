# **Mildew Detection in Cherry Leaves**

Using machine learning technology, the Mildew Detection app was developed for the fictional Farmy & Foods and lets users submit pictures of cherry leaves for examination. It can determine whether a cherry leaf is powdery mildew-infected or healthy, and it offers a report that can be downloaded that summarizes the results.

**Deployed version [Mildew Detection in Cherry Leaves](https://milestone-project-mildew-detection-in-cl6x.onrender.com)**

![Responsive image](/files/readme/Responsive.png)

## Dataset Content

- We got the dataset from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). Next, we came up with a fake user story that demonstrated how predictive analytics could be used in an actual project at work.

- There are about 4,000 photos in the dataset that were shot from the client's crop fields. A fungal disease that plagues many plant species, powdery mildew, is visible on both healthy and diseased cherry leaves in the pictures. One of the best goods in their portfolio is the cherry plantation crop, so the corporation is worried about offering the market a product of inferior quality.

## Business Requirements

Farmy & Foods' cherry plantations have been exhibiting powdery mildew, which is hindering their crop. Checking for powdery mildew on a particular cherry tree is now done by hand. An employee spends around half an hour in each tree, collecting a few leaf samples and visually confirming if the tree is healthy or has powdery mildew. Should powdery mildew be present, the staff member applies a certain substance to eradicate the mold. The application of this chemical takes one minute. Thousands of cherry trees owned by the corporation are spread over several farms around the nation. The time required for the manual process inspection makes this manual procedure unscalable.

The IT team proposed an ML system that uses an image of a leaf tree to instantaneously determine if it is healthy or has powdery mildew in order to save time in this procedure. There is a comparable manual method for identifying pests in other crops, and if this experiment is effective, it may be possible to expand it to all other crops. The dataset consists of a set of photos of cherry leaves that were collected from Farmy & Foods' farms.

- 1. The client wants to carry out a research to visually distinguish between a cherry leaf that has powdery mildew and one that is healthy.
- 2. The clients wants to know if the cherry leaf in the picture is healthy or if it has powdery mildew.

## Hypotheses and how to validate?

### ***Hypotheses***

- Healthy and powdery mildew-affected cherry leaves can be distinguished from one another using the obvious pattern differences between the two types of photos.

- Cherry leaves affected with powdery mildew differ from healthy leaves in subtle color and form.

- The given image dataset can be used to build a machine learning model that can determine with at least 97% accuracy if a leaf has powdery mildew.

### ***Validation***

- The image montage illustrates the apparent distinction between leaves that are healthy and those that have powdery mildew.

![Image montage healthy leaves](/files/readme/healthy.png)
![Image montage mildew leaves](/files/readme/powdery-mildew.png)

- Average, Difference, and Variability Color variations within the center of each leaf image supported the notion, but there aren't any obvious patterns that would allow one to distinguish them by shape.

![Average Healthy](/outputs/v2/avg_var_healthy.png)
![Average Infected](/outputs/v2/avg_var_powdery_mildew.png)
![Difference](/outputs/v2/avg_diff.png)

- A performance evaluation of the ML pipeline reveals that it can distinguish between a healthy and diseased leaf with 99% accuracy.

![Performance Metrics](/files/readme/ave-diff.png)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### ***Business Requirement 1:***

The client wants to carry out a research to visually distinguish between a cherry leaf that has powdery mildew and one that is healthy.

> **Data Visualization**

- The dashboard will show mean and standard deviation photos of healthy and powdery mildew-infected cherry leaves.

- The difference between an average healthy leaf and an average powdery mildew-infected leaf will be demonstrated.

- An picture montage of healthy and powdery mildew-infected leaves will be shown.

### ***Business Requirement 2:***

The clients wants to know if the cherry leaf in the picture is healthy or if it has powdery mildew.

> **Classification**

- Build a binary classifier ML model to determine if a leaf is healthy or diseased with powdery mildew. 

- Evaluate the Ml model's loss and accuracy.

- Add an option for users to generate and download a prediction report for uploadable photos.

## Cross Industry Standard Process for Data Mining (CRISP-DM)

CRISP-DM was used while developing this project.

![Crisp- DM image](/files/readme/crisp-dm.png)

> Business Requirement 1

Study should include analysis on:

- average images and variability images for each class (healthy or powdery mildew),
- the differences between average healthy and average powdery mildew cherry leaves,
- an image montage for each class

> Business Requirement 2:

- deliver an ML system that is capable of predicting whether a cherry leaf is healthy or contains powdery mildew

***2. Data Understanding***

The [Kaggle dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) is provided by Code Institute over 4k images of healthy and affected cherry leaves.

- Data collection.

- Retrieve data from the Kaggle dataset  and save as raw data.

***3. Data Preparation***

- Clean data, check and remove non image files
- Split data into train validation and test set
- Set Image shape
- Average and variability of images per label
- Load image shapes and labels in an array
- Plot and save mean variability of images per label
- Difference between average healthy and powdery mildew contained leaf
- Image montage
- Image data augmentation

***4. Modelling***

- Create CNN model
- Fit created ML model with train set
- Save model

***5. Evaluation***

- Plot model learning curve for model training loss and accuracy
- Evaluate model on test set
- Load random image to predict
- Convert image to array and prepare for prediction.
- Predict class probabilities and evaluate.

***6. Deployment***

- Deploy the models into production environment.