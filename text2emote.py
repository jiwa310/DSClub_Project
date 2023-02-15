import pandas as pd
import numpy as np
import neattext.functions as nfx
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

df = pd.read_csv("emotion-dataset.csv")
df['Clean_Text'] = df['Text'].apply(nfx.remove_userhandles)
df['Clean_Text'] = df['Clean_Text'].apply(nfx.remove_stopwords)

Xfeatures = df['Clean_Text']
ylabels = df['Emotion']


pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression(max_iter = 256))])
x_train, x_test, y_train, y_test = train_test_split(Xfeatures, ylabels, test_size = 0.3)
pipe_lr.fit(x_train,y_train)
print("Accuracy:")
print(pipe_lr.score(x_test,y_test))

