# 📘 AI Study Assistant

[![Built with Python](https://img.shields.io/badge/Built%20with-Python-blue.svg)](https://www.python.org/)
[![Uses PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)](https://pytorch.org/)
[![Uses TensorFlow](https://img.shields.io/badge/TensorFlow-ML-orange)](https://www.tensorflow.org/)
[![LangChain Integrated](https://img.shields.io/badge/LangChain-LLM-blueviolet)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-June%202025-blue)]()

## 🧠 Project Overview

**AI Study Assistant** is a smart learning companion that:

- 📄 Extracts and analyzes PDF study materials
- 🧠 Summarizes complex concepts using **LangChain**
- 📝 Generates quizzes with **TensorFlow**
- 📊 Uses **NumPy** for intelligent preprocessing
- 🔍 Recognizes handwritten content using **PyTorch**

This project is built to give hands-on experience with popular AI frameworks while solving a real-world problem — making study easier.

## 🔧 Tech Stack

| Tool/Library | Purpose                                |
| ------------ | -------------------------------------- |
| Python       | Core language                          |
| NumPy        | Text/data preprocessing                |
| LangChain    | PDF Q&A and summarization              |
| TensorFlow   | Quiz classification (Easy/Medium/Hard) |
| PyTorch      | Handwriting recognition                |
| Streamlit    | UI for demo                            |

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Set up environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

## 🗂️ Project Structure

```bash
ai-study-assistant/
│
├── data/                  # PDF files, training datasets
├── notebooks/             # Jupyter notebooks for exploration
├── models/                # Saved models (TF & PyTorch)
├── src/
│   ├── extract/           # PDF reading & cleanup (NumPy)
│   ├── summarize/         # LangChain summarizer
│   ├── quiz/              # TensorFlow quiz classifier
│   └── vision/            # PyTorch handwriting model
├── app.py                 # Streamlit app
├── requirements.txt
└── README.md
```

## 📌 Features Roadmap

- [x] PDF Text Extraction
- [x] Topic Summarization (LangChain)
- [ ] Quiz Generator (TensorFlow)
- [ ] Image Recognition (PyTorch)
- [ ] UI with Streamlit or Gradio

## 📜 License

This project is licensed under the MIT License.

## 💡 Author

**Saif Ali** – [@saifaliy](https://github.com/saifaliy)

## 🏷️ Tags

`#AI` `#LangChain` `#PyTorch` `#TensorFlow` `#NumPy` `#Beginner-Project` `#StudyTools` `#PDFSummarizer`
