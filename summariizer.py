import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

fp = open("sample.txt", "r")  ##To see another sample output change filename to sample2.txt
if fp.mode == "r":
    text = fp.read()

stopwords1 = nltk.corpus.stopwords.words('english')
wordscores = dict()
words = word_tokenize(text)
for word in words:
    word = word.lower()
    if word in stopwords1:
        continue
    if word in wordscores:
        wordscores[word] += 1
    if word not in wordscores:
        wordscores[word] = 1

maximum_frequncy = max(wordscores.values())

for word in wordscores.keys():
    wordscores[word] = (wordscores[word] / maximum_frequncy)

sentence_list = sent_tokenize(text)
sentscores = dict()
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in wordscores.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentscores.keys():
                    sentscores[sent] = wordscores[word]
                else:
                    sentscores[sent] += wordscores[word]

summary = heapq.nlargest(2, sentscores, key=sentscores.get)
##To get more summarized sentences change the value from 2 to required value


final_summary = ''.join(summary)
print(final_summary)
print("The Length of summarized text:", len(final_summary))  ##Length of string
