import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np
import re
import torch

# === Load data ===
df = pd.read_excel("data/courses_flattened.xlsx")
taxonomy_df = pd.read_csv("taxonomy/taxonomy.csv")

# === Clean & get standard skills ===
standard_skills = taxonomy_df[
    taxonomy_df["Dimension"] == "skills"
]["name"].dropna().str.lower().unique().tolist()

# === Load model ===
model = SentenceTransformer('all-MiniLM-L6-v2')
standard_embeddings = model.encode(standard_skills, convert_to_tensor=True)

# === Preprocessing skill string
def preprocess(text):
    return re.sub(r"[^\w\s\-+/]", "", text.strip().lower())

# === Semantic Matching
def semantic_match(raw_skills: str, threshold: float = 0.6):
    if not isinstance(raw_skills, str):
        return [], 0, 0, 0.0, None

    matched, scores = [], []
    skills = [s.strip() for s in raw_skills.split(',') if s.strip()]
    total = len(skills)
    for skill in skills:
        skill_clean = preprocess(skill)
        query_emb = model.encode(skill_clean, convert_to_tensor=True)
        cosine_scores = util.cos_sim(query_emb, standard_embeddings)[0]
        best_score, best_idx = torch.max(cosine_scores, dim=0)
        scores.append(best_score.item())
        if best_score.item() >= threshold:
            matched.append(standard_skills[best_idx])
        else:
            matched.append(f"[Unmatched] {skill}")
    match_count = sum(1 for m in matched if not m.startswith("[Unmatched]"))
    avg_score = round(np.mean(scores), 4) if scores else None
    match_rate = round(match_count / total * 100, 2) if total else 0.0
    return matched, match_count, total, match_rate, avg_score
