import os
from django.conf import settings
from django.shortcuts import render

from parser.resume_parser import parse_resume
from nlp.screening_engine import rank_resumes

def home(request):

    results = None

    if request.method == "POST":

        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        jd_file = request.FILES.get("jd_file")
        resumes = request.FILES.getlist("resumes")

        # Save JD
        jd_path = os.path.join(settings.MEDIA_ROOT, jd_file.name)
        with open(jd_path, 'wb+') as f:
            for chunk in jd_file.chunks():
                f.write(chunk)

        # Extract JD text
        jd_text = parse_resume(jd_path)

        resume_texts = []
        resume_names = []

        for resume in resumes:

            resume_path = os.path.join(settings.MEDIA_ROOT, resume.name)

            with open(resume_path, 'wb+') as f:
                for chunk in resume.chunks():
                    f.write(chunk)

            text = parse_resume(resume_path)

            resume_texts.append(text)
            resume_names.append(resume.name)

        # Run ranking engine
        ranked_indices, final_scores, sim_scores, skill_scores, explanations = rank_resumes(jd_text, resume_texts)

        results = []

        for idx in ranked_indices:
            results.append({
                "name": resume_names[idx],
                "final": round(final_scores[idx], 3),
                "similarity": round(sim_scores[idx], 3),
                "skill": round(skill_scores[idx], 3),
                "matched": explanations[idx]["matched"],
                "missing": explanations[idx]["missing"]
            })

        print("Screening complete")

    return render(request, "home.html", {"results": results})