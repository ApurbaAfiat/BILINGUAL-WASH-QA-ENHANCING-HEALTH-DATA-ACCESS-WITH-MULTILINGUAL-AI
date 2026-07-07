# Bilingual WASH QA Chatbot

An interactive RAG (Retrieval-Augmented Generation) chatbot designed to answer queries about the **WASH (Water, Sanitation, and Hygiene)** and **World Bank development datasets** in both **Bangla** and **English**.

The project translates Bangla queries into English, performs semantic vector search over the processed dataset using **FAISS** and **Sentence Transformers**, retrieves the most relevant records, and translates the response back to Bangla if needed.

---

## Features
- 🌟 **Bilingual Q&A**: Type questions in either Bangla or English.
- ⚡ **FAISS Vector Search**: Fast semantic retrieval using Sentence Transformers (`distiluse-base-multilingual-cased-v1`).
- 💾 **Local Cache**: FAISS index and sentence embeddings are cached locally (`faiss_index.bin` and `embeddings.npy`) to enable instant start-up on subsequent runs.
- 🛠️ **Automated Preprocessing**: Scripts to clean and combine multiple CSV datasets.

---

## File Structure
- `dataset_ACMEAI.py`: Merges raw CSV datasets from the `All datasets` directory.
- `preprocess_jmp_dataset.py`: Cleans and normalizes columns of the merged dataset into `final_cleaned_jmp_dataset.csv`.
- `bangla_to_english.py`: Core RAG logic containing translation, embedding generation, index creation, and the query function.
- `run_chatbot.py`: Interactive CLI wrapper to run the chatbot in real-time.
- `testing.py`: Pre-defined script to test the model with sample queries.

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ApurbaAfiat/BILINGUAL-WASH-QA-ENHANCING-HEALTH-DATA-ACCESS-WITH-MULTILINGUAL-AI.git
   cd BILINGUAL-WASH-QA-ENHANCING-HEALTH-DATA-ACCESS-WITH-MULTILINGUAL-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install deep-translator pandas sentence-transformers scikit-learn faiss-cpu numpy
   ```

3. **Prepare the dataset**:
   If raw files are updated, run:
   ```bash
   python dataset_ACMEAI.py
   python preprocess_jmp_dataset.py
   ```

4. **Launch the Chatbot**:
   ```bash
   python run_chatbot.py
   ```

---

## Example Queries

### English
* *What was the hygiene status of Sudan in 2020?*
* *What was the under-5 mortality rate in Sudan in 2020?*

### Bangla
* *২০২০ সালে সুদানে শিশু মৃত্যুর হার কত ছিল?*
* *সুদানে কি মৌলিক খাবার পানির সুবিধা ভালো ছিল?*
