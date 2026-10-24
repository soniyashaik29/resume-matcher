import re, json

import os, json

BASE = os.path.dirname(__file__)
SKILLS = json.load(open(os.path.join(BASE, "skills.json"), encoding="utf-8"))

SKILLS = json.load(open("skills.json"))

def clean(text):
    return re.sub(r"\s+", " ", text.lower())

def extract_skills(text):
    text = clean(text)
    return sorted({s for s in SKILLS if re.search(rf"\b{re.escape(s)}\b", text)})

def extract_email(text):
    m = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return m.group(0) if m else None

def extract_phone(text):
    m = re.search(r"(\+?\d[\d\s\-]{8,14}\d)", text)
    return m.group(0) if m else None