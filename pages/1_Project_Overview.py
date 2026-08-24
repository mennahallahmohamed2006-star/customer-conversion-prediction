import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Project Overview",
    page_icon="📁",
    layout="wide"
)

# ---------------- Header ----------------
st.title("📁 Project Overview")

st.markdown(
    """
    ### 🎯 Goal

    A Machine Learning project that analyzes customer data and predicts whether a
    customer is likely to **convert**.

    The project covers the complete Machine Learning workflow, from data analysis
    and preprocessing to model training, evaluation, and deployment.
    """
)

st.divider()

# ---------------- Model Performance ----------------
st.markdown("### 🏆 Model Performance")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", "89.94%")
c2.metric("Precision", "90.11%")
c3.metric("Recall", "99.43%")
c4.metric("F1-Score", "94.54%")

st.divider()

# ---------------- Project Workflow ----------------
st.markdown("### 🔹 What Was Done")

st.markdown(
    """
    - 🧹 **Data Cleaning**
    - 📊 **Exploratory Data Analysis (EDA)**
    - ⚙️ **Feature Engineering**
    - 🔄 **Data Preprocessing**
    - 🤖 **Machine Learning Model Training**
    - 🔍 **Model Comparison**
    - 🎯 **Hyperparameter Tuning**
    - 📈 **Model Evaluation**
    - 🚀 **Deployment using Streamlit**
    """
)

st.divider()

# ---------------- Project Highlights ----------------
st.markdown("### 💡 Project Highlights")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
        **🎯 Prediction Task**

        Predict whether a customer is likely to convert based on
        marketing and behavioral features.
        """
    )

with col2:
    st.success(
        """
        **🏆 Best Model Performance**

        The final model achieved a **99.43% Recall** and
        **94.54% F1-Score** on the test set.
        """
    )

st.divider()

# ---------------- Navigation ----------------
st.markdown("### 🔗 Explore the Project")

st.page_link(
    "pages/2_Prediction.py",
    label="Go to Prediction Page",
    icon="🔮"
)