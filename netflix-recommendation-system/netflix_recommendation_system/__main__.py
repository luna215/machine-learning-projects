import numpy as np
import re
import string

import pandas as pd
import nltk

from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

nltk.download("stopwords")
stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words("english"))

def clean(text: string) -> string:
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)

    return text

def netflix_recommendation(title, columns, indices, similarity):
    index = indices[title]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[0:10]
    movieindices = [i[0] for i in similarity_scores]

    return columns["Title"].iloc[movieindices]

def main():
    data = pd.read_csv("./netflix_data.csv")

    data = data[["Title", "Description", "Content Type", "Genres"]]
    data = data.dropna()
    data["Title"] = data["Title"].apply(clean)

    """
    Use Genre column as feature to recommend similar content to user
    """
    feature = data["Genres"].tolist()
    tfidf = text.TfidfVectorizer(input=feature, stop_words="english")
    tfidf_matrix = tfidf.fit_transform(feature)
    similarity = cosine_similarity(tfidf_matrix)

    """
    Set Title column as an index so that we can find similar content
    by giving the title of the movie or TV show as input
    """
    indices = pd.Series(data.index, index=data["Title"]).drop_duplicates()

    print(netflix_recommendation("girlfriend", data, indices, similarity))

if __name__ == "__main__":
    main()