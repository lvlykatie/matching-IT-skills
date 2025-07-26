import openai
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util
from thefuzz import fuzz
import torch

# Load .env & OpenAI key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Sentence-BERT
model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_skills_gpt(text):
    prompt = f"""
Given this list of skills, for each skill, detect its level as one of: beginner, intermediate, expert, unknown.

Input:
{text}

Return JSON:
[{{"skill": "python", "level": "intermediate"}}, ...]
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        import json
        return json.loads(response['choices'][0]['message']['content'])
    except:
        return []

def embed(texts):
    return model.encode(texts, convert_to_tensor=True)

def get_best_candidates(skill, standard_skills, top_k=3):
    fuzzy_scores = [(s, fuzz.token_set_ratio(skill, s)) for s in standard_skills]
    fuzzy_top = sorted(fuzzy_scores, key=lambda x: x[1], reverse=True)[:top_k]

    query_vec = embed([skill])[0]
    corpus_vec = embed(standard_skills)
    scores = util.cos_sim(query_vec, corpus_vec)[0]
    embed_top = sorted(zip(standard_skills, scores.tolist()), key=lambda x: x[1], reverse=True)[:top_k]

    combined = {s for s, _ in fuzzy_top + embed_top}
    return list(combined)

def choose_best_with_gpt(skill, candidates):
    prompt = f"""
Choose the best matching skill for: "{skill}"
Candidates: {candidates}
Return only the exact best match, or "None" if none applies.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response['choices'][0]['message']['content'].strip().strip('"')
    except:
        return "None"
