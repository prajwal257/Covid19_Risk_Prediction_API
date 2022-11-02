import column_dictionary
from column_dictionary import *
import pickle
import uvicorn
from fastapi import FastAPI
import numpy as np

app = FastAPI()
pickle_in = open("regressor.pkl", "rb")
regressor = pickle.load(pickle_in)

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.post("/predict")
def predict_risk(data:patient_details):
    data = data.dict()
    # Data we are getting from drop-downs
    sex = int(column_dictionary.gender_coded.get(data['sex']))                           # HTML attribute named sex.
    age = int(column_dictionary.age_coded.get(data['age']))                              # HTML attribute named age.
    blood_type = int(column_dictionary.blood_type_coded.get(data['blood_type']))         # HTML attribute named bloody_type.
    race = int(column_dictionary.race_coded.get(data.get("race")))                       # HTML attribute named race.
    smoking = int(column_dictionary.smoking_coded.get(data.get("smoking")))              # HTML attribute named smoking.
    working = int(column_dictionary.working_coded.get(data.get("working")))              # HTML attribute named working.
    country_name = int(column_dictionary.country_coded.get(data.get("country_name")))    # HTML attribute named country_name.
    # Data from text boxes...
    height = float(data.get('height'))
    weight = float(data.get('weight'))
    bmi = np.log(weight/(height*height))                                                 # HTML attribute named weight & height.
    # Data from radio buttons checkboxes
    public_transport_count = data['public_transport_count']                              # direct input
    worried = data['worried']                                                            # direct input
    covid19_positive = data['covid19_positive']                                          # direct input
    covid19_symptoms = data['covid19_symptoms']                                          # direct input
    covid19_contact = data['covid19_contact']                                            # direct input
    asthma = data['asthma']                                                              # direct input
    kidney_disease = data['kidney_disease']                                              # direct input
    liver_disease = data['liver_disease']                                                # direct input
    compromised_immune = data['compromised_immune']                                      # direct input
    heart_disease = data['heart_disease']                                                # direct input
    lung_disease = data['lung_disease']                                                  # direct input
    diabetes = data['diabetes']                                                          # direct input
    hiv_positive = data['hiv_positive']                                                  # direct input
    hypertension = data['hypertension']                                                  # direct input
    other_chronic = data['other_chronic']                                                # direct input
    nursing_home = data['nursing_home']                                                  # direct input
    health_worker = data['health_worker']                                                # direct input
    prediction = regressor.predict([[
        sex, age, bmi, blood_type, race, smoking, public_transport_count, working, worried, covid19_positive, 
        covid19_symptoms, covid19_contact, asthma, kidney_disease, liver_disease, compromised_immune, heart_disease, lung_disease, diabetes, 
        hiv_positive, hypertension, other_chronic, nursing_home, health_worker, country_name
    ]])
    return {"prediction": prediction[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")

# uvicorn app:app --reload