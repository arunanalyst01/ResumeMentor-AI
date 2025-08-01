from pdfminer.high_level import extract_text
def extract_resume_text(file_path):
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        return f"Error reading file: {e}"

# Try it
resume_path = "E:/ResumeMentor-AI/datasets/resume_dataset/Arunachalam-Resume.pdf"
text = extract_resume_text(resume_path)
print(text[:1000])  # show first 1000 characters
from skill_matcher import load_job_roles, match_skills
from resume_parser import extract_resume_text

resume_text = extract_resume_text("E:/ResumeMentor-AI/datasets/resume_dataset/Sample_resume.pdf")
job_data = load_job_roles(r"E:\ResumeMentor-AI\datasets\job_roles.csv")  
matches = match_skills(resume_text, job_data)
for role, score, matched_skills in matches:
    print(f"Role: {role}")
    print(f"Match Score: {score:.2f}%")
    print(f"Matched Skills: {matched_skills}")
    print("="*40)
    import os
from resume_parser import extract_resume_text
from skill_matcher import load_job_roles, match_skills

job_data = load_job_roles("datasets/job_roles.csv")
folder_path = "datasets/resume_dataset/"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        print(f"📄 Processing {filename}")
        file_path = os.path.join(folder_path, filename)
        resume_text = extract_resume_text(file_path)
        matches = match_skills(resume_text, job_data)

        for role, score, matched_skills in matches[:3]:
            print(f"Role: {role}")
            print(f"Match Score: {score:.2f}%")
            print(f"Matched Skills: {matched_skills}")
            print("-" * 40)
        print("=" * 60 + "\n")

