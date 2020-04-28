import requests
import editdistance
import io
import itertools
import networkx as nx
import nltk
import os
from nltk.tokenize import sent_tokenize,word_tokenize
import regex
import string

def setup_environment():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    print('Completed resource downloads.')

#This is the sample function that i used to initially read a set of 40 json files and extract the summaries from them
"""
with open('C:/Users/jwala/OneDrive/Desktop/pdf_json/0b05d3ede3351f8b3edb22c74b0cfe933ba408c1.json') as json_data:
    data = json.load(json_data)
#print(data)
#type(data)
#print(data.items())
data_list=list(data.values())
#print(data_list.split(","))
type(data_list)

def extract_values(obj, key):
   
    arr = []

    def extract(obj, arr, key):
       
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

names = extract_values(data,'text')
print(names)
type(names)
"""

#another dictionary approach to list  them into a dataframe. from the metadata field, I am extracting the abstract and thee text field

"""
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
def remove_punctuation(sentences) :
  sentences = sent_tokenize(sentences):
  sentence_list=[]
  for sent in sentences:
    words=word_tokenize(sent)
    value=""
  #  for i in range(len(words)):
     # a=regex.sub("[^\w\s]|_","",words[i]).strip()
     # value=value+" "+a
     # value=value.strip()
   # sentence_list.append(value)
 # return sentence_list
"""
  
def build_graph(nodes):
    g1 = nx.Graph()  # initialize an undirected graph
    g1.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = editdistance.eval(firstString, secondString)
        g1.add_edge(firstString, secondString, weight=levDistance)

    return g1
def remove_stopwords(sentences):
  stop_words=set(stopwords.words("english"))
   
  sentence_list=[]
  for sent in sentences:
    words=word_tokenize(sent)
    words=[word for word in words if word not in stop_words]
    words=" ".join(words)
    words=words.strip()
    sentence_list.append(words)
  return sentence_list

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

#Writing the summaries obtained to SUMMARY.md file
def write_files(summary, key_phrases, filename):
    key_phrase_file = io.open('SUMMARY.md' + filename, 'w')
    for key_phrase in key_phrases:
        key_phrase_file.write(key_phrase + '\n')
    key_phrase_file.close()
    summary_file = io.open('SUMMARY.md/' + filename, 'w')
    summary_file.write(summary)
    summary_file.close()


def summarize_all():
    # retrieve each of the articles
    articles = os.listdir("text")
    for article in text:
        article_file = io.open('text/' + article, 'r')
        text = article_file.read()
        keyphrases = extract_key_phrases(text)
        summary = extract_sentences(text)
        write_files(summary, keyphrases, article)
