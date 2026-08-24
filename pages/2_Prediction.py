import streamlit as st
import joblib
import pandas as pd


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Customer Conversion Prediction",
    page_icon="🔮",
    layout="wide"
)


# ============================================================
# Load Model
# ============================================================

model = joblib.load("model/final_adaboost_pipeline.pkl")


# ============================================================
# Header
# ============================================================

st.title("🔮 Customer Conversion Prediction")

st.write(
    "Enter the customer information below to predict "
    "whether the customer is likely to convert."
)

st.divider()


# ============================================================
# Customer Information
# ============================================================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

with col2:
    income = st.number_input(
        "Income",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

with col3:
    ad_spend = st.number_input(
        "Ad Spend",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )


# ============================================================
# Marketing & Website Behavior
# ============================================================

st.subheader("📈 Marketing & Website Behavior")

col1, col2, col3 = st.columns(3)

with col1:
    click_through_rate = st.number_input(
        "Click Through Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.10,
        step=0.01
    )

with col2:
    conversion_rate = st.number_input(
        "Conversion Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
        step=0.01
    )

with col3:
    website_visits = st.number_input(
        "Website Visits",
        min_value=0,
        value=10,
        step=1
    )

col1, col2, col3 = st.columns(3)

with col1:
    pages_per_visit = st.number_input(
        "Pages Per Visit",
        min_value=0.0,
        value=3.0,
        step=0.5
    )

with col2:
    time_on_site = st.number_input(
        "Time On Site",
        min_value=0.0,
        value=5.0,
        step=0.5
    )

with col3:
    social_shares = st.number_input(
        "Social Shares",
        min_value=0,
        value=5,
        step=1
    )


# ============================================================
# Email & Purchase Behavior
# ============================================================

st.subheader("📧 Email & Purchase Behavior")

col1, col2, col3 = st.columns(3)

with col1:
    email_opens = st.number_input(
        "Email Opens",
        min_value=0,
        value=5,
        step=1
    )

with col2:
    email_clicks = st.number_input(
        "Email Clicks",
        min_value=0,
        value=2,
        step=1
    )

with col3:
    previous_purchases = st.number_input(
        "Previous Purchases",
        min_value=0,
        value=2,
        step=1
    )

col1, col2, col3 = st.columns(3)

with col1:
    loyalty_points = st.number_input(
        "Loyalty Points",
        min_value=0,
        value=100,
        step=10
    )

with col2:
    email_engagement = st.number_input(
        "Email Engagement",
        min_value=0.0,
        value=0.50,
        step=0.01
    )

with col3:
    purchase_history_flag = st.selectbox(
        "Purchase History Flag",
        options=[0, 1]
    )


# ============================================================
# Campaign Information
# ============================================================

st.subheader("🎯 Campaign Information")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col2:
    campaign_channel = st.selectbox(
        "Campaign Channel",
        [
            "Referral",
            "PPC",
            "Email",
            "SEO",
            "Social Media"
        ]
    )

with col3:
    campaign_type = st.selectbox(
        "Campaign Type",
        [
            "Conversion",
            "Awareness",
            "Consideration",
            "Retention"
        ]
    )


# ============================================================
# Prediction
# ============================================================

st.divider()

if st.button("🔮 Predict Conversion", use_container_width=True):

    input_data = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "AdSpend": [ad_spend],
        "ClickThroughRate": [click_through_rate],
        "ConversionRate": [conversion_rate],
        "WebsiteVisits": [website_visits],
        "PagesPerVisit": [pages_per_visit],
        "TimeOnSite": [time_on_site],
        "SocialShares": [social_shares],
        "EmailOpens": [email_opens],
        "EmailClicks": [email_clicks],
        "PreviousPurchases": [previous_purchases],
        "LoyaltyPoints": [loyalty_points],
        "EmailEngagement": [email_engagement],
        "PurchaseHistoryFlag": [purchase_history_flag],
        "Gender": [gender],
        "CampaignChannel": [campaign_channel],
        "CampaignType": [campaign_type]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probabilities = model.predict_proba(input_data)[0]

    conversion_probability = probabilities[1] * 100
    non_conversion_probability = probabilities[0] * 100


    # ========================================================
    # Results
    # ========================================================

    st.subheader("📊 Prediction Result")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.metric(
            "Conversion Probability",
            f"{conversion_probability:.2f}%"
        )

    with result_col2:
        st.metric(
            "Not Conversion Probability",
            f"{non_conversion_probability:.2f}%"
        )

    st.progress(
        int(round(conversion_probability))
    )

    if prediction == 1:

        st.success(
            "🎉 The customer is likely to **CONVERT**!"
        )

    else:

        st.warning(
            "❌ The customer is likely to **NOT CONVERT**."
        )