from bangla_to_english import query_qa

test_queries = [
    "২০২০ সালে সুদানে শিশু মৃত্যুর হার কত ছিল?",
    "What was the hygiene status of Sudan in 2020?",
    "সুদানে ২০১৫ থেকে ২০২০ সালের মধ্যে পানির প্রবেশাধিকার কেমন ছিল?"
]

for query in test_queries:
    response = query_qa(query)
    print(f"\n Query: {query}")
    print(f" Response: {response}")

# Manual evaluation prompt
    print("Rate this output [1–5]:")
    print(" - Fluency: ___")
    print(" - Relevance: ___")
    print(" - Accuracy: ___")