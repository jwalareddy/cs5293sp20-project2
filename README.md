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
Initially we create a private repository in ouy github accounts using the name cs5293p20-project2. We clone the repository link into our Linux environment by using the following command :
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

## Initial work on the project.
As per the initial data extraction, since we have a lot of files in the pdf_json directory, I created a sub-folder pdf_json1 which contains a subset of these files. 
## Description of the methodology and the functions used :
Initially, I randomly selected random json files from the pdf_json directory and then performed the summarization of those documents in the entire directory. To summarize them, I did the initial text cleaning and a set of other functions implementations. I used the below function where under the "body_text" field, I am extracting the matching values of the "text" field and storing them in a list. 

For reading 10% of the files, I used the following command : instead of specifying the percentage, I mentioned the raw count of 5000.
~~~
count_files = get_glob_files("**/*.json", 5000)
~~~
This command would fetch a given count of 5000 files and that end with the extension .json
~~~
item = glob.glob(os.path.join('C:/Users/jwala/OneDrive/Desktop/pdf_json1', '*.json'))
r = np.random.choice(item, int(len(item)*.1))

def readdata():
    for j, aJson in enumerate(r):
        with open(aJson) as data:
            my_data = json.load(data)
            my_list=[]
            for value in my_data['body_text']:
                my_text= value['text']
                my_list.append(my_text)
                actual_data = '\n'.join(my_list)
            return actual_data
~~~

~~~
def remove_punctuation(sentences):
~~~
This function is used to remove any sort of punctuations in the text document so that all the tex is particularly organized. 
Then I used another function to remove the stop words in the text document.
~~~
def remove_stopwords(sentences):
~~~
Next with another function I calculated the frequency of a particular word and the word count of all the words occuring in the document that I have taken. 
To run my code I used a separate text file j.txt and inputted all the "body_text" values that I obtained from a sample subset of pdf_json directory. I have run all my python files using the same text file for tokenization and summarization.

This is another approach that I used to read the data initially:
~~~
alldicts = []
for file in os.listdir('C:/Users/jwala/OneDrive/Desktop/pdf_json1'):
    full_filename = 'C:/Users/jwala/OneDrive/Desktop/pdf_json1' + "/" + file
    with open(full_filename,'r') as fi:
        dict = json.load(fi)
        alldicts.append(dict)
        
df = pd.DataFrame(alldicts)
df
type(df)
df.head()
df1 = df[['metadata']]
variable = alldicts1.get('metadata', None)
print(variable)
objs = [df1, pd.DataFrame(df['metadata'].tolist()).iloc[:, :6]]
df4 = pd.concat(objs, axis=1).drop('metadata', axis=1)
df5 = df4[['body_text']]
~~~
All these functions are defined in __init__.py. We can run individual functions to see how each output is obtained. I have tried in my Jupyter notebook in the same way and I have aggregated individual functions into one python file.
extra and other approaches for same implementation are defined in other python files.
Individual python functions have also been used to preprocess and remove stop words and prepare the textual data for clustering and summarization.
## Tokenizing
I used the nltk library to tokenize the data. The following library is used for that.
~~~
from nltk import sent_tokenize, word_tokenize
sentences.append(sent_tokenize(sent))
~~~

## Clustering
Once I collected the list, I used the nltk library to tokenize them into individual sentences to be able to do the vectorization. 
Next for Clustering, I used the Tfidf vectorizer to initially represent all the text documents as in vectorized form. Next I built the model using the kmeans clustering with the initial number of clusters as 5. 
After the text summarization we also rank the sentences for which the algorithm basically consists of :
Finding links between sentences by looking for overlapping terminology
Using Google Pagerank on the sentence network to rank sentences in order of importance
I have used multiple approaches for getting the clusters and summarizing them.

## TextRank algorithm summarization used:
Take input file which consists of the text and use sentence tokenizer them to split them into sentences.
Each sentence is considered as a node of our graph. The links between those sentences are the edges that are being used. The edge weight between the sentences is considered as the similarity measure. I also used the wordnet library to obtain the similarity score between the sentences in the text. we find the best score for each of the sentences in the library. Finally we extract the top n sentences and also I used an another approach to specify the length of the summary as 100.
I used the Treebank Word Tokenizer to perform the tokenization. I used the concept of stopword and used it to remove the less important words. I used the concept of POS tagging and the PorterStemmer, SnowballStemmer and gensim package for text summarization. 


Successful execution : 
after summarization , since there are a large number of sentences in each text document, I have extracted a sample of top 50 sentences from 150 sentences that I have considered. Also, I have displayed the similarity score for the sentences as well.
![image](https://user-images.githubusercontent.com/27561736/80410963-01cbf280-8891-11ea-9860-a5eb65f00a14.png)

I have also created another implementation to display the summary and it asks the user to display how many lines of summary that he needs. Below, I have attached the screenshots as well.
![image](https://user-images.githubusercontent.com/27561736/80429024-ce00c500-88b0-11ea-88d3-e896bedc4774.png)

![image](https://user-images.githubusercontent.com/27561736/80429107-f12b7480-88b0-11ea-8e28-198b393849c0.png)

In the first image, it asks for the number of lines of summary to be displayed. After that it shows the sample of documents in that particular cluster that I selected. When I gave the input as 15, in the next image it shows the 15-line summary of the documents in the cluster specified. This is the second implementation that I have used for summmarization of the cluster documents.

## Evaluating the quality of the clustering using the silhouette coefficient
I have run the silhouette coefficient code using the Jupyter notebook, as I wanted to clearly able to distinguish the difference in scores when we keep the changing the number of clusters to fit our document needs.
when i give the number of clusters as 5 : The silhouette coefficient is almost 0.8 which is nearly close to 1.
![image](https://user-images.githubusercontent.com/27561736/80429490-d7d6f800-88b1-11ea-8266-5fe43d4df0a3.png)

## Writing the summaries to the file
I used the below function to write the summaries to the file titled as SUMMARY.md :
~~~
def write_files(summary, key_phrases, filename):
    key_phrase_file = io.open('SUMMARY.md' + filename, 'w')
    for key_phrase in key_phrases:
        key_phrase_file.write(key_phrase + '\n')
    key_phrase_file.close()
    summary_file = io.open('SUMMARY.md/' + filename, 'w')
    summary_file.write(summary)
    summary_file.close()
 ~~~
 
All the summaries of the individual cluster for a document have been written to the SUMMARY.md file. However, only a particular number of sentences for eeach summary would be printed by default, the entire summary is not printed. As attached in the screenshot above, I am able to give the input for the number of lines of summary that I would want for a given document. In the same way, in the SUMMARY.md file I have printed the 10-line summary for each of the cluster documents.

## Creating the Pipfile and the Piplock file for my project:
The Pipfile and the Piplock file which are the constituents of my project's virtual environment are created using the following command :
~~~
pipenv --python python3
pipenv install requests
~~~

This creates a virtual environment and the Pipfile later. For the second command, it initially installs the requests package and then creates the Piplock file successfully.



