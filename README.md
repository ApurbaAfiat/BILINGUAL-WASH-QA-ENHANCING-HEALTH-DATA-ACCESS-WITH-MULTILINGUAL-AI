LLM-Based QA for JMP WASH Dataset (Bangla-English Support)
📌 Overview

This project demonstrates the use of a Large Language Model (LLM) to support Water, Sanitation, and Hygiene (WASH)-related tasks under the WHO/UNICEF JMP framework.

The main feature is a Question Answering (QA) system that allows users to ask structured health and sanitation questions in both Bangla and English. The system uses a Retrieval-Augmented Generation (RAG) pipeline with multilingual embeddings for effective bilingual support.

✨ Features

✅ Dual-language (Bangla & English) support for queries.

✅ Retrieval-Augmented Generation (RAG) using FAISS.

✅ Multilingual Sentence Transformer for embeddings.

✅ Dynamic translation layer for runtime Bangla-to-English conversion.

✅ UTF-8 handling for Bangla outputs.

✅ Lightweight, interpretable, and fast architecture.


🏗️ System Architecture

The system uses RAG with the following components:

FAISS → Fast similarity search for retrieval.

SentenceTransformer (distiluse-base-multilingual-cased-v1) → Generates bilingual embeddings.

deep_translator (Google Translate API) → Enables runtime Bangla-English translation.

Flow:

User enters query (Bangla/English).

If Bangla → Query translated to English.

Vectorized using SentenceTransformer.

FAISS retrieves top relevant entries.

LLM generates final answer.

If Bangla → Answer translated back to Bangla.

📂 Data Preparation

Collected multiple JMP WASH Excel files.

Cleaned and merged them into a single structured CSV dataset.

Converted each row into a QA-style natural language prompt.

Maintained dataset in English only → added translation layer at runtime.

🧑‍💻 Preprocessing & Embeddings

Tokenization & Embedding with distiluse-base-multilingual-cased-v1.

Designed for low-resource languages → effective for Bangla-English tasks.

Embeddings stored and indexed with FAISS for retrieval.

📊 Evaluation

Evaluation conducted via manual scoring (1–5 scale) on:

Fluency (naturalness of language).

Relevance (contextual fit of the answer).

Accuracy (factual correctness).

This provided direct insight into system performance in both Bangla and English.

🚧 Key Challenges & Solutions
Challenge	Solution
Dataset in English only	Runtime Bangla-to-English translation with deep_translator
Bangla text display issues	UTF-8 encoded text files for Bangla responses
Lack of high-quality Bangla training data	Used multilingual embeddings instead of monolingual models
Misalignment of Bangla-English outputs	Future improvements: fine-tuned Bangla embeddings or custom translation models
Time constraints (academic workload, exams)	Limited optimization noted as future work
📈 Future Improvements

Incorporate summarization features.

Add voice interface for accessibility.

Extend support to local dialects of Bangla.

Fine-tune embeddings with native Bangla data.


# English Query
Q: What is the sanitation coverage in Bangladesh (2020)?

# Bangla Query
Q: বাংলাদেশে ২০২০ সালে স্যানিটেশন কভারেজ কত?













