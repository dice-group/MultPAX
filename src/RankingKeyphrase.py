# Get document (abstract) embedding representation from BERT model.
# Get words (present and absent keyphrases) embeddding representation from BERT Model.
# Compute the cosine similarity between doc2vec and words2vec, then return a sorted list as an output.

import glob
from scipy import spatial
import numpy as np
from scipy.spatial import distance

from sentence_transformers import SentenceTransformer, util


class RanKeyphrase:

    def __init__(self, input_dataset='./Output/PKE/') -> None:

        self.input_data= input_dataset     
        self.model = SentenceTransformer('all-MiniLM-L6-v2')


def ranking_keyphrases(self): 
        
    #iterate over all files in the present keyphrases.
    fNames= glob.glob(self.input_data+'*.txt')

    for file in fNames:
        # read the content of the input document.
        input_doc = open(self.input_data, mode='r').read()
        input_doc=input_doc.replace('\t', ' ').replace('\n', '')    

        similar_keyphrases= {}
        
        #---- compute ranking ---#    
        doc_embedding = self.model.encode(input_doc, convert_to_tensor=True)
        
        PKE_file = open(file, 'r') #--- Path of the present keyphrase ---#
        present_keyphrases = PKE_file.readlines()   
        
        keyphrase_embedding = self.model.encode(present_keyphrases, convert_to_tensor=True)

        #Compute cosine-similarits
        cosine_scores = util.pytorch_cos_sim(doc_embedding, keyphrase_embedding)
        
        final_keyphrases= {}
        #Output the pairs with their score
        for i in range(len(present_keyphrases)):
            final_keyphrases[present_keyphrases[i]]= cosine_scores[0][i]
        
        final_keyphrase=sorted(similar_keyphrases.items(), key=lambda x: x[1], reverse=True)
                
        #save ranked keyphrases into file
        
        with open('./Output/Ranking/'+file.split('/')[-1], 'w') as outFile:
            outFile.writelines(final_keyphrase)
        outFile.close()