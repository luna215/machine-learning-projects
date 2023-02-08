import numpy as np

import pandas as pd
import getpass

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def main():
    data = pd.read_csv("./data.csv", error_bad_lines=False)
    print(data.head())
    data = data.dropna()
    data["strength"] = data["strength"].map({0: "Weak", 
                                         1: "Medium",
                                         2: "Strong"})
    
    def word(password):
        return [i for i in password]

    x = np.array(data["password"])
    y = np.array(data["strength"])
    tdif = TfidfVectorizer()
    x = tdif.fit_transform(x)
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.05, 
                                                    random_state=42)

    model = RandomForestClassifier()
    model.fit(xtrain, ytrain)

    user = getpass.getpass("Enter password: ")
    data = tdif.transform([user]).toarray()
    output = model.predict(data)
    print(output)
    print(model.score(xtest, ytest))



if __name__ == "__main__":
    print("main:here..")
    main()