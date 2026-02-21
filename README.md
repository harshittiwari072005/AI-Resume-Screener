# 🚀 AI Resume Screening System

An AI-powered web application that automatically screens and ranks resumes based on their relevance to a job description using NLP and machine learning techniques.

Built with Django + TF-IDF + Skill Matching + Explainable AI insights to assist recruiters in making faster and smarter hiring decisions.

---

## ✨ Features

- 📄 Upload Job Description (PDF)
- 📂 Upload multiple resumes at once
- 🤖 AI-based resume ranking
- 📊 Final score based on:
  - Semantic similarity
  - Skill overlap
- 🏆 Top candidate highlighting
- 🥇 Rank badges
- 🧠 Explainability panel:
  - Matched skills
  - Missing skills
- 📈 Recruiter-friendly dashboard UI
- ⚡ Fast screening pipeline

---

## 🧠 How It Works

1. Job description and resumes are parsed from PDFs.
2. Text is cleaned using NLP preprocessing.
3. TF-IDF vectorization converts text into numerical features.
4. Cosine similarity measures relevance.
5. Skill extraction compares required vs candidate skills.
6. Final score is computed:


7. Candidates are ranked and displayed.

---

## 🖥️ System Architecture
User Upload → Django Backend → NLP Pipeline → Ranking Engine → Dashboard UI

---

## 🛠️ Tech Stack

- Python
- Django
- Scikit-learn
- spaCy
- NumPy
- HTML / Bootstrap
- PDF Parsing

---

## 📊 Example Output

- Ranked candidate list
- Final score
- Similarity score
- Skill score
- Matched skills
- Missing skills

---

## 🚀 How to Run Locally

### 1️⃣ Clone repo
git clone https://github.com/harshittiwari072005/AI-Resume-Screener.git

cd AI-Resume-Screener

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Install spaCy model
python -m spacy download en_core_web_sm

### 4️⃣ Run server
cd webapp
python manage.py runserver

Open: http://127.0.0.1:8000/

---

## 📁 Project Structure
AI_Resume_Screener/
│
├── nlp/ # NLP pipeline
├── parser/ # Resume parsing
├── data/ # Dataset
├── notebooks/ # Experiments
├── webapp/ # Django app
├── uploads/ # Uploaded files
└── README.md


---

## 🔮 Future Improvements

- Transformer embeddings (BERT / Sentence Transformers)
- Interview recommendation system
- Recruiter analytics dashboard
- Candidate feedback scoring
- Cloud deployment
- Resume clustering
- Hiring insights panel

---

## 🎯 Use Case

Designed for:

- HR teams
- Recruiters
- Campus hiring
- ATS automation
- Resume filtering

---

## 👨‍💻 Author

Harshit Tiwari

AI / ML Developer — NLP Projects

---

## ⭐ If you like this project

Give it a star — it helps a lot!  

## UI SCREENSHOT
<img width="1909" height="752" alt="image" src="https://github.com/user-attachments/assets/2e681cd3-c2c8-462c-b9ac-796a349171a8" />



<img width="995" height="697" alt="image" src="https://github.com/user-attachments/assets/542dcaf1-3b81-4554-906b-5372e602ec72" />




