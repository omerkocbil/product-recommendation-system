import pickle
from gensim.models import Word2Vec

with open("code/data/word_vector.pkl", "rb") as f:
    word_vector = pickle.load(f)

#train word2vec model
model = Word2Vec(sentences=word_vector, window=10, sg=1, hs=0, negative=20,
                 alpha=0.03, min_alpha=0.0007, vector_size=100, epochs=10, 
                 seed=24)

#save the model
with open("code/model/word2vec_model.pkl", "wb") as f:
    pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)