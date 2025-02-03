import streamlit as st


def page_project_hypothesis_body():
    # https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/#:~:text=Powdery%20mildew%20of%20sweet%20and,1).

    st.write("## Project Hypothesis and Validation")

    st.info(
        f"Podosphaera clandestina is an obligatory biotrophic fungus that"
        f" causes powdery mildew on sweet and sour cherries. Cultivars of"
        f" sweet cherries (Prunus avium) that are in the middle or late "
        f"stages of the growing season are frequently impacted, making them "
        f"unsellable because of the white fungal growth that covers their surface. \n\n"
        f"Early signs are light, approximately round, powdery-looking patches "
        f"on young, sensitive leaves (newly unfurled, light green spreading leaves),"
        f" which typically appear 7 to 10 days after the first irrigation. "
        f"In addition to being inherently more resistant to infection than "
        f"younger leaves, older leaves acquire an age-related (ontogenic) "
        f"resistance to powdery mildew. Keep an eye out for early leaf "
        f"infections on root suckers, the inside of the canopy, or the "
        f"tree's crotch where there is a lot of humidity.\n\n"
        f"Although it is more likely to start on the abaxial (underside) "
        f"of leaves, the illness will eventually spread to both sides. "
        f"Leaves may become twisted and curl upward as the season goes "
        f"on and infection is dispersed by the wind. Leaves may pucker "
        f"and twist as a result of severe diseases. On fresh branches, "
        f"newly formed leaves get smaller and smaller, are frequently "
        f"pale, and might be deformed."
    )
    
    st.write('---')
    
    st.warning(
        f"**Hypotheses**\n\n"
        f"* It is possible to distinguish between healthy and powdery "
        f"mildew-affected cherry leaves by looking for obvious pattern "
        f"changes between photos of healthy and infected leaves. \n\n"
        f"* Cherry leaves affected with powdery mildew differ from "
        f"healthy leaves in subtle color and form. \n\n"
        f"* With a 97% accuracy rate, a machine learning model can "
        f"be created using the given image dataset to determine if a "
        f"leaf is infected with powdery mildew."
    )

    st.success(
        f"**Validation**\n\n"
        f"* The apparent distinction between leaves with powdery mildew "
        f"and those that are healthy is depicted in the Image Montage. \n\n"
        f"* Difference, Average, and Variability Although there are no "
        f"obvious patterns to distinguish them by shape, the images "
        f"supported the idea by displaying color variations within "
        f"the center of each leaf image. \n\n"
        f"* An analysis of the ML pipeline's performance reveals that "
        f"it can distinguish between an infected and healthy "
        f"leaf with 99% accuracy."
    )
    
    st.write('---')
    
    st.write(
        f"* 1. Cherry-Py wants to carry out a research to visually "
        f"distinguish between a cherry leaf that has powdery mildew "
        f"and one that is healthy. \n"
        f"* 2. Chery-Py wants to know if the cherry leaf in the "
        f"picture is healthy or if it has powdery mildew."
    )
    
    st.write (
        f"> **Cherry-Py bussines requirements are fullfilled.**"
    )

    st.write('---')