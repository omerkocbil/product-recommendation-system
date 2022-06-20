import pandas as pd
import pickle

data = pd.read_csv("code/data/case_study_data_v2.csv")

#create word vector and prepare data for word2vec
word_vector = []
for id in data['client'].unique().tolist():
    vector = data[data["client"] == id]["product_id"].tolist()
    word_vector.append(vector)

#save word vector
with open("code/data/word_vector.pkl", "wb") as f:
    pickle.dump(word_vector, f, protocol=pickle.HIGHEST_PROTOCOL)