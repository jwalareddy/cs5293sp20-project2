import numpy as np

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

stopwordsList2 = list(stopwords.words('english'))
lemma = WordNetLemmatizer()    
    

def cleanData(doc):
    #To get all sentances from a paragraph.
    tokenizer = RegexpTokenizer(r'[^.?!]+')   #regex expression to get all sentances. It denotes occurrence of anything except a class containing full stop(.), question mark(?), exclamatory mark(!) and a space.
    sentancesList = tokenizer.tokenize(doc)
    wordsDict = {}
    #To get all words from sentances.
    tokenizer = RegexpTokenizer(r'\w+\'*-*\w+')   #regex expression to get all words. It denotes occurrence of one or more words, then occurrence of ' zero or more times, then occurrence of one or more words.
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
    #print(sentancesList)
    #print(wordsList)
    #print(termDocMatrix)
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
