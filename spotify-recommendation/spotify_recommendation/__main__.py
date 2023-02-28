import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

sns.set()

data = pd.read_csv("./spotify.csv")

df = data.drop(columns=["id", "name", "artists", "release_date", "year"])


datatypes = ["int16", "int32", "int64", "float16", "float32", "float64"]

normalization = data.select_dtypes(include=datatypes)

for col in normalization.columns:
    MinMaxScaler(col)

kmeans = KMeans(n_clusters=10)
features = kmeans.fit_predict(normalization)
data['features'] = features
MinMaxScaler(data['features'])


class SpotifyRecommendation:

    def __init__(self, dataset):
        self.dataset = dataset

    def recommend(self, songs, amount=1):
        distance = []
        song = self.dataset[(self.dataset.name.str.lower() == songs.lower())].head(1).values[0]
        rec = self.dataset[self.dataset.name.str.lower() != songs.lower()]

        for songs in tqdm(rec.values):
            d = 0
            for col in np.arange(len(rec.columns)):
                if not col in [1, 6, 12, 14, 18]:
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            
            distance.append(d)
        
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['artists', 'name']

        return rec[columns][:amount]


recommendations = SpotifyRecommendation(data)
from pprint import pprint
pprint(recommendations.recommend("I Want It That Way", 10))
