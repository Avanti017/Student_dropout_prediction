import streamlit as st
import pickle 
import pandas as pd
import numpy as ny

file1 = open('student_pred_model.pkl', 'rb')
rfc1 = pickle.load(file1)
file1.close()

x_columns = ['Application mode', 'Application order', 'Course',
       'Previous qualification', 'Nationality', 'Mother\'s qualification',
       'Father\'s qualification', 'Mother\'s occupation', 'Father\'s occupation',
       'Admission grade', 'Displaced', 'Educational special needs', 'Debtor',
       'Tuition fees up to date', 'Gender', 'Scholarship holder',
       'Age at enrollment', 'International',
       'Curricular units 1st sem (credited)',
       'Curricular units 1st sem (enrolled)',
       'Curricular units 1st sem (evaluations)',
       'Curricular units 1st sem (approved)',
       'Curricular units 1st sem (grade)',
       'Curricular units 1st sem (without evaluations)',
       'Curricular units 2nd sem (credited)',
       'Curricular units 2nd sem (enrolled)',
       'Curricular units 2nd sem (evaluations)',
       'Curricular units 2nd sem (approved)',
       'Curricular units 2nd sem (grade)',
       'Curricular units 2nd sem (without evaluations)', 'Unemployment rate',
       'Inflation rate', 'GDP']

# Initialize Variables
application_mode = 15
application_order = 1
course = 9254
previous_qualification = 1
nationality = 1
mother_qualification = 1
father_qualification = 3
mother_occupation = 3
father_occupation = 3
admission_grade = 142.5
displaced = 1
educational_special_needs =0
debtor =0
tuition_fees_up_to_date = 0
gender = 1
scholarship_holder = 0 
age_at_enrollment = 19
international = 0
curricular_units_first_sem_credited = 0
curricular_units_first_sem_enrolled = 6
curricular_units_first_sem_eval = 6
curricular_units_first_sem_approved = 6
curricular_units_first_sem_grade = 14
curricular_units_first_sem_no_eval = 0
curricular_units_second_sem_credited = 0
curricular_units_second_sem_enrolled = 6
curricular_units_second_sem_eval = 6
curricular_units_second_sem_approved = 6
curricular_units_second_sem_grade = 13.6
curricular_units_second_sem_no_eval = 0
unemployment_rate = 13.9
inflation_rate = -0.3
gdp = 0.79
target = 1


st.markdown("""
<!-- Load Google Font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredericka+the+Great&display=swap" rel="stylesheet">

<!-- Use the font for the heading -->
<h1 style="font-family: 'Fredericka the Great', serif; font-weight:500; font-style:normal; color: #235789;">
    Endura AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<!-- Load Google Font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredericka+the+Great&display=swap" rel="stylesheet">

<!-- Use the font for the heading -->
<h3 style="font-family: 'Fredericka the Great', serif; font-weight:500; font-style:normal; color: #c45714;">
    Helping College Students Achieve their Higher Ed Goals
</h3>
""", unsafe_allow_html=True)


st.write("Thousands of students step into college each year with big dreams; yet the reality of higher education tells a different story. In the United States alone, around one-third of undergraduate students dropout out of their programs because of financial burden, mental health issues, and other prevelant obstacles. To combat this, Endura predicts the likelyhood of such circumstances to prevent such an instance. Endura helps students get the help and support they need in order to achieve their goals of higher education.")
st.write(" ")
st.write(" ")

st.markdown("""
<!-- Load Google Font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredericka+the+Great&display=swap" rel="stylesheet">

<!-- Use the font for the heading -->
<h4 style="font-family: 'Fredericka the Great', serif; font-weight:599; font-style:normal; color: #c45714;">
    Continue to Endura Dropout Risk Predict:
</h4>
""", unsafe_allow_html=True)

# Application Mode
modes_map={"Regular National Applicants":1, "Ordinance No. 612/93":2, "Applicants from the Azores region":5, "Holders of other higher courses":7, "Ordinance No. 854-B/99": 10, "International student (bachelor)":15, "1st phase - special contingent (Madeira Island)": 16, "2nd phase - general contingent":17, "3rd phase - general contingent": 18, "Ordinance No. 533-A/99, item b2) (Different Plan)": 26, "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,"Over 23 years old":39, "Transfer":42,"Change of course":43, "Technological specialization diploma holders":44,  "Change of institution/course": 51,"Short cycle diploma holders": 53,"Change of institution/course (International)":51}

mode = st.selectbox('Application Mode', list(modes_map.keys()), help = "How has the student applied for the program?")
application_mode = modes_map[mode]
# st.write(application_mode)

# Application Order
application_order = st.slider("Student Program Preference Ranking (0-9)", 0,9,0,help="0 = first choice, 9 = last choice.")

#Course
courses_map = {"Biofuel Production Technologies": 33, "Animation and Multimedia Design": 171, "Social Service (evening attendance)": 8014, "Agronomy": 9003, "Communication Design": 9070, "Veterinary Nursing": 9085,"Informatics Engineering": 9119, "Equinculture": 9130, "Management": 9147, "Social Service": 9238, "Tourism": 9254, "Nursing": 9500, "Oral Hygiene": 9556, "Advertising and Marketing Management": 9670, "Journalism and Communication": 9773, "Basic Education": 9853,"Management (evening attendance)": 9991}

course_name = st.selectbox("Student Course", list(courses_map.keys()))
course = courses_map[course_name]
# st.write(course)

# Previous Qualification
qualification_map = {"Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43}
student_qual = st.selectbox("Previous Qualifications", list(qualification_map.keys()))
previous_qualification = qualification_map[student_qual]
# st.write(previous_qualification)

# Nationality
countries_map = {"Portuguese": 1, "German": 2, "Spanish": 6, "Italian": 11, "Dutch": 13, "English": 14, "Lithuanian": 17, "Angolan": 21, "Cape Verdean": 22, "Guinean": 24, "Mozambican": 25, "Santomean": 26, "Turkish": 32, "Brazilian": 41, "Romanian": 62, "Moldova (Republic of)": 100, "Mexican": 101, "Ukrainian": 103, "Russian": 105, "Cuban": 108, "Colombian": 109}
country = st.selectbox("Select Student Nationality", list(countries_map.keys()), help = "Due to limited data the range of nationalities is small")
nationality = countries_map[country]
# st.write(nationality)

# Mother's Qualification
m_qual_map = education_levels = {"Secondary Education - 12th Year of Schooling or Eq.": 1, "Higher Education - Bachelor's Degree": 2, "Higher Education - Degree": 3, "Higher Education - Master's": 4, "Higher Education - Doctorate": 5, "Frequency of Higher Education": 6, "12th Year of Schooling - Not Completed": 9, "11th Year of Schooling - Not Completed": 10, "7th Year (Old)": 11, "Other - 11th Year of Schooling": 12, "10th Year of Schooling": 14, "General commerce course": 18, "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19, "Technical-professional course": 22, "7th year of schooling": 26, "2nd cycle of the general high school course": 27, "9th Year of Schooling - Not Completed": 29, "8th year of schooling": 30, "Unknown": 34, "Can't read or write": 35, "Can read without having a 4th year of schooling": 36, "Basic education 1st cycle (4th/5th year) or equiv.": 37, "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38, "Technological specialization course": 39, "Higher education - degree (1st cycle)": 40, "Specialized higher studies course": 41, "Professional higher technical course": 42, "Higher Education - Master (2nd cycle)": 43, "Higher Education - Doctorate (3rd cycle)": 44}

mother_qual = st.selectbox("Select Mother's Qualifications", list(m_qual_map.keys()))
mother_qualification = m_qual_map[mother_qual]
# st.write(mother_qualification)

# Father's Qualification
f_qual_map = education_levels = {"Secondary Education - 12th Year of Schooling or Eq.": 1, "Higher Education - Bachelor's Degree": 2, "Higher Education - Degree": 3, "Higher Education - Master's": 4, "Higher Education - Doctorate": 5, "Frequency of Higher Education": 6, "12th Year of Schooling - Not Completed": 9, "11th Year of Schooling - Not Completed": 10, "7th Year (Old)": 11, "Other - 11th Year of Schooling": 12, "2nd year complementary high school course": 13, "10th Year of Schooling": 14, "General commerce course": 18, "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19, "Complementary High School Course": 20, "Technical-professional course": 22, "Complementary High School Course - not concluded": 25, "7th year of schooling": 26, "2nd cycle of the general high school course": 27, "9th Year of Schooling - Not Completed": 29, "8th year of schooling": 30, "General Course of Administration and Commerce": 31, "Supplementary Accounting and Administration": 33, "Unknown": 34, "Can't read or write": 35, "Can read without having a 4th year of schooling": 36, "Basic education 1st cycle (4th/5th year) or equiv.": 37, "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38, "Technological specialization course": 39, "Higher education - degree (1st cycle)": 40, "Specialized higher studies course": 41, "Professional higher technical course": 42, "Higher Education - Master (2nd cycle)": 43, "Higher Education - Doctorate (3rd cycle)": 44}

father_qual = st.selectbox("Select Father's Qualifications", list(f_qual_map.keys()))
father_qualification = f_qual_map[father_qual]
# st.write(father_qualification)

# Mother's Occupation
m_occ_map = education_levels =  {"Student": 0, "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1, "Specialists in Intellectual and Scientific Activities": 2, "Intermediate Level Technicians and Professions": 3, "Administrative staff": 4, "Personal Services, Security and Safety Workers and Sellers": 5, "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6, "Skilled Workers in Industry, Construction and Craftsmen": 7, "Installation and Machine Operators and Assembly Workers": 8, "Unskilled Workers": 9, "Armed Forces Professions": 10, "Other Situation": 90, "(blank)": 99, "Health professionals": 122, "teachers": 123, "Specialists in information and communication technologies (ICT)": 125, "Intermediate level science and engineering technicians and professions": 131, "Technicians and professionals, of intermediate level of health": 132, "Intermediate level technicians from legal, social, sports, cultural and similar services": 134, "Office workers, secretaries in general and data processing operators": 141, "Data, accounting, statistical, financial services and registry-related operators": 143, "Other administrative support staff": 144, "personal service workers": 151, "sellers": 152, "Personal care workers and the like": 153, "Skilled construction workers and the like, except electricians": 171, "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173, "Workers in food processing, woodworking, clothing and other industries and crafts": 175, "cleaning workers": 191, "Unskilled workers in agriculture, animal production, fisheries and forestry": 192, "Unskilled workers in extractive industry, construction, manufacturing and transport": 193, "Meal preparation assistants": 194}

mother_occ = st.selectbox("Select Mother's Occupation", list(m_occ_map.keys()))
mother_occupation = m_occ_map[mother_occ]
# st.write(mother_occupation)

# Father's Occupation
f_occ_map = education_levels =  {"Student": 0, "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1, "Specialists in Intellectual and Scientific Activities": 2, "Intermediate Level Technicians and Professions": 3, "Administrative staff": 4, "Personal Services, Security and Safety Workers and Sellers": 5, "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6, "Skilled Workers in Industry, Construction and Craftsmen": 7, "Installation and Machine Operators and Assembly Workers": 8, "Unskilled Workers": 9, "Armed Forces Professions": 10, "Other Situation": 90, "(blank)": 99, "Armed Forces Officers": 101, "Armed Forces Sergeants": 102, "Other Armed Forces personnel": 103, "Directors of administrative and commercial services": 112, "Hotel, catering, trade and other services directors": 114, "Specialists in the physical sciences, mathematics, engineering and related techniques": 121, "Health professionals": 122, "Teachers": 123, "Specialists in finance, accounting, administrative organization, public and commercial relations": 124, "Intermediate level science and engineering technicians and professions": 131, "Technicians and professionals, of intermediate level of health": 132, "Intermediate level technicians from legal, social, sports, cultural and similar services": 134, "Information and communication technology technicians": 135, "Office workers, secretaries in general and data processing operators": 141, "Data, accounting, statistical, financial services and registry-related operators": 143, "Other administrative support staff": 144, "Personal service workers": 151, "Sellers": 152, "Personal care workers and the like": 153, "Protection and security services personnel": 154, "Market-oriented farmers and skilled agricultural and animal production workers": 161, "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence": 163, "Skilled construction workers and the like, except electricians": 171, "Skilled workers in metallurgy, metalworking and similar": 172, "Skilled workers in electricity and electronics": 174, "Workers in food processing, woodworking, clothing and other industries and crafts": 175, "Fixed plant and machine operators": 181, "Assembly workers": 182, "Vehicle drivers and mobile equipment operators": 183, "Unskilled workers in agriculture, animal production, fisheries and forestry": 192, "Unskilled workers in extractive industry, construction, manufacturing and transport": 193, "Meal preparation assistants": 194, "Street vendors (except food) and street service providers": 195}

father_occ = st.selectbox("Select Father's Occupation", list(f_occ_map.keys()))
father_occupation = f_occ_map[father_occ]
# st.write(father_occupation)

# Admission Grade
first_ad_grade = st.slider("Select Admission Grade %", 0 , 100,0, help = "Student grade given during college admission")
admission_grade = first_ad_grade *2 

# Displaced? 
yn_displaced = st.radio("Was student displaced?", ("Yes", "No"))
if yn_displaced == "Yes": 
    displaced = 1
else:
    displaced = 0

# Educational Special Needs?
needs = st.radio("Does the student have any educations special needs?", ("Yes", "No"))
if needs == "Yes": 
    educational_special_needs = 1
else:
    educational_special_needs = 0

# Debt
debt = st.radio("Is the student in debt?", ("Yes", "No"))
if debt == "Yes": 
    debtor = 1
else:
    deptor = 0

# Tuition Fees up to Date?
tuition = st.radio("Are tuition fees up to date?", ("Yes", "No"))
if tuition == "Yes": 
    tuition_fees_up_to_date = 1
else:
    tuition_fees_up_to_date = 0

# Gender
gen = st.selectbox("Sex:", ["Female", "Male", "Other"])
if gen == "Female": 
    gender = 0
else:
    gender = 1

# Scholarship Holder
schol = st.radio("Is the student a scholarship holder", ("Yes", "No"))
if schol == "Yes": 
    scholarship_holder = 1
else:
    scholarship_holder = 0

# Age at enrollemnt
age_at_enrollment = st.number_input("Student age at enrollment:", min_value = 0, max_value = 120, value =18, step = 1)
# st.write(age_at_enrollment)

# International Student
inter= st.radio("Is the student an international student?", ("Yes", "No"))
if inter == "Yes": 
    international = 1
else:
    international = 0



#FIRST SEM
# Curricular Units (credited/taken) first semester
curricular_units_first_sem_credited = st.number_input("Enter number of curricular units credited in the first semester", min_value=0, step=1, format="%d", help="Number of courses credited from previous work or experience (so the student didn’t have to take them again)")

# Curricular Units enrolled first semester
curricular_units_first_sem_enrolled = st.number_input("Enter number of curricular units enrolled in the first semester", min_value=0, step=1, format="%d", help="Number of courses student has registered for in first semester")

# Curricular Units first semester evaluations
curricular_units_first_sem_eval = st.number_input("Enter number of evaluations the student has taken in the first semester", min_value=0, step=1, format="%d")

# Curricular Units first semester approved
curricular_units_first_sem_approved = st.number_input("Enter number of curricular units passed in the first semester", min_value=0, step=1, format="%d", help="Classes passed")

# Curricular Units first semester grade
grade = st.slider("Enter average grade for first semester (%)", 0,100,0)
curricular_units_first_sem_grade = 20 * grade/100

# Curricular Units first semester no evaluation
curricular_units_first_sem_no_eval = st.number_input("Number of curricular units without evalutions in the 1st semester", min_value = 0, step =1, format = "%d", help="Number of courses in which there was no evaluation or the student didn’t participate in any evaluation")









#SECOND SEM
# Curricular Units (credited/taken) second semester
curricular_units_second_sem_credited = st.number_input("Enter number of curricular units credited in the second semester", min_value=0, step=1, format="%d", help="Number of courses credited from previous work or experience (so the student didn’t have to take them again)")

# Curricular Units enrolled second semester
curricular_units_second_sem_enrolled = st.number_input("Enter number of curricular units enrolled in the second semester", min_value=0, step=1, format="%d", help="Number of courses student has registered for in first semester")

# Curricular Units second semester evaluations
curricular_units_second_sem_eval = st.number_input("Enter number of evaluations the student has taken in the second semester", min_value=0, step=1, format="%d")

# Curricular Units second semester approved
curricular_units_second_sem_approved = st.number_input("Enter number of curricular units passed in the second semester", min_value=0, step=1, format="%d", help="Classes passed")

# Curricular Units second semester grade
grades = st.slider("Enter average grade for second semester (%)", 0,100,0)
curricular_units_second_sem_grade = 20 * grades/100

# Curricular Units second semester no evaluation
curricular_units_second_sem_no_eval = st.number_input("Number of curricular units without evalutions in the 2nd semester", min_value = 0, step =1, format = "%d", help="Number of courses in which there was no evaluation or the student didn’t participate in any evaluation")

#Unemployment Rate
unemployment_rate = st.number_input("Enter the current unemployment rate for your country (%)")

#Inflation Rate
inflation_rate = st.number_input("Enter the current inflation rate for your country (%)")

#GDP
gdp_mean = -0.009256198347107426
gdp_std = 2.259985867959604
user_gdp = st.number_input("Enter you country's current GDP (in trillions):", min_value=0.0, step=0.1)
gdp = (user_gdp - gdp_mean) / gdp_std



# Put in Data Frame
x_new = pd.DataFrame([[
    application_mode,
    application_order,
    course,
    previous_qualification,
    nationality,
    mother_qualification,
    father_qualification,
    mother_occupation,
    father_occupation,
    admission_grade,
    displaced,
    educational_special_needs,
    debtor,
    tuition_fees_up_to_date,
    gender,
    scholarship_holder,
    age_at_enrollment,
    international,
    curricular_units_first_sem_credited,
    curricular_units_first_sem_enrolled,
    curricular_units_first_sem_eval,
    curricular_units_first_sem_approved,
    curricular_units_first_sem_grade,
    curricular_units_first_sem_no_eval,
    curricular_units_second_sem_credited,
    curricular_units_second_sem_enrolled,
    curricular_units_second_sem_eval,
    curricular_units_second_sem_approved,
    curricular_units_second_sem_grade,
    curricular_units_second_sem_no_eval,
    unemployment_rate,
    inflation_rate,
    gdp
]],columns = x_columns)


if st.button('Predict Dropout'):

   prob = rfc1.predict_proba(x_new)
   dropout_prob = prob[0][1]
   st.subheader("Risk of dropout is: " + str(dropout_prob*100)+ "%")


st.markdown(
    """
    <style>
    h1,{
    color: #FF1493;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #dee5fc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<!-- Load Google Font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredericka+the+Great&display=swap" rel="stylesheet">

<!-- Use the font for the heading -->
<h3 style="font-family: 'Fredericka the Great', serif; font-weight:500; font-style:normal; color: #c45714;">
    Resources for those at risk of dropout: 
</h3>
""", unsafe_allow_html=True)

resources = [
    ("Dropout prevention and alternatives for at‑risk college students",
     "https://www.watermarkinsights.com/resources/blog/dropout-prevention-and-alternatives-for-at-risk-college-students/"),
    ("Dropout Prevention and Intervention — NC DPI",
     "https://www.dpi.nc.gov/students-families/student-support/dropout-prevention-and-intervention"),
    ("National Dropout Prevention Center",
     "https://dropoutprevention.org/"),
    ("15 Effective Strategies for Improving Student Attendance and Reducing Dropout (PDF)",
     "https://web.ped.nm.gov/wp-content/uploads/2025/01/Dropout-Prevention-Technical-Assistance-Guidance.pdf"),
    ("The Impacts of Dropout Prevention Programs — Mathematica",
     "https://www.mathematica.org/projects/the-impacts-of-dropout-prevention-programs"),
    ("Reframing School Dropout as a Public Health Issue",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC2099272/"),
]

for title, url in resources:
    st.write(f"- [{title}]({url})")