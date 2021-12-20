
import pandas as pd 
import glob
import requests
from pathlib import Path
import os

from nltk.stem import WordNetLemmatizer
from py_babelnet.calls import BabelnetAPI

class AKey_Extraction: 

    def __init__(self, PKE_path='./Output/PKE'):

        self.inputPath= PKE_path

        Path("./Output/AKE/").mkdir(parents=True, exist_ok=True)
        Path("./Output/AKE-babelnet/").mkdir(parents=True, exist_ok=True)

        self.api = BabelnetAPI('6a01c7b8-50a2-4a18-9385-635ab5e8e489')
        self.lemmatizer = WordNetLemmatizer()

    
    def preprocess_keywords_ngrams(self, inputFile):
        '''
        process keyphrases to link with DBpedia
        based on ngram matching
        '''
        present_keyphrase = pd.read_csv(inputFile, header= None)
        
        keywordsfull= present_keyphrase[0].tolist()  
        keywords=[]
        for keyword in keywordsfull:
            keyword=keyword.replace("'","")
            words=keyword.split(" ")

            keywords.append(keyword)
            lastindex=len(words)-1
            currentlen=len(words)-1
            firstind=0
            while currentlen>0:
                lastind=firstind+currentlen-1
                if lastind <= lastindex:
                    keywords.append(" ".join(words[firstind:lastind+1]))
                    firstind=firstind+1
                else:
                    currentlen=currentlen-1
                    firstind=0
        output= ""
        for word in keywords: 
            
            output+="<entity>"+word+"</entity> "
                    
        return output


        # save named entities URIs from DBpedia into file
    def save_dict_to_file(dic, fName):
        
        f = open('./Output/AKE/'+fName,'w')
        f.write(str(dic))
        f.close()

    def extract_absentKeyphrases(self):

        fNames= glob.glob(self.inputPath+"/*.txt")

        for file in fNames:
            keywords = self.preprocess_keywords_ngrams(file)
            #print(keywords)
            mydata= 'text={"agstring":"'+keywords+'","maxkeywords":10,"topics":[]}&type=json'
            #print(mydata)
            resp=requests.post("http://localhost:8080/AGDISTIS",data=mydata)
            
            json_data= resp.json()
            
            linked_entities=""
            
            for url in json_data['topNodes']: 
                
                linked_entities+=url['entityURL']+"\n"
                
            save_dict_to_file(linked_entities, file.split('/')[-1])


    def babelNet_linking(self, word):     

        word_lemma= self.lemmatizer.lemmatize(word)
        senses = self.api.get_senses(lemma = word_lemma, pos="NOUN", searchLang = "EN")    
        related_terms= set()
        
        for sens in senses: 
                    
            related_term= sens['properties']['fullLemma'].lower() #align all terms in lowercase         
            related_term=self.lemmatizer.lemmatize(related_term)
            related_terms.add(related_term)
            
        return related_terms  

    def save_to_file(list_related_terms, fName):    
        f = open('./Output/AKE-babelnet/'+fName,'w')
        f.write(str(list_related_terms))
        f.close()

    
    def get_relatedTerms(self):
        fNames= glob.glob("./Output/AKE/*.txt")

        # for each document which may contain linked_entities: 
        for file in fNames:
            if os.stat(file).st_size > 0: # skipp empty documents
                linking_df = pd.read_csv(file, header= None, on_bad_lines='skip')    
                
                linked_entities=[x.split('/')[-1] for x in linking_df[0].tolist()]
                
                for entity in linked_entities:             
                    related_terms=self.babelNet_linking(entity)                    

                ## save the output of babelNet linking:         
                save_to_file(related_terms, file.split('/')[-1])
                

