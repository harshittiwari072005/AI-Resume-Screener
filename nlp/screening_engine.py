from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nlp.text_preprocessing import clean_text
from nlp.skill_extraction import extract_skills


def rank_resumes(jd_text, resume_texts):

    # Clean JD
    cleaned_jd = clean_text(jd_text)

    # Clean resumes
    cleaned_resumes = [clean_text(r) for r in resume_texts]

    # TF-IDF
    documents = [cleaned_jd] + cleaned_resumes

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    jd_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(jd_vector, resume_vectors).flatten()

    # Skill scoring
    jd_skills = extract_skills(cleaned_jd)

    skill_scores = []
    explanations = []

    for r in cleaned_resumes:
        skills = extract_skills(r)

        overlap = set(skills).intersection(set(jd_skills))
        missing = set(jd_skills) - set(skills)

        score = len(overlap) / len(jd_skills) if jd_skills else 0
        skill_scores.append(score)

        explanations.append({
            "matched": list(overlap),
            "missing": list(missing)
        })

    # Final score
    final_scores = []

    for sim, skill in zip(similarity_scores, skill_scores):
        final_scores.append(0.7 * sim + 0.3 * skill)

    # Rank
    ranked_indices = sorted(range(len(final_scores)),
                            key=lambda i: final_scores[i],
                            reverse=True)

    return ranked_indices, final_scores, similarity_scores, skill_scores, explanations
