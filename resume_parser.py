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
