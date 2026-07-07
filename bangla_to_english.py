from deep_translator import GoogleTranslator

def translate_query(text, target_lang='en'):
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print("Translation error:", e)
        return text

# ============================================
# 🔍 2. QA Pipeline: FAISS + Sentence Transformers
# ============================================
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import MinMaxScaler
import faiss
import numpy as np
import sys
import os

if os.name == "nt":
    import ctypes
    # Set console code page to UTF-8
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    sys.stdout.reconfigure(encoding='utf-8')


df = pd.read_csv("final_cleaned_jmp_dataset.csv")

# Step 1: Generate natural-language QA-style prompts
def generate_prompt(row):
    return (
        f"In {int(row['year'])}, the {row['indicator_name']} in {row['country_name']} "
        f"was approximately {round(row['value'], 2)}."
    )

df['prompt'] = df.apply(generate_prompt, axis=1)

# Step 2: Loaded sentence embedding model (multilingual)
model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

# Saved prompt list for search results
prompt_list = df['prompt'].tolist()

# Step 3 & 4: Load cached index/embeddings if they exist, else generate and save
index_file = "faiss_index.bin"
embeddings_file = "embeddings.npy"

if os.path.exists(index_file) and os.path.exists(embeddings_file):
    print("Loading cached FAISS index and embeddings...")
    embeddings = np.load(embeddings_file)
    index = faiss.read_index(index_file)
else:
    print("Generating embeddings and FAISS index (this may take a minute)...")
    embeddings = model.encode(prompt_list, show_progress_bar=True)
    np.save(embeddings_file, embeddings)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    faiss.write_index(index, index_file)

# Step 5: Define the Query Function
def query_qa(user_query, top_k=3):
    # Detect language: if contains Bengali script, translate to English
    lang = 'en'
    if any(ord(char) > 255 for char in user_query):
        user_query_translated = translate_query(user_query, 'en')
        lang = 'bn'
    else:
        user_query_translated = user_query

    # Embed the query
    query_embedding = model.encode([user_query_translated])
    D, I = index.search(np.array(query_embedding), top_k)

    # Retrieve top matches
    results = [prompt_list[i] for i in I[0]]

    # Combine results
    combined_response = "\n".join(results)

    # Translate response back to Bangla if needed
    if lang == 'bn':
        combined_response = translate_query(combined_response, 'bn')
    return combined_response

# Example usage:
answer = query_qa("২০২০ সালে সুদানে শিশু মৃত্যুর হার কত ছিল?")
print("Answer:", answer)

