"""
 10-12-2023
 CSC461 – Assignment4 – NLP
 Muhammad Tayab
 FA21-BSE-030

Q1. Compute BoW, TF, IDF, and then TF.IDF values for each term in the following three sentences.
    S1: “data science is one of the most important courses in computer science”
    S2: “this is one of the best data science courses”
    S3: “the data scientists perform data analysis”
Q2. Compute the similarity between S1, S2, and S3 using cosine, manhattan, and euclidean distances.
"""
#     Q1-

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

# Define the three sentences
sentences = [
    "data science is one of the most important courses in computer science",
    "this is one of the best data science courses",
    "the data scientists perform data analysis"
]

# Bag of Words (BoW)
vectorizer_bow = CountVectorizer()
X_bow = vectorizer_bow.fit_transform(sentences)
bow_df = pd.DataFrame(X_bow.toarray(), columns=vectorizer_bow.get_feature_names_out())
print("Bag of Words (BoW):\n", bow_df)

# Term Frequency (TF)
vectorizer_tf = TfidfVectorizer(use_idf=False)
X_tf = vectorizer_tf.fit_transform(sentences)
tf_df = pd.DataFrame(X_tf.toarray(), columns=vectorizer_tf.get_feature_names_out())
print("\nTerm Frequency (TF):\n", tf_df)

# Inverse Document Frequency (IDF)
vectorizer_idf = TfidfVectorizer(use_idf=True)
X_idf = vectorizer_idf.fit_transform(sentences)
idf_df = pd.DataFrame(X_idf.toarray(), columns=vectorizer_idf.get_feature_names_out())
print("\nInverse Document Frequency (IDF):\n", idf_df)

# TF.IDF
vectorizer_tfidf = TfidfVectorizer()
X_tfidf = vectorizer_tfidf.fit_transform(sentences)
tfidf_df = pd.DataFrame(X_tfidf.toarray(), columns=vectorizer_tfidf.get_feature_names_out())
print("\nTF.IDF:\n", tfidf_df)

#      Q2--
from sklearn.metrics.pairwise import cosine_similarity, manhattan_distances, euclidean_distances
import numpy as np

# Defining the three sentences
sentences = [
    "data science is one of the most important courses in computer science",
    "this is one of the best data science courses",
    "the data scientists perform data analysis"
]

# Transforming sentences using TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(sentences)

# Converting TF-IDF matrix to dense array
tfidf_matrix = X_tfidf.toarray()

# Computing similarity using cosine similarity
cosine_similarities = cosine_similarity(tfidf_matrix)
print("Cosine Similarity:\n", cosine_similarities)

# Computing similarity using Manhattan distance
manhattan_distances = manhattan_distances(tfidf_matrix)
print("\nManhattan Distances:\n", manhattan_distances)

# Computing similarity using Euclidean distance
euclidean_distances = euclidean_distances(tfidf_matrix)
print("\nEuclidean Distances:\n", euclidean_distances)
