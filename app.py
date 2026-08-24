import streamlit as st

st.set_page_config(
    page_title="Customer Conversion | Menna Mohamed",
    page_icon="📊",
    layout="wide"
)

# ---------------- Hero Banner ----------------
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-top: 10px;">
        <img 
            src="assets/Gemini_Generated_Image_6ljpq36ljpq36ljp.jpg"
            style="
                width: 700px;
                max-width: 90%;
                border-radius: 15px;
            "
        >
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='text-align: center; margin-top: 20px;'>
    Customer Conversion Prediction 📊
    </h1>

    <p style='text-align: center; font-size: 18px; color: gray;'>
    Machine Learning App to predict whether a customer is likely to convert
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- Intro ----------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
        ### 👋 Welcome

        This app uses a trained Machine Learning pipeline to analyze customer data
        and predict whether a customer will **convert** or **not convert**, based on
        marketing and behavioral features.

        Use the sidebar to navigate:

        - **📁 Project Overview** — Learn about the data, methodology, and results
        - **🔮 Prediction** — Enter customer data and get a live prediction
        - **👤 About Me** — Who built this and how to reach me
        """
    )

with col2:
    st.image(
        "assets/Gemini_Generated_Image_522yth522yth522y.jpg",
        use_container_width=True
    )

st.divider()

# ---------------- Model Performance Highlight ----------------
st.markdown("### 🏆 Model Performance")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Accuracy", "89.94%")
m2.metric("Precision", "90.11%")
m3.metric("Recall", "99.43%")
m4.metric("F1-Score", "94.54%")

st.info(
    "👉 Head to the **Prediction** page from the sidebar to try the model yourself!"
)