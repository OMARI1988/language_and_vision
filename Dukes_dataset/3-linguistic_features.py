import numpy as np
import math as m
from xml_functions import *
from nltk.tree import *
from nltk.tree import ParentedTree
import pickle
import getpass
#--------------------------------------------------------------------------------------------------------#

def _read_stop_wrods():
    pkl_file = '/home/mo/Datasets/11-Leeds/Dukes_modified/learning/idf_FW_linguistic_features.p'
    data = open(pkl_file, 'rb')
    stop = pickle.load(data)
    return stop

def _read_pickle(scene):
    pkl_file = '/home/mo/Datasets/11-Leeds/Dukes_modified/scenes/'+str(scene)+'_sentences.p'
    data = open(pkl_file, 'rb')
    sentences = pickle.load(data)
    return sentences


def _find_n_grams(sentence):
    n_word = 3 ## length of n_grams
    w = sentence.split(' ')
    n_grams = []
    for i in range(len(w)):
        # if w[i]not in self.words[s]: self.words[s].append(w[i])
        for j in range(i+1,np.min([i+1+n_word,len(w)+1])):
            n_grams.append(' '.join(w[i:j]))
    return n_grams

def _get_n_grams(sentences,stop):
    all_n_grams = []
    for id in sentences:
        n = _find_n_grams(sentences[id]['text'])
        for i in n:
            ok = 1
            for stop_word in stop:
                if stop_word == i or ' '+stop_word in i or stop_word+' ' in i:
                    ok = 0
            if ok:
                if i not in all_n_grams:
                    all_n_grams.append(i)
    return all_n_grams

stop = _read_stop_wrods()
for scene in range(1,1001):
    print 'extracting feature from scene : ',scene
    pkl_file = '/home/mo/Datasets/11-Leeds/Dukes_modified/learning/'+str(scene)+'_linguistic_features.p'
    LF = {}
    sentences = _read_pickle(scene)
    LF['n_grams'] = _get_n_grams(sentences,stop)
    # print LF['n_grams']
    pickle.dump(LF, open(pkl_file, 'wb'))
    file1 = '/home/mo/Datasets/11-Leeds/Dukes_modified/learning/'+str(scene)+'_linguistic_feature.txt'
    F = open(file1, 'w')
    for n in LF['n_grams']:
        F.write(n+'\n')
    F.close()
