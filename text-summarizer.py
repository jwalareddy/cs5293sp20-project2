import numpy as np

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

stopwordsList2 = list(stopwords.words('english'))
lemma = WordNetLemmatizer()    
    

def cleanData(doc):
    tokenizer = RegexpTokenizer(r'[^.?!]+')   
    sentancesList = tokenizer.tokenize(doc)
    wordsDict = {}
    tokenizer = RegexpTokenizer(r'\w+\'*-*\w+') 
    for i in range(len(sentancesList)):
        sentanceWordsList = tokenizer.tokenize(sentancesList[i])
        for j in range(len(sentanceWordsList)):
            word = sentanceWordsList[j]
            word = word.lower()
            word = lemma.lemmatize(word)
            if word in stopwordsList2:
                continue
            
            elif word in wordsDict:
                wordsDict[word].append(i)
            else:
                wordsDict[word] = [i]
    wordsList = list(wordsDict.keys())
    n = len(wordsList)
    m = len(sentancesList)
    termDocMatrix = np.zeros((n,m))
    for i in range(n):
        word = wordsList[i]
        dictList = wordsDict[word]
        for j in range(len(dictList)):
            termDocMatrix[i][dictList[j]] += 1
    return sentancesList, wordsList, termDocMatrix             


from numpy.linalg import svd


def remove_punctuation(sentences):
  sentence_list=[]
  for sent in sentences:
    words=word_tokenize(sent)
    value=""
    for i in range(len(words)):
      a=regex.sub("[^\w\s]|_","",words[i]).strip()
      value=value+" "+a
      value=value.strip()
    sentence_list.append(value)
  return sentence_list


"""

def applySVD(termDocMatrix):
    U, S, Vt = svd(termDocMatrix, full_matrices=False)
    return U, S, Vt
"""

import operator
import math

"""
def summarizer(doc=None, k=4):
    sentancesList, wordsList, termDocMatrix = cleanData(doc)
    #print(sentancesList)
    #print(wordsList)
    #print(termDocMatrix)
    U, S, Vt = applySVD(termDocMatrix)
    #print(U)
    #print(S)
    #print(Vt)
    l = S.size
    n, m = Vt.shape
    #l is equal to n which is number of dimensions in reduced space.
    #m is number of sentances.
    scoreDict = {}
    for i in range(m):
        score = 0
        for j in range(l):
            score += S[j]*S[j]*Vt[j,i]*Vt[j,i]      
        score = math.sqrt(score)
        #score contains the square of the magnitude of the sentance vector.
        scoreDict[i] = score
    summarySentancesList = []
    ctr = k
    sortedDictList = sorted(scoreDict.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in sortedDictList:
        summarySentancesList.append(key)
        ctr -= 1
        if ctr==0:
            break
    summarySentancesList.sort()
    summary = ''
    for i in range(len(summarySentancesList)):
        summary += sentancesList[summarySentancesList[i]]
        summary += '.'
        summary += '\n'
    return summary
"""
"""
def cluster_texts(texts, clusters=3):
    Transform texts to Tf-Idf coordinates and cluster texts using K-Means
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
    clustering = collections.defaultdict(list)
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)
    return clustering
clusters = cluster_texts(sentences)
#print(dict(clusters))
print(clusters)
def extract_sentences(text, summary_length=100, language='english'):
    sentence_detector = nltk.data.load('tokenizers/punkt/'+language+'.pickle')
    sentence_tokens = sentence_detector.tokenize(text.strip())
    graph = build_graph(sentence_tokens)
    calculated_page_rank = nx.pagerank(graph, weight='weight')
    sentences = sorted(calculated_page_rank, key=calculated_page_rank.get,
                       reverse=True)
    # I specified the length of the summary to be 100, but we can arbitarily change it
    summary = ' '.join(sentences)
    summary_words = summary.split()
    summary_words = summary_words[0:summary_length]
    dot_indices = [idx for idx, word in enumerate(summary_words) if word.find('.') != -1]
    if dot_indices:
        last_dot = max(dot_indices) + 1
        summary = ' '.join(summary_words[0:last_dot])
    else:
        summary = ' '.join(summary_words)
    return summary
"""

from pathlib import Path
import os


if __name__ == "__main__":
    file = open('j.txt',"r")
    #file1 = file.remove_punctuation(file)
    filedata = file.read()
    filedataList = filedata.split("\n")
    sample = ""
    for i in range(len(filedataList)):
        sample += filedataList[i]
        file.close()
        n = int(input("Enter number of lines in summary: "))
        print("Sample :")
        print(sample+"\n")
        print("Summary:")
        summary = summarizer(doc=sample, k=n)
        print(summary)
        print("\n\n")
