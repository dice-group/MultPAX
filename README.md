# MultPAX: Keyphrase Extraction using Language Models and Knowledge Graphs
This repositoy contains the source code of paper: *"MultPAX: Keyphrase Extraction using Language models and Knowledge Graphs"*. The paper is currently under-review at the ISWC 2022 conference. 


<p align="center">
<img src="data/MltPAX.jpg" width="500" height="300">
</p>
<p align="center">Fig. 1 Architecure of MltPAX Framework</p>


### Summary: 
- Keyphrase extraction is the process of extracting a small set of phrases that best describe an input corpus. 
- The automatic generation of keyphrases has become essential for many natural language applications such as text categorization, indexing, and summarization. 
- In this paper, we propose MultPAX, a multitask framework for extracting *present* and *absent* keyphrases using pretrained language models and knowledge graphs. In particular, our framework contains three components: 
    1) MultPAX identifies present keyphrases from the input corpus.
    2) MultPAX then links the input corpus with external knowledge graphs to get more relevant phrases.
    3) MultPAX ranks the extracted phrases based on their semantic relatedness to input corpus.

### Our Contributions:
```
1) We propose an *unsupervised* multitask framework that not only extracts present keyphrases, but also generate absent ones.
    
2) To the best of our knowledge, our approach is the first attempt that leverages existing knowledge graphs for keyphrase extraction without the need to create keyphrase vocabularies or phrase banks.
    
3) We introduce an embedding-based F1 score that considers semantic similarity between generated and ground-truth keyphrases rather than the existing exact-matching. 
    
4) We carried out several experiments on four benchmark datasets. The evaluation results showed that our approach proved to be more accurate compared with state-of-the-art baselines.  
```    
---
## How to run: 
We conduct several experiments on four benchmark datasets, namely: *Inspec, SemEval2010, NUS and Krapivin2009*. The datasets are available at the [Dropbox Folder](https://www.dropbox.com/s/aluvkblymjs7i3r/MULTPAX-Datasets.zip?dl=0). 

To setup the experiments, you need to install the following libraries via `pip install -r requirments.txt` or install them manually: 
```
Python 3.7
keybert
sentence-transformers 2.2.0
SPARQLWrapper 2.0.0
SciPy 1.8.0
NumPy 1.21.5
Pandas 1.4.2
NLTK 3.6.6 
requests 2.27.1
py-babelnet
```

We provide our experiements as Jupyter notebooks (`see Experiments Folder`) and source files (`see src Folder`). We recommend using Jupyter notebooks for an interactive execution of our experiments. Furhtermore, we provide a Jupyter notebook for each experiments:
- [MultPAX-Inspec](Experiments/MltPAX-Inspec.ipynb) 
- MultPAX-SemEval 
- MultPAX-NUS 
- MultPAX-Krapivin2009  

---
## Citation
TBD
