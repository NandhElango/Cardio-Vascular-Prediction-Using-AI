import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(
    page_title="Cardio_Vascular_Prediction",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">Cardiovascular</p>
    """,
    height=69,
)


def page_layout():
    st.write("Cardiovascular health refers to the overall health and function of the heart and blood vessels. It's a critical aspect of overall well-being, as the cardiovascular system is responsible for transporting oxygen, nutrients, hormones, and other vital substances throughout the body. Here are some key points about cardiovascular health:")

    st.write("1. **Importance of Cardiovascular Health**: A healthy cardiovascular system is essential for sustaining life. It helps maintain proper blood pressure, regulates circulation, supports organ function, and ensures that tissues receive an adequate oxygen supply.")

    st.write("2. **Risk Factors**: Various factors can contribute to poor cardiovascular health, including unhealthy diet, lack of physical activity, smoking, excessive alcohol consumption, obesity, high cholesterol, high blood pressure, and genetic predisposition. These factors can increase the risk of developing cardiovascular diseases such as heart disease, stroke, and peripheral artery disease.")

    st.write("3. **Exercise and Physical Activity**: Regular exercise is one of the most effective ways to promote cardiovascular health. Aerobic exercises like walking, running, cycling, swimming, and dancing help strengthen the heart muscle, improve circulation, and lower blood pressure. The American Heart Association recommends at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity aerobic activity per week for adults.")

    st.write("4. **Healthy Diet**: A balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats can support cardiovascular health by providing essential nutrients and antioxidants. Limiting intake of processed foods, saturated fats, trans fats, cholesterol, sodium, and added sugars is also important for preventing cardiovascular disease.")

    st.write("5. **Regular Health Check-ups**: Monitoring key indicators of cardiovascular health, such as blood pressure, cholesterol levels, blood sugar levels, and body weight, through regular health check-ups can help detect potential issues early and enable timely intervention.")

    st.write("6. **Stress Management**: Chronic stress can negatively impact cardiovascular health by contributing to high blood pressure, inflammation, and unhealthy lifestyle behaviors. Practicing stress-reduction techniques such as mindfulness meditation, deep breathing exercises, yoga, and spending time in nature can help promote relaxation and improve overall well-being.")

    st.write("7. **Avoidance of Tobacco and Excessive Alcohol**: Smoking and excessive alcohol consumption are significant risk factors for cardiovascular disease. Quitting smoking and limiting alcohol intake can significantly reduce the risk of developing heart disease and other cardiovascular conditions.")

    st.write("8. **Medication and Treatment**: In some cases, medication may be necessary to manage cardiovascular risk factors such as high blood pressure, high cholesterol, or diabetes. It's essential to follow healthcare provider's recommendations regarding medication use and to adhere to treatment plans for optimal cardiovascular health.")

# Render page layout
page_layout()
