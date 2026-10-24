# Resume Analyzer & Job Matcher

A web app that reads a resume (PDF/DOCX), extracts key information, and ranks the best matching jobs with a match score and a skill gap report.

## Features
- Upload resume in PDF or DOCX format
- Extracts skills, email, and phone number
- Matches resume against job descriptions using TF-IDF + skill matching
- Shows match percentage, matched skills, and missing skills
- Simple and clean Streamlit interface

## Tech Stack
- Python
- Streamlit
- pdfplumber, python-docx
- scikit-learn (TF-IDF, cosine similarity)
- spaCy, pandas

## How It Works
1. The resume text is extracted from the uploaded file.
2. Skills are detected using a skills database (`skills.json`).
3. Each job description is compared with the resume.
4. Final score = 40% text similarity + 60% skill match.
5. The top matching jobs are shown with missing skills to learn.

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/resume-analyzer-job-matcher.git
cd resume-analyzer-job-matcher
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## Project Structure
```
├── app.py          # Streamlit UI
├── parser.py       # Resume text extraction
├── extractor.py    # Skill/contact extraction
├── matcher.py      # Scoring logic
├── skills.json     # Skills database
└── data/jobs.csv   # Sample job listings
```

## Screenshots
(Add screenshots here)

## Future Improvements
- Semantic matching with sentence-transformers
- AI-based resume feedback
- Live job listings through an API
- Export analysis as a PDF report

## Author
Your Name | [LinkedIn](https://linkedin.com/in/your-profile)
