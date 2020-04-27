# cs5293sp20-project2
The Summarizer
## Introduction
Millions of documents are push onto the Internet every year. Hundreds of thousands of those documents are academic documents that may be meaningful. Unfortunately, no human is able to wade through the gruff to reach the meaningful documents. Most scientist only look at documents that are published at “prestigious” journals and conferences. In this project, you are going to exercise what you have learned so far in class to help scientists and interested citizes get a lay of the land when it comes to publlished academic work.
## Implementation
The work done is summarized below as follows : 
1. Select a subset of academic documents.
2. Tokenize and cluster the documents.
3. Summarize each cluster.
## Setting up the initial installations
We run the following installations in the project's virtual environment. Even if the installations are done in the Python environment, in the project's virtual environment, there might be an error popping up "no module named nltk"
~~~
pipenv install nltk
pipenv install re
pipenv install CommonRegex
pipenv install numpy
~~~
## Platform used :
I used Google Cloud Platform to create a VM instance in the cloud. I used it for cloning the Git repository, and made changes using the following github actions.

## Git Repository commands :
Initially we create a private repository in ouy github accounts using the name cs5293p20-project1. We clone the repository link into our Linux environment by using the following command :
~~~
https://github.com/jwalareddy/cs5293sp20-project2.git
~~~
Further changes made to the directory structure are committed to github using the following commands :
~~~
git add -A
git commit -m " appropriate message to be displayed if it is the initial commit or the final commit"
git push origin master 
git pull origin master
~~~
If any errors occur while pushing the data from the linux environment to the github repository, we can use 
~~~
git push origin master --force
~~~
to pull the changes, if any, made from the github repository to our local environment, we use the following command :
~~~
git pull origin master
~~~
## Description of the methodology and the functions used :
Initially, I randomly selected 20 json files from the pdf_json directory and then performed the summarization of those documents in the entire directory. To summarize them, I did the initial text cleaning and a set of other functions implementations. I used the function 
~~~
def remove_punctuation(sentences):
~~~
This function is used to remove any sort of punctuations in the text document so that all the tex is particularly organized. 
Then I used another function to remove the stop words in the text document.
~~~
def remove_stopwords(sentences):
~~~
Next with another function I calculated the frequency of a particular word and the word count of all the words occuring in the document that I have taken. 

## CLustering
Next for Clustering, I used the Tfidf vectorizer to initially represent all the text documents as in vectorized form. Next I built the model using the kmeans clustering with the initial number of clusters as 5. 
After the text summarization we also rank the sentences for which the algorithm basically consists of :
Finding links between sentences by looking for overlapping terminology
Using Google Pagerank on the sentence network to rank sentences in order of importance

## TextRank algorithm summarization used:
* Take input file which consists of the text and use sentence tokenizer them to split them into sentences.
Each sentence is considered as a node of our graph. The links between those sentences are the edges that are being used. The edge weight between the sentences is considered as the similarity measure. I also used the wordnet library to obtain the similarity score between the sentences in the text. we find the best score for each of the sentences in the library. Finally we extract the top n sentences and also I used an another approach to specify the length of the summary as 100.
I used the Treebank Word Tokenizer to perform the tokenization. I used the concept of stopword and used it to remove the less important words. I used the concept of POS tagging and the PorterStemmer for text summarization. 


Successful execution : 
![image](https://user-images.githubusercontent.com/27561736/80410963-01cbf280-8891-11ea-9860-a5eb65f00a14.png)



















## References
https://arxiv.org/pdf/1602.03606.pdf

