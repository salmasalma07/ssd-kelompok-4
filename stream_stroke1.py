import numpy as np
import joblib
import streamlit as st

# Membaca model
stroke_model = joblib.load(open('stroke_model1.sav', 'rb'))


# Judul web
st.title('Prediksi Penyakit Stroke')

# Input pengguna
Age_Years_input = st.text_input('Input usia dalam tahun')
Sex_input = st.selectbox(
    "Pilih jenis kelamin:",
    ('Laki-Laki', 'Perempuan')
)
gender_mapping = {'Laki-Laki': 1, 'Perempuan': 0}
Sex_y = gender_mapping[Sex_input]


ever_married_input = st.selectbox(
    "Pilih ever_married:",
    ('Menikah', 'Tidak Menikah')
)
ever_married_mapping = {'Menikah': 1, 'Tidak Menikah': 0}
ever_married_y = ever_married_mapping[ever_married_input]


work_type_input = st.selectbox(
    "Pilih work_type:",
    ('Govt_Job', 'Never_Work','Private','Self-Employed','Children')
)
work_type_mapping = {'Govt_Job': 0, 'Never_Work': 1, 'Private': 2, 'Self-Employed': 3, 'Children': 4}
work_type_y = work_type_mapping[work_type_input]


Residence_type_input = st.selectbox(
    "Pilih Residence_type:",
    ('Urban', 'Rudal')
)
Residence_type_mapping = {'Urban': 1, 'Rudal': 0}
Residence_type_y = Residence_type_mapping[Residence_type_input]

smoking_status_input = st.selectbox(
    "Pilih smoking_statuse:",
    ('Unknown', 'fomerly smoked','never smoked','smokes')
)
smoking_status_type_mapping = {'Unknown': 0, 'fomerly smoked': 1, 'never smoked': 2, 'smokes': 3}
smoking_status_y = smoking_status_type_mapping[smoking_status_input]


hypertension_input = st.text_input('Input hypertension dengan nilai 0 (rendah) atau 1 (tinggi)')
heart_disease_input = st.text_input('Input heart_disease dengan nilai 0 (tidak) atau 1 (ya)')
avg_glucose_level_input = st.text_input('Input nilai avg_glucose (mg/dl)')
bmi_input = st.text_input('Input nilai bmi')


# Validasi input
if Age_Years_input.strip() and Sex_input.strip() and hypertension_input.strip() and heart_disease_input.strip() and ever_married_input.strip() and work_type_input.strip() and Residence_type_input.strip() and avg_glucose_level_input.strip() and bmi_input.strip():
    Age_Years = float(Age_Years_input)
    Sex = float(Sex_y)
    hypertension = float(hypertension_input)
    heart_disease = float(heart_disease_input)
    ever_married = float(ever_married_y)
    work_type = float(work_type_y)
    Residence_type = float(Residence_type_y)
    avg_glucose_level = float(avg_glucose_level_input)
    bmi = float(bmi_input)
    smoking_status = float(smoking_status_y)

     # Code untuk prediksi
    # Membuat tombol untuk prediksi
    if st.button('Test Prediksi Stroke'):
        input_data = np.array([Age_Years, Sex, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]).reshape(1, -1)
        stroke_prediction = stroke_model.predict(input_data)

        # Menampilkan hasil prediksi
        if stroke_prediction[0] == 1:
            stroke_prediction = 'Seseorang tidak terkena Stroke'
        else:
            stroke_prediction = 'Seseorang terkena Stroke'

        st.success(stroke_prediction)
else:
    st.warning('Mohon lengkapi semua kolom input.')
