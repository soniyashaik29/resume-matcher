from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from extractor import extract_skills

def tfidf_score(resume, job):
    vec = TfidfVectorizer(stop_words="english")
    tfidf = vec.fit_transform([resume, job])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0]

def skill_match(resume, job):
    r, j = set(extract_skills(resume)), set(extract_skills(job))
    if not j: return 0, [], []
    matched, missing = r & j, j - r
    return len(matched) / len(j), sorted(matched), sorted(missing)

def final_score(resume, job):
    t = tfidf_score(resume, job)
    s, matched, missing = skill_match(resume, job)
    return round((0.4 * t + 0.6 * s) * 100, 1), matched, missing