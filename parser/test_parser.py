from resume_parser import parse_resume

file_path = "uploads/sample_resume.pdf"  # change if docx
text = parse_resume(file_path)

print("Parsed text preview:\n")
print(text[:1000])
