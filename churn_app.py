import pandas as pd
import pickle
import streamlit as st
from PIL import Image


html_temp = """
<div style="background-color:orange;padding:1.5px">
<h1 style="color:white;text-align:center;">Select Employee's Attributes</h1>
</div><br>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

html_temp2 = """
<div style="background-color:green;padding:40px;border-radius: 20px 20px 20px 20px;">
<h1 style="color:white;text-align:center;">Employee Churn Prediction App</h1>
</div><br>"""

html_temp3 = """
<div style="background-color:darkblue;padding:1px; border-radius: 20px 20px 20px 20px;">
<h3 style="color:white;text-align:center;font-family: Comic Sans MS">Whether your employees will continue to work with you or not ? Let's See !</h1>
</div><br>"""


st.markdown(html_temp2,unsafe_allow_html=True)

img = Image.open("image.png")
#img = img.resize((3000, 1500))
st.image(img, width=500, use_column_width =True) 

st.markdown(html_temp3,unsafe_allow_html=True)

st.info("**Please fill the attributes on the left hand side to make \
    run the model properly.**")



satisfaction = st.sidebar.number_input("Satisfaction", 0.090, 1.0)
last_eval = st.sidebar.number_input("Last Evaluation", 0.360, 1.0)
number_project = st.sidebar.slider("Number of  Projects", 2, 7, 1)
average_montly_hours = st.sidebar.slider("Average Monthly Hours", 96, 310, 1)
experience = st.sidebar.slider("Experience", 2, 10, 1)
work_accident = st.sidebar.selectbox("Work Accident", ("Yes", "No"))
promotion = st.sidebar.selectbox("Promotion", ("Yes", "No"))
departments = st.sidebar.selectbox("Department",('sales', 'accounting', 'hr', 'technical', 'support', 'management',
       'IT', 'product_mng', 'marketing', 'RandD'))
salary = st.sidebar.selectbox("Salary",('low', 'medium', 'high'))

if promotion == "Yes":
    promotion = 1
else:
    promotion = 0 

if work_accident == "Yes":
    work_accident = 1
else:
    work_accident = 0     





new_data = {"satisfaction" : satisfaction,
            "last_eval" : last_eval,
            "num_of_projects" : number_project,
            "avg_monthly_hours" : average_montly_hours,
            "work_accident" : work_accident,
            "experience" : experience,
            "promotion" : promotion,
            "department":departments,
            "salary":salary}

df = pd.DataFrame([new_data])

st.write(df)

final_model = pickle.load(open("xgb_model_final", "rb"))
st.info("**Check the features you selected from the table above. If correct, press the Predict button.**")
if st.button("Predict"):
    prediction = final_model.predict(df)
    if prediction == 1:
        prediction = "leave"
    else:
        prediction = "stay"
    st.success(f"Your employee will ** {prediction}.**")