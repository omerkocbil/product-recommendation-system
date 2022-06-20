import pickle
    
with open("code/model/word2vec_model.pkl", "rb") as f:
    model = pickle.load(f)

def recommend_products(product_id, n=15):
    return model.wv.similar_by_word(product_id, topn=n)