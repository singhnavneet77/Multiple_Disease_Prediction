
import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu

# Set up the Streamlit page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="👨‍🦰🤶")

# Get the absolute path of the current working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths for your saved models
heart_disease_model_path = os.path.join(working_dir, 'saved_models/heart.pkl')
kidney_disease_model_path = os.path.join(working_dir, 'saved_models/kindey.pkl')

# Check if the model files exist before attempting to load them

if os.path.exists(heart_disease_model_path):
    heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
else:
    st.error(f"Heart disease model file not found at {heart_disease_model_path}")

if os.path.exists(kidney_disease_model_path):
    kidney_disease_model = pickle.load(open(kidney_disease_model_path, 'rb'))
else:
    st.error(f"Kidney disease model file not found at {kidney_disease_model_path}")


# Sidebar menu options
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction", 
                           [
                            'Heart Disease Prediction',
                            'Kidney Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart', 'person'],
                           default_index=0)



# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using Machine Learning")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain Types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol in mg/dl")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_disease_result = ""
    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, 
                      oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])
        if prediction[0] == 1:
            heart_disease_result = "This person has heart disease"
        else:
            heart_disease_result = "This person does not have heart disease"
    
    st.success(heart_disease_result)

# Kidney Disease Prediction
if selected == 'Kidney Disease Prediction':
    st.title("Kidney Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')
    with col2:
        blood_pressure = st.text_input('Blood Pressure')
    with col3:
        specific_gravity = st.text_input('Specific Gravity')
    with col4:
        albumin = st.text_input('Albumin')
    with col5:
        sugar = st.text_input('Sugar')
    with col1:
        red_blood_cells = st.text_input('Red Blood Cell')
    with col2:
        pus_cell = st.text_input('Pus Cell')
    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')
    with col4:
        bacteria = st.text_input('Bacteria')
    with col5:
        blood_glucose_random = st.text_input('Blood Glucose Random')
    with col1:
        blood_urea = st.text_input('Blood Urea')
    with col2:
        serum_creatinine = st.text_input('Serum Creatinine')
    with col3:
        sodium = st.text_input('Sodium')
    with col4:
        potassium = st.text_input('Potassium')
    with col5:
        haemoglobin = st.text_input('Haemoglobin')
    with col1:
        packed_cell_volume = st.text_input('Packet Cell Volume')
    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')
    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')
    with col4:
        hypertension = st.text_input('Hypertension')
    with col5:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')
    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')
    with col2:
        appetite = st.text_input('Appetite')
    with col3:
        peda_edema = st.text_input('Peda Edema')
    with col4:
        aanemia = st.text_input('Aanemia')

    kidney_disease_result = ""
    if st.button("Kidney's Test Result"):
        user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
                      red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                      blood_glucose_random, blood_urea, serum_creatinine, sodium,
                      potassium, haemoglobin, packed_cell_volume,
                      white_blood_cell_count, red_blood_cell_count, hypertension,
                      diabetes_mellitus, coronary_artery_disease, appetite,
                      peda_edema, aanemia]
        user_input = [float(x) for x in user_input]
        prediction = kidney_disease_model.predict([user_input])
        if prediction[0] == 1:
            kidney_disease_result = "The person has kidney disease"
        else:
            kidney_disease_result = "The person does not have kidney disease"
    
    st.success(kidney_disease_result)
