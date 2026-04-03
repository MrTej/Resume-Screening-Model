# AI-Powered Resume Screening & Candidate Matching System

## 📌 Overview

This project implements an **AI-driven resume screening system** that automatically evaluates and ranks candidates based on their suitability for different job roles. Using Natural Language Processing (NLP) and transformer-based embeddings, the system compares resume content against job categories to generate a **fit score**, enabling efficient and scalable candidate shortlisting.

---

## 🚀 Features

* 📄 **Resume Parsing**: Processes and extracts text from structured datasets of resumes.
* 🧠 **Semantic Matching**: Uses transformer models to compute similarity between resumes and job roles.
* 🏆 **Candidate Ranking**: Ranks candidates based on their relevance to specific job categories.
* 📊 **Performance Evaluation**: Measures model accuracy using ground truth labels.
* ⚖️ **Bias Detection**: Flags potential bias-related terms in resume content.
* 💾 **Export Results**: Saves ranked candidate outputs for further analysis.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** – Data handling and preprocessing
* **spaCy** – Named Entity Recognition (NLP)
* **Sentence-Transformers (SBERT)** – Semantic similarity modeling
* **Scikit-learn** – (optional for evaluation/extension)
* **Google Colab** – Development environment

---

## ⚙️ How It Works

1. **Data Loading**

   * Resume data is loaded from a CSV dataset containing resume text and job categories.

2. **Preprocessing**

   * Text is cleaned and prepared for NLP processing.

3. **Embedding Generation**

   * Resumes and job categories are converted into dense vector representations using a pre-trained transformer model.

4. **Similarity Computation**

   * Cosine similarity is calculated between resume embeddings and job category embeddings to produce a **fit score**.

5. **Ranking**

   * Candidates are ranked based on their fit score for each job category.

6. **Evaluation**

   * Model performance is evaluated by comparing predicted job categories with actual labels.

---

## 📂 Dataset

The project uses a resume dataset containing:

* **Resume Text (`Resume_str`)**
* **Job Category (`Category`)**
* **Resume ID**

This allows for supervised evaluation of how well the model predicts job-role alignment.

---

## 📈 Results

* Achieved a baseline accuracy of **~56%** using semantic similarity with general-purpose embeddings.
* Performance can be improved using:

  * Enhanced job descriptions
  * More advanced embedding models (e.g., `all-mpnet-base-v2`)
  * Hybrid scoring (semantic + keyword matching)
  * Fine-tuning on labeled data

---

## 🔍 Future Improvements

* Fine-tune transformer models for domain-specific classification
* Integrate real-world job descriptions instead of category labels
* Build a web interface (e.g., Streamlit) for interactive resume screening
* Implement advanced skill extraction and matching
* Optimize performance for large-scale datasets

---

## 🎯 Use Cases

* Automated resume screening for recruiters
* Candidate-job matching systems
* HR analytics and talent acquisition tools
* AI-driven hiring platforms

---

## 📌 Conclusion

This project demonstrates how modern NLP techniques can be applied to automate and improve the recruitment process. While the current system provides a strong baseline, it also opens the door for more advanced, production-ready solutions in AI-powered hiring.

---
