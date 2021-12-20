
from keybert import KeyBERT 
# check https://github.com/MaartenGr/KeyBERT for more pre-trained models

from pathlib import Path
import glob


class PKey_Extraction: 

    def __init__(self, input_dataset='../Inspec/docsutf8/'):
        self.input_dataset= input_dataset

        #check if output directories exist...
        Path("./Output/").mkdir(parents=True, exist_ok=True)
        Path("./Output/PKE/").mkdir(parents=True, exist_ok=True)
       
        Path("./Output/Ranking/").mkdir(parents=True, exist_ok=True)
        
        self.kw_model = KeyBERT()

    def extract_presentKeyphrases(self): 

        #iterate over all files in the dataset ... 
        fNames= glob.glob(self.input_dataset+'*.txt')

        for file in fNames:
            # read the content of the input document.
            input_doc = open(file, mode='r').read()
            input_doc=input_doc.replace('\t', ' ').replace('\n', '')

            # extract present keyphrases
            keywords = self.kw_model.extract_keywords(input_doc, keyphrase_ngram_range=(1, 3), 
                                            stop_words='english', use_mmr=True, diversity=0.5)
            
            # save keywods without relevance score into file
            final_keywords=""
            for keyword in keywords: 
                final_keywords+=keyword[0]+"\n"
            
            with open('./Output/PKE/'+file.split('/')[-1], 'w') as outFile:
                outFile.writelines(final_keywords.rstrip())
            outFile.close()

