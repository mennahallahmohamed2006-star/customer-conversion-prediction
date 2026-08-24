import streamlit as st
import base64
import os

st.set_page_config(page_title="About Me | Menna", page_icon="👤", layout="wide")

# دالة لقراءة الصورة بجودتها الأصلية بدون أي ضغط
def load_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

st.title("👤 About Me")

col1, col2 = st.columns([1, 3])

with col1:
    # الصورة الشخصية بدون إطار ذهبي (فقط حواف دائرية أنيقة)
    personal_img_path = os.path.join("assets", "ChatGPT Image Aug 24, 2026, 04_24_33 PM.png")
    
    try:
        img_base64 = load_image_base64(personal_img_path)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
                <img src="data:image/png;base64,{img_base64}" 
                     style="width: 180px; height: auto; border-radius: 12px; object-fit: contain;">
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        st.error("تأكدي من وجود الصورة الشخصية داخل مجلد assets")

with col2:
    st.markdown("""
    ## Menna Mohamed
    ##### Junior Data Scientist | Machine Learning
    🔗 [GitHub](https://github.com/mennahallahmohamed2006-star)
    &nbsp;|&nbsp;
    🔗 [LinkedIn](https://www.linkedin.com/in/menna-mohamed-80899b380)
    &nbsp;|&nbsp;
    📧 [Email](mailto:mennahallahmohamed2006@gmail.com)
    """)

st.divider()

st.subheader("🚀 My Projects")

# ---- Project 1: Customer Conversion (this app) ----
c1, c2 = st.columns([1, 2])
with c1:
    # قراءة صورة مشروع الكاستمر المعمولة بالـ Base64 لضمان ظهورها
    img1_path = os.path.join("assets", "Gemini_Generated_Image_6ljpq36ljpq36ljp.jpg")
    if os.path.exists(img1_path):
        img1_base64 = load_image_base64(img1_path)
        st.markdown(f'<img src="data:image/jpeg;base64,{img1_base64}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)
    else:
        st.info("📊 Customer Conversion Banner")

with c2:
    st.markdown("""
    #### Customer Conversion Prediction
    A Machine Learning project that analyzes customer data and predicts whether
    a customer is likely to convert.

    **Test Performance:** Accuracy 89.94% • Precision 90.11% • Recall 99.43% • F1-Score 94.54%

    *(This app!)*
    """)

st.divider()

# ---- Project 2: AquaSafe ----
c1, c2 = st.columns([1, 2])
with c1:
    # قراءة الصورة الثانية للمشروع من الأصول بأمان بدون حوادث
    img2_path = os.path.join("assets", "Gemini_Generated_Image_522yth522yth522y.jpg")
    if os.path.exists(img2_path):
        img2_base64 = load_image_base64(img2_path)
        st.markdown(f'<img src="data:image/jpeg;base64,{img2_base64}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)
    else:
        st.info("💧 AquaSafe Banner")

with c2:
    st.markdown("""
    #### 💧 AquaSafe — Water Quality Analysis & Safety Prediction
    A Machine Learning application that predicts whether a water sample is
    **Safe** or **Unsafe** based on its chemical and biological characteristics.

    **Highlights:**
    - Data Cleaning & Exploratory Data Analysis (EDA)
    - Statistical & Outlier Analysis
    - Feature Engineering & Preprocessing
    - Comparison of multiple ML models + Hyperparameter Tuning
    - Deployment using Streamlit

    **Final Model:** Tuned Decision Tree Classifier
    **Test Performance:** Accuracy 96.06% • Precision 81.82% • Recall 84.07% • F1-Score 82.93%

    🔗 [GitHub Repo](https://lnkd.in/ev-8Wp6c) &nbsp;|&nbsp; 🚀 [Live Demo](https://lnkd.in/ekV-cBh7)
    """)

st.divider()
st.markdown("<p style='text-align:center; color:gray;'>Thanks for visiting! Feel free to connect with me 🙌</p>", unsafe_allow_html=True)