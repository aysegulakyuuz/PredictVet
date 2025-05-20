
from flask import Flask, render_template, request
import pickle
import numpy as np
import json
import joblib
app = Flask(__name__)

model = joblib.load('model/animal_disease_model_compressed.joblib')

le_animal = joblib.load('le_animal_updated.pkl')  # Make sure not to overwrite this later!
le_disease = pickle.load(open('model/le_disease.pkl', 'rb'))
mlb_symptoms = pickle.load(open('model/mlb_symptoms.pkl', 'rb'))

with open('static/animal_info_reference.json', 'r') as f:
    animal_info = json.load(f)

with open('static/reference_data.json', 'r') as f:
    reference_data = json.load(f)

with open('static/symptom_groups.json', 'r') as f:
    symptom_groups = json.load(f)

@app.route('/')
def home():
    animal_list = sorted(animal_info.keys())
    return render_template('index.html',
        animal_list=animal_list,
        symptom_groups=symptom_groups,
        symptoms_selected=[],
        prediction_text=None,
        reference_info=None,
        animal=None,
        age=None,
        temperature=None)

@app.route('/predict', methods=['POST'])
def predict():
    animal = request.form.get('animal')
    age = request.form.get('age')
    temperature = request.form.get('temperature')
    symptoms = request.form.getlist('symptoms')

    animal_list = sorted(animal_info.keys())
    ref = animal_info.get(animal)
    selected = symptoms

    if not animal or not age or not temperature:
        return render_template('index.html', prediction_text='Please fill all fields.',
                               summary={
        "animal": animal,
        "age": age,
        "temperature": temperature,
        "symptoms": symptoms
    },
    animal_list=animal_list, animal=animal,
                               age=age, temperature=temperature,
                               symptoms_selected=selected, reference_info=ref,
                               symptom_groups=symptom_groups)

    try:
        age = float(age)
        temperature = float(temperature)
    except:
        return render_template('index.html', prediction_text='Invalid input: age and temperature must be numbers.',
                               animal_list=animal_list, animal=animal,
                               age=age, temperature=temperature,
                               symptoms_selected=selected, reference_info=ref,
                               symptom_groups=symptom_groups)

    if not (ref['age'][0] <= age <= ref['age'][1]):
        return render_template('index.html', prediction_text='Age must be between {}–{}.'.format(ref["age"][0], ref["age"][1]),
                               animal_list=animal_list, animal=animal,
                               age=age, temperature=temperature,
                               symptoms_selected=selected, reference_info=ref,
                               symptom_groups=symptom_groups)

    if not (ref['temperature'][0] <= temperature <= ref['temperature'][1]):
        return render_template('index.html', prediction_text='Temperature must be between {}–{} °C.'.format(ref["temperature"][0], ref["temperature"][1]),
                               animal_list=animal_list, animal=animal,
                               age=age, temperature=temperature,
                               symptoms_selected=selected, reference_info=ref,
                               symptom_groups=symptom_groups)

    if not symptoms:
        return render_template('index.html', prediction_text='Please select at least one symptom.',
                               animal_list=animal_list, animal=animal,
                               age=age, temperature=temperature,
                               symptoms_selected=selected, reference_info=ref,
                               symptom_groups=symptom_groups)

    animal_encoded = le_animal.transform([animal])[0]
    symptom_vector = mlb_symptoms.transform([symptoms])
    input_vector = np.hstack([[animal_encoded, age, temperature], symptom_vector.flatten()])

    prediction = model.predict(input_vector.reshape(1, -1))[0]
    predicted_disease = le_disease.inverse_transform([prediction])[0]

    return render_template('index.html', prediction_text='Predicted Disease: {}'.format(predicted_disease),
                           animal_list=animal_list, animal=animal,
                           age=age, temperature=temperature,
                           symptoms_selected=selected, reference_info=ref,
                           symptom_groups=symptom_groups)

if __name__ == '__main__':
    app.run(debug=True)
