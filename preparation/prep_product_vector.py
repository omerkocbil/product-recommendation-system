import pandas as pd
import random as random
import pickle

data = pd.read_csv("../data/case_study_data_v2.csv")

##Create word vectors and prepare data for word2vec
clients = data["client"].unique().tolist()
print(len(clients))

#split train and validation
client_ids = [clients[i] for i in range(round(0.9 * len(clients)))]

train_data = data[data['client'].isin(client_ids)]
validation_data = data[~data['client'].isin(client_ids)]

#create train word vector
train_word_vector = []
for id in train_data['client'].unique().tolist():
    vector = train_data[train_data["client"] == id]["product_id"].tolist()
    train_word_vector.append(vector)

#create validation word vector
validation_word_vector = []
for id in validation_data['client'].unique().tolist():
    vector = validation_data[validation_data["client"] == id]["product_id"].tolist()
    validation_word_vector.append(vector)

#save word vectors
word_vectors = (train_word_vector, validation_word_vector)
with open("../data/word_vectors.pkl", "wb") as f:
    pickle.dump(word_vectors, f, protocol=pickle.HIGHEST_PROTOCOL)