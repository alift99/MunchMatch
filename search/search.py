import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# df_vectors = pd.read_csv('assets/search/restaurant_vectors.csv')
# VECTORIZER = pickle.load(open('assets/search/query_vectorizer.pkl', 'rb'))

# def search_restaurants(query):
#     query = query.lower().strip()
#     query_vector = VECTORIZER.transform([query])
#     similarity_scores = cosine_similarity(query_vector, df_vectors.drop(['name'], axis=1))

#     df_vectors['similarity_scores'] = similarity_scores[0]
#     df_vectors = df_vectors.sort_values(by='similarity_scores', ascending=False)
#     return df_vectors['name'][:16].to_numpy()

