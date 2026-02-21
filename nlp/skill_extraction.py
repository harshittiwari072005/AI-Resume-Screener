from nlp.skill_dictionary import TECH_SKILLS
def extract_skills(text):
    found_skills = []

    for skill in TECH_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))