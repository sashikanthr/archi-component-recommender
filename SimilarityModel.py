from gensim.models.word2vec import Word2Vec

def word_2_vec(component_names):
    model = Word2Vec(sentences=component_names, vector_size=64, sg=1, window=1, min_count=2, workers=8)
    print(model.wv.most_similar("entity 1"))
    print(model.wv.similarity("entity 1", "entity 2"))


