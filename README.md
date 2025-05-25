🐾 PredictVet: AI-Supported Animal Disease Prediction System

PredictVet is a machine learning-powered web application that predicts potential animal diseases based on user input, including animal type, age, temperature, and symptoms. Designed for veterinarians, livestock managers, and researchers, PredictVet aims to support early diagnosis and improve animal health management.

🚀 Live Demo
👉 [https://predictvet.onrender.com](https://predictvet.onrender.com)

🎯 Project Goal

To develop a user-friendly AI system for early disease detection in animals, helping to reduce diagnostic delays and improve decision-making in veterinary care.

---

🧠 Features

- Disease prediction using a trained **RandomForestClassifier**
- Species-specific validation for age and temperature
- Multi-symptom input with grouped checkboxes
- Real-time backend API using Flask
- Interactive Power BI dashboards
- Responsive design for all devices
- Cloud deployment via Render.com

---

 🛠️ Technologies Used

- **Backend:** Python 3.8+, Flask, Scikit-learn, Joblib  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Render.com  
- **Visualization:** Microsoft Power BI

---

 📊 Power BI Visuals

- Symptom frequency bar chart  
- Disease distribution by species  
- Avg. temperature and age by disease  

---

 📂 Project Structure

PredictVet/
│
├── static/ # CSS & JS
├── templates/ # HTML frontend
├── model/ # Trained model files
├── app.py # Flask backend logic
├── requirements.txt # Python dependencies
├── Procfile # For Render.com deployment
└── README.md # Project overview



---

📈 Model Performance

- Accuracy: **81%**  
- Weighted F1-score: **0.81**  
- Macro F1-score: **0.63**  
(Note: imbalance due to rare disease entries.)

---

🔮 Future Improvements

- Expand dataset with more species and conditions  
- Add confidence scores for predictions  
- Enable input of symptom severity and duration  
- Add multilingual support  
- Develop mobile version for offline rural use  

---

 📚 References

Veterinary sources used to enrich the dataset include:
- [CDC – Brucellosis](https://www.cdc.gov/brucellosis/index.html)  
- [DairyNZ – Mastitis](https://www.dairynz.co.nz/animal/cow-health/mastitis/)  
- [Merck Vet Manual – BVD, Johne’s Disease](https://www.merckvetmanual.com)  
- [FAO – Theileriosis, CCPP](https://www.fao.org/animal-health/en/)  
- [WHO – Rabies](https://www.who.int/news-room/fact-sheets/detail/rabies)  
- [NADIS – Mange](https://www.nadis.org.uk/disease-a-z/farm-animals/mange/)  
- And others listed in the [Full Report (PDF)](https://github.com/aysegulakyuuz/PredictVet/blob/main/Aysegul%20Akyuz%20diploma%20project%20.pdf)

---
 👩‍💻 Author

**Ayşegül Akyuz**  
Data Science & AI  
University of Economics and Human Sciences in Warsaw

📫 [ayseegulakyuz@gmail.com](mailto:aysegulakyuuz@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/ayseegulakyuz/)

---
