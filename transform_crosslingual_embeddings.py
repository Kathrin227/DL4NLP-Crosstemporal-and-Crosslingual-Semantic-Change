import numpy as np
import pickle

def read(file_english, file_german, out_vocab, out_npy):
    f_e = open(file_english, encoding='utf-8' , errors='surrogateescape')
    words_en, vecs_en = read_embeddings(f_e)
    
    f_g = open(file_german, encoding='utf-8' , errors='surrogateescape')
    words_ger, vecs_ger = read_embeddings(f_g)

    	
    
    words_total = words_en + words_ger
    print(len(words_total))
    vecs_total = np.concatenate((vecs_en, vecs_ger), axis=0)
    
    vocab = open(out_vocab, 'wb')
    npy = open(out_npy, 'wb')
    
    pickle.dump(words_total, vocab)
    vocab.close()
    
    np.save(npy, vecs_total)
    npy.close()
        


def read_embeddings(file, threshold=0, vocabulary=None, dtype='float'):
    header = file.readline().split(' ')
    count = int(header[0]) if threshold <= 0 else min(threshold, int(header[0]))
    dim = int(header[1])
    words = []
    matrix = np.empty((count, dim), dtype=dtype) if vocabulary is None else []
    for i in range(count):
        word, vec = file.readline().split(' ', 1)
        if vocabulary is None:
            words.append(word)
            matrix[i] = np.fromstring(vec, sep=' ', dtype=dtype)
        elif word in vocabulary:
            words.append(word)
            matrix.append(np.fromstring(vec, sep=' ', dtype=dtype))
    return (words, matrix) if vocabulary is None else (words, np.array(matrix, dtype=dtype))
            
if __name__ == '__main__':
    """
    read("../word2vec/eng-fre/fre_trans_1800.word2vec", "../word2vec/eng-fre/eng_trans_1800.word2vec", "../word2vec/eng-fre/sgns/1800-vocab.pkl", "../word2vec/eng-fre/sgns/1800-w.npy")
    read("../word2vec/eng-fre/fre_trans_1810.word2vec", "../word2vec/eng-fre/eng_trans_1810.word2vec", "../word2vec/eng-fre/sgns/1810-vocab.pkl", "../word2vec/eng-fre/sgns/1810-w.npy")
    read("../word2vec/eng-fre/fre_trans_1820.word2vec", "../word2vec/eng-fre/eng_trans_1820.word2vec", "../word2vec/eng-fre/sgns/1820-vocab.pkl", "../word2vec/eng-fre/sgns/1820-w.npy")
    read("../word2vec/eng-fre/fre_trans_1830.word2vec", "../word2vec/eng-fre/eng_trans_1830.word2vec", "../word2vec/eng-fre/sgns/1830-vocab.pkl", "../word2vec/eng-fre/sgns/1830-w.npy")
    read("../word2vec/eng-fre/fre_trans_1840.word2vec", "../word2vec/eng-fre/eng_trans_1840.word2vec", "../word2vec/eng-fre/sgns/1840-vocab.pkl", "../word2vec/eng-fre/sgns/1840-w.npy")
    read("../word2vec/eng-fre/fre_trans_1850.word2vec", "../word2vec/eng-fre/eng_trans_1850.word2vec", "../word2vec/eng-fre/sgns/1850-vocab.pkl", "../word2vec/eng-fre/sgns/1850-w.npy")
    read("../word2vec/eng-fre/fre_trans_1860.word2vec", "../word2vec/eng-fre/eng_trans_1860.word2vec", "../word2vec/eng-fre/sgns/1860-vocab.pkl", "../word2vec/eng-fre/sgns/1860-w.npy")
    read("../word2vec/eng-fre/fre_trans_1870.word2vec", "../word2vec/eng-fre/eng_trans_1870.word2vec", "../word2vec/eng-fre/sgns/1870-vocab.pkl", "../word2vec/eng-fre/sgns/1870-w.npy")
    read("../word2vec/eng-fre/fre_trans_1880.word2vec", "../word2vec/eng-fre/eng_trans_1880.word2vec", "../word2vec/eng-fre/sgns/1880-vocab.pkl", "../word2vec/eng-fre/sgns/1880-w.npy")
    read("../word2vec/eng-fre/fre_trans_1890.word2vec", "../word2vec/eng-fre/eng_trans_1890.word2vec", "../word2vec/eng-fre/sgns/1890-vocab.pkl", "../word2vec/eng-fre/sgns/1890-w.npy")

    read("../word2vec/eng-fre/fre_trans_1900.word2vec", "../word2vec/eng-fre/eng_trans_1900.word2vec", "../word2vec/eng-fre/sgns/1900-vocab.pkl", "../word2vec/eng-fre/sgns/1900-w.npy")
    read("../word2vec/eng-fre/fre_trans_1910.word2vec", "../word2vec/eng-fre/eng_trans_1910.word2vec", "../word2vec/eng-fre/sgns/1910-vocab.pkl", "../word2vec/eng-fre/sgns/1910-w.npy")
    read("../word2vec/eng-fre/fre_trans_1920.word2vec", "../word2vec/eng-fre/eng_trans_1920.word2vec", "../word2vec/eng-fre/sgns/1920-vocab.pkl", "../word2vec/eng-fre/sgns/1920-w.npy")
    read("../word2vec/eng-fre/fre_trans_1930.word2vec", "../word2vec/eng-fre/eng_trans_1930.word2vec", "../word2vec/eng-fre/sgns/1930-vocab.pkl", "../word2vec/eng-fre/sgns/1930-w.npy")
    read("../word2vec/eng-fre/fre_trans_1940.word2vec", "../word2vec/eng-fre/eng_trans_1940.word2vec", "../word2vec/eng-fre/sgns/1940-vocab.pkl", "../word2vec/eng-fre/sgns/1940-w.npy")
    read("../word2vec/eng-fre/fre_trans_1950.word2vec", "../word2vec/eng-fre/eng_trans_1950.word2vec", "../word2vec/eng-fre/sgns/1950-vocab.pkl", "../word2vec/eng-fre/sgns/1950-w.npy")
    read("../word2vec/eng-fre/fre_trans_1960.word2vec", "../word2vec/eng-fre/eng_trans_1960.word2vec", "../word2vec/eng-fre/sgns/1960-vocab.pkl", "../word2vec/eng-fre/sgns/1960-w.npy")
    read("../word2vec/eng-fre/fre_trans_1970.word2vec", "../word2vec/eng-fre/eng_trans_1970.word2vec", "../word2vec/eng-fre/sgns/1970-vocab.pkl", "../word2vec/eng-fre/sgns/1970-w.npy")
    read("../word2vec/eng-fre/fre_trans_1980.word2vec", "../word2vec/eng-fre/eng_trans_1980.word2vec", "../word2vec/eng-fre/sgns/1980-vocab.pkl", "../word2vec/eng-fre/sgns/1980-w.npy")
    read("../word2vec/eng-fre/fre_trans_1990.word2vec", "../word2vec/eng-fre/eng_trans_1990.word2vec", "../word2vec/eng-fre/sgns/1990-vocab.pkl", "../word2vec/eng-fre/sgns/1990-w.npy")
    """
    read("../word2vec/eng-ger/ger_trans_1890.word2vec", "../word2vec/eng-ger/eng_trans_1890.word2vec", "../word2vec/eng-ger/sgns/1890-vocab.pkl", "../word2vec/eng-ger/sgns/1890-w.npy")

