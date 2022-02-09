# Uni_Webapp
 
The data consists of two files:
* disease_evidence.tsv - list of disease identified 
    * diseaseid: id of the disease
    * sentence: sentences for the given disease found in literature 
    * nsentence: the number of sentences in the sentence field
    * pmid: the PubMed id of the article
    * disease_name: name of the disease
    * disease_type: Enumaration that define the disease type defined by DisGeNET
* gene_evidence.tsv - list of genes identified
    * geneid: the NCBI Entrez Gene Identifier
    * sentence: sentences for the evidence of a given gene found in literature 
    * nsentence: the number of sentences in the sentence field
    * pmid: the PubMed id of the article
    * gene_symbol: symbol of the gene
    * organism: organism in which the gene was found

The program is divide into three parts:
* Model: Defines the model and the operations that can be applied to it
* Datasets: Defines the differences between the two datasets by using different default arguments
* Controller: Handles both datasets and the web application
