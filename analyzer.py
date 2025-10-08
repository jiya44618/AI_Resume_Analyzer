import streamlit as st
import PyPDF2
import docx

st.title("AI Resume Analyzer")
st.write("Upload your resume (PDF or DOCX) to analyze it.")

# File upload
uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

if uploaded_file is not None:
    text = ""

    # Read PDF
    if uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    # Read DOCX
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])

    # Show resume content
    st.subheader("Resume Content:")
    st.text_area("", text, height=300)

    # Detect skills
    keywords = ["Python", "Java", "Machine Learning", "Excel", "SQL", "C++", "Communication", "Data Analysis"]
    found_skills = [kw for kw in keywords if kw.lower() in text.lower()]

    st.subheader("Detected Skills:")
    if found_skills:
        st.write(", ".join(found_skills))
    else:
        st.write("No predefined skills detected.")

