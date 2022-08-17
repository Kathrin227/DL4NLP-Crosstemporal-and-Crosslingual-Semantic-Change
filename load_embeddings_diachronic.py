import numpy as np
import pickle

def read(file_vocab, file_embeddings, file_out, dtype='float'):
    f = open(file_vocab, 'rb')
    out = open(file_out, 'w')

    vectors = np.load(file_embeddings)
    words = pickle.load(f)
    matrix = np.load(file_embeddings)
    
    num = str(len(words))
    
    num += " "
    
    num += str(matrix.shape[1])
    
    num += ("\n")
    
    out.write(num)
    
    string = ""
    
    for i in range(len(words)):
        string += words[i]
        string += " "
        for vec in matrix[i]:
            string += str(vec)
            string+= " "
        string += "\n"
        
        out.write(string)
        string = ""
        
def compare_vocab(file_1, file_2):

    vocab_1 = open(file_1, 'rb')
    vocab_2 = open(file_2, 'rb')
    
    words_1 = pickle.load(vocab_1)
    print("The first wordlist has length: ", len(words_1))
    words_2 = pickle.load(vocab_2)
    print("The second wordlist has length: ", len(words_2))
    
    count_matches = 0
    
    if(words_1 == words_2):
        print("Lists are equal")
        return
    
    for i in range(len(words_2)):
        w_1 = words_2[i]
        for j in range(len(words_2)):
            w_2 = words_2[j]
            if (w_1==w_2):
                count_matches += 1
                #print(count_matches, w_1, w_2)
    
    print("There are ", count_matches, " matches in the word vectors")
    return
        
        
if __name__ == '__main__':
    """
    read("../fre-all_sgns/sgns/1800-vocab.pkl", "../fre-all_sgns/sgns/1800-w.npy", "../word2vec/fre_1800.word2vec")
    read("../fre-all_sgns/sgns/1810-vocab.pkl", "../fre-all_sgns/sgns/1810-w.npy", "../word2vec/fre_1810.word2vec")
    read("../fre-all_sgns/sgns/1820-vocab.pkl", "../fre-all_sgns/sgns/1820-w.npy", "../word2vec/fre_1820.word2vec")
    read("../fre-all_sgns/sgns/1830-vocab.pkl", "../fre-all_sgns/sgns/1830-w.npy", "../word2vec/fre_1830.word2vec")
    read("../fre-all_sgns/sgns/1840-vocab.pkl", "../fre-all_sgns/sgns/1840-w.npy", "../word2vec/fre_1840.word2vec")
    read("../fre-all_sgns/sgns/1850-vocab.pkl", "../fre-all_sgns/sgns/1850-w.npy", "../word2vec/fre_1850.word2vec")
    read("../fre-all_sgns/sgns/1860-vocab.pkl", "../fre-all_sgns/sgns/1860-w.npy", "../word2vec/fre_1860.word2vec")
    read("../fre-all_sgns/sgns/1870-vocab.pkl", "../fre-all_sgns/sgns/1870-w.npy", "../word2vec/fre_1870.word2vec")
    read("../fre-all_sgns/sgns/1880-vocab.pkl", "../fre-all_sgns/sgns/1880-w.npy", "../word2vec/fre_1880.word2vec")
    read("../fre-all_sgns/sgns/1890-vocab.pkl", "../fre-all_sgns/sgns/1890-w.npy", "../word2vec/fre_1890.word2vec")
    read("../fre-all_sgns/sgns/1900-vocab.pkl", "../fre-all_sgns/sgns/1900-w.npy", "../word2vec/fre_1900.word2vec")
    read("../fre-all_sgns/sgns/1910-vocab.pkl", "../fre-all_sgns/sgns/1910-w.npy", "../word2vec/fre_1910.word2vec")
    read("../fre-all_sgns/sgns/1920-vocab.pkl", "../fre-all_sgns/sgns/1920-w.npy", "../word2vec/fre_1920.word2vec")
    read("../fre-all_sgns/sgns/1930-vocab.pkl", "../fre-all_sgns/sgns/1930-w.npy", "../word2vec/fre_1930.word2vec")
    read("../fre-all_sgns/sgns/1940-vocab.pkl", "../fre-all_sgns/sgns/1940-w.npy", "../word2vec/fre_1940.word2vec")
    read("../fre-all_sgns/sgns/1950-vocab.pkl", "../fre-all_sgns/sgns/1950-w.npy", "../word2vec/fre_1950.word2vec")
    read("../fre-all_sgns/sgns/1960-vocab.pkl", "../fre-all_sgns/sgns/1960-w.npy", "../word2vec/fre_1960.word2vec")
    read("../fre-all_sgns/sgns/1970-vocab.pkl", "../fre-all_sgns/sgns/1970-w.npy", "../word2vec/fre_1970.word2vec")
    read("../fre-all_sgns/sgns/1980-vocab.pkl", "../fre-all_sgns/sgns/1980-w.npy", "../word2vec/fre_1980.word2vec")
    read("../fre-all_sgns/sgns/1990-vocab.pkl", "../fre-all_sgns/sgns/1990-w.npy", "../word2vec/fre_1990.word2vec")
    """
    
    compare_vocab("../word2vec/eng-ger/sgns/1990-vocab.pkl", "../ger-all_sgns/sgns/1990-vocab.pkl")
