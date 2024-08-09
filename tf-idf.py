from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Never jump over the lazy dog quickly.",
    "A quick brown dog jumps over the lazy fox."
]

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Get the feature names (terms)
feature_names = vectorizer.get_feature_names_out()

# Convert the tfidf_matrix to a dense array
dense_tfidf = tfidf_matrix.todense()

# Display the TF-IDF scores
for doc_idx, doc in enumerate(dense_tfidf):
    print(f"Document {doc_idx + 1} TF-IDF Scores:")
    for term_idx, score in enumerate(doc.tolist()[0]):
        print(f"Term: {feature_names[term_idx]}, Score: {score:.4f}")
    print("\n")
