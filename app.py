import streamlit as st
from src.extract.pdf_reader import extract_text_from_pdf
from src.summarize.langchain_summarizer import summarize_text
from src.quiz.tf_classifier import classify_question
from src.summarize.question_generator import generate_quiz_questions
from src.quiz.tf_classifier import classify_batch

st.set_page_config(page_title="AI Study Assistant", layout="wide")

st.title("📘 AI Study Assistant")

tabs = st.tabs(["📄 Upload PDF", "🧠 Quiz Me", "📊 About"])

# -------- TAB 1 --------
with tabs[0]:
    st.header("Upload and Summarize Study Material")
    uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_pdf is not None:
        # Save temporarily
        temp_path = f"data/{uploaded_pdf.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_pdf.read())

        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_pdf(temp_path)
            st.subheader("📜 Extracted Text:")
            st.text_area("Raw PDF Text", extracted_text[:2000], height=200)

        if st.button("🔍 Summarize"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(extracted_text)
                st.subheader("🧠 Summary:")
                st.write(summary)

                if st.button("🎯 Generate Quiz from Summary"):
                    with st.spinner("Generating quiz questions..."):
                        questions = generate_quiz_questions(summary, num_questions=5)
                        difficulties = classify_batch(questions)

                        st.subheader("📝 Quiz Questions with AI Difficulty:")
                        for q, d in zip(questions, difficulties):
                            st.markdown(f"**Q:** {q}<br>🔍 *Difficulty:* `{d}`", unsafe_allow_html=True)


# -------- TAB 2 --------
with tabs[1]:
    st.header("Question Difficulty Classifier")
    question_input = st.text_area("Enter a question:")

    if st.button("Classify"):
        if question_input.strip():
            difficulty = classify_question(question_input)
            st.success(f"Predicted Difficulty: **{difficulty.upper()}**")
        else:
            st.warning("Please enter a question.")

# -------- TAB 3 --------
with tabs[2]:
    st.header("📊 About This Project")
    st.markdown("""
    **AI Study Assistant** is a smart tool that:
    - Extracts and summarizes PDF study materials using LangChain + OpenAI
    - Classifies quiz question difficulty using TensorFlow
    - Built with Python, NumPy, Streamlit, LangChain, and more

    👩‍💻 Made by [Kaveesha Gimhani](https://github.com/kaveeshagim)
    """)

