import streamlit as st, pandas as pd
from parser import extract_text
from extractor import extract_skills, extract_email
from matcher import final_score

st.title("Resume Analyzer & Job Matcher")
file = st.file_uploader("Upload resume", type=["pdf", "docx"])

if file:
    text = extract_text(file)
    st.subheader("Detected Skills")
    st.write(extract_skills(text))

    jobs = pd.read_csv("data/jobs.csv")
    results = []
    for _, row in jobs.iterrows():
        score, matched, missing = final_score(text, row["description"])
        results.append((row["title"], row["company"], score, matched, missing))

    results.sort(key=lambda x: x[2], reverse=True)
    for title, company, score, matched, missing in results[:5]:
        with st.expander(f"{title} at {company}: {score}%"):
            st.write("✅ Matched:", matched)
            st.write("❌ Missing:", missing)