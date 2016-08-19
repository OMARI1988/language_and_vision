import numpy as np
import math as m
from xml_functions import *
from nltk.tree import *
from nltk.tree import ParentedTree
import pickle
import getpass
import operator
import itertools
from copy import deepcopy
#--------------------------------------------------------------------------------------------------------#

def _read_tags():
    pkl_file = '/home/'+getpass.getuser()+'/Datasets_old/Dukes_modified/learning/tags.p'
    data = open(pkl_file, 'rb')
    hypotheses_tags, VF_dict, LF_dict = pickle.load(data)
    return [hypotheses_tags, VF_dict, LF_dict]

def _read_sentences(scene):
    pkl_file = '/home/'+getpass.getuser()+'/Datasets_old/Dukes_modified/scenes/'+str(scene)+'_sentences.p'
    data = open(pkl_file, 'rb')
    sentences = pickle.load(data)
    return sentences

def _read_vf(scene):
    pkl_file = '/home/'+getpass.getuser()+'/Datasets_old/Dukes_modified/learning/'+str(scene)+'_visual_features.p'
    data = open(pkl_file, 'rb')
    vf,tree = pickle.load(data)
    return vf,tree

def _read_grammar_trees(scene):
    pkl_file = '/home/'+getpass.getuser()+'/Datasets_old/Dukes_modified/learning/'+str(scene)+'_grammar.p'
    data = open(pkl_file, 'rb')
    tree = pickle.load(data)
    return tree

def _test_Actions(element):
    action_flag = 1
    action_position = []
    for count,item in enumerate(element):
        if 'actions_' in item:
            action_position.append(count)
    if len(action_position) == 0:
        action_flag = 0
        # print 'test1'
    elif len(action_position) > 1:
        L = [a_i - b_i for a_i, b_i in zip(action_position[:-1],action_position[1:])]
        for i in L:
            if i!= -1:
                action_flag=0
                # print 'test2'
                # print action_position
    # if action_flag:
    #     print element
    return action_flag

#--------------------------------------------------------------------------------------------------------#
# this function tests one susbet of words at a time
def _all_possibilities_func(subset, hyp_language_pass):
    all_possibilities = []      # all the possibilities gathered in one list
    for word in subset:
        all_possibilities.append(hyp_language_pass[word].keys())
    return all_possibilities

def _get_semantics(tree, hypotheses_tags):
    words = []
    for i in range(len(tree)):
        for word in tree[i]:
            words.append(word)
    semantic_trees = {}
    all_possibilities = _all_possibilities_func(words, hypotheses_tags)
    for count,element in enumerate(itertools.product(*all_possibilities)):
        valid = _test_Actions(element)
        if valid:
            semantic_trees[count] = deepcopy(tree)
            c = 0
            for i in range(len(semantic_trees[count])):
                for j in range(len(semantic_trees[count][i])):
                    semantic_trees[count][i][j] = element[c]
                    c += 1
            # print semantic_trees[count]
    return semantic_trees

hypotheses_tags, VF_dict, LF_dict = _read_tags()
for scene in range(1,1001):
    semantic_trees = {}
    print 'generating grammar from scene : ',scene
    VF,Tree = _read_vf(scene)
    sentences = _read_sentences(scene)
    grammar_trees = _read_grammar_trees(scene)
    counter = 0
    for id in sentences:
        # print '###############################################################'
        # print sentences[id]['text']
        # print '###############################################################'
        semantic_trees[id] = {}
        for t in grammar_trees[id]:
            tree = grammar_trees[id][t]
            semantic_trees[id][t] = _get_semantics(tree,hypotheses_tags)
            counter += len(semantic_trees[id][t])
    pkl_file = '/home/'+getpass.getuser()+'/Datasets_old/Dukes_modified/learning/'+str(scene)+'_semantic_grammar.p'
    pickle.dump(semantic_trees, open(pkl_file, 'wb'))
