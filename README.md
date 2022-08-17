# DL4NLP: Crosstemporal and Crosslingual Semantic Change

The following code is part of our final project for the seminar "Deep Learning for Natural Language Processing"

As our code heavily relies on the two existing Mapping Processes for Cross-Lingual and Cross-Temporal Word Embedding Alignment, our code was initially integrated in these repositories. The file

  [identify_cosine_sim.py](https://github.com/Kathrin227/DL4NLP-Crosstemporal-and-Crosslingual-Semantic-Change/blob/main/identify_cosine_sim.py)
  
uses functions directly imported from [this GitHub](https://github.com/williamleif/histwords). The imports at the top of the file may need to be adapted. For the visualization of the data, the [file /viz/common.py](https://github.com/williamleif/histwords/blob/master/viz/common.py) from that distribution needs to be adapted to include

  * the correct temproal range in *line 80*, which works as (start,end,step). The year for end will actually be the last year before end that can be reached through the given step size if the end year itself is not reachable.
  
  * the correct path for the fully aligned word2vec data in *line 86*. 
  
  The files for the fully aligned embeddings that we produced on the basis of the embeddings provided [here](https://nlp.stanford.edu/projects/histwords/) are available in our [sciebo directory](https://uni-bielefeld.sciebo.de/s/gtIjITSM0Fvjciu).
  
  [There](https://uni-bielefeld.sciebo.de/s/gtIjITSM0Fvjciu) you can also find our full tables for all embedding timeframes.
  
  
To adapt the embeddings provided by Hamilton et al. for cross-lingual alignment with [VecMap](https://github.com/artetxem/vecmap) you can adapt the file paths in [load_embeddings_diachronic.py](https://github.com/Kathrin227/DL4NLP-Crosstemporal-and-Crosslingual-Semantic-Change/blob/main/load_embeddings_diachronic.py). To visualize and evaluate the embeddings cross-temporally you can re-adapt them back into the original format (saving embeddings for both languages in one file) by using [transform_crosslingual_embeddings.py](https://github.com/Kathrin227/DL4NLP-Crosstemporal-and-Crosslingual-Semantic-Change/blob/main/transform_crosslingual_embeddings.py). Please make sure to adapt all file-paths and to save the embeddings correctly.

For our cross-lingual alignment, we used bilingual dictionaries provided [here](https://github.com/facebookresearch/MUSE).
