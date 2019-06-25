from itertools import chain
import nltk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn
import pycrfsuite

from until import *

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class chucker():
    
    def word2IOB(self,word):
        text = nltk.word_tokenize(word)
        x = nltk.pos_tag(text)
        modified = [ele + ('X',) for ele in x]
        return modified
        

        
c = chucker()

result = c.word2IOB("i want to see image of package 455646465")
# print(result)

tagger = pycrfsuite.Tagger()
tagger.open('./model/req-infoextract.model')


#############################



def merge(result,predicted):
    listres = []
    for i in range(len(result)):
        listx = list(result[i])
        listx[2] = predicted[i]
        listres.append(tuple(listx))
    return listres






#############################

example_sent = result
# print(example_sent)
print(' '.join(sent2tokens(example_sent)), end='\n\n')

predicted = tagger.tag(sent2features(example_sent))


# print(predicted)

# listres = []
# for i in range(len(result)):
#     listx = list(result[i])
#     listx[2] = predicted[i]
#     listres.append(tuple(listx))
learned = merge(result,predicted)
# print(merge(result,predicted))






print("Predicted:", ' '.join( predicted ))

nltk.chunk.conlltags2tree(learned).draw()
# print("Correct:  ", ' '.join(sent2labels(learned)))
# x = nltk.pos_tag(text)
# print(x)