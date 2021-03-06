import numpy as np
import itertools
from nltk import PCFG
import operator

class process_NLP():
    def __init__(self):
        # initial language
        self.N = {}                                             # non-terminals
        self.N['e'] = {}                                        # non-terminals entity
        self.N['r'] = {}                                        # non-terminals entity
        self.N['e']['sum'] = 0.0                                # non-terminals entity counter
        self.N['r']['sum'] = 0.0                                # non-terminals entity counter
        self.file = open("/home/omari/Datasets/simulation/grammar.txt", "w")
    #--------------------------------------------------------------------------------------------------------#
    def _build_parser(self, hypotheses, sentence, scene, write):
        self.S = {0:sentence}
        self.scene = scene+1
        self.write = write
        self.hyp_language_pass = {}
        for word in hypotheses['valid_HSV_hyp']:
            self.hyp_language_pass[word] = {'color':[['??',1.0]],'possibilities':1}
            
        if 'valid_dis_hyp' in hypotheses:
            for word in hypotheses['valid_dis_hyp']:
                self.hyp_language_pass[word] = {'distance':[['??',1.0]],'possibilities':1}
                        
        if 'valid_dir_hyp' in hypotheses:
            for word in hypotheses['valid_dir_hyp']:
                self.hyp_language_pass[word] = {'direction':[['??',1.0]],'possibilities':1}
            
        self._update_terminals()
        self._update_nonterminals()
        self._build_PCFG()
        
    #--------------------------------------------------------------------------------------------------------#
    def _update_terminals(self):
        hypotheses = self.hyp_language_pass
        self.grammar = ''
        self.T = {}                                             # terminals
        self.T['features'] = {}
        self.T['sum'] = {}
        for word in hypotheses:
            for feature in hypotheses[word]:
                if feature not in ['possibilities','all']:
                    if feature not in self.T['features']:
                        self.T['features'][feature] = []
                        self.T['sum'][feature] = 0
                    for hyp in hypotheses[word][feature]:
                        self.T['features'][feature].append((word,hyp[1]))
                        self.T['sum'][feature] += hyp[1]
                        
        for feature in self.T['features']:
            l = len(self.T['features'][feature])
            for hyp in self.T['features'][feature]:
                self.grammar += feature+" -> '"+hyp[0]+"' ["+str(hyp[1]/self.T['sum'][feature])+"]"+'\n'
                
    #--------------------------------------------------------------------------------------------------------#
    def _update_nonterminals(self,):
        # there is a threshold in NLTK to drop a hypotheses 9.99500249875e-05 I think it;s 1e-4
    
        entity_features = ['color','shape','location']
        relation_features = ['distance','direction']
        
        def rotate(l,n):
            return l[n:] + l[:n]
            
        def _find_entities(A):
            all_e = []
            e = []
            k_1 = 0
            for k in A:
                if e == []:
                    e.append(k)
                    k_1 = k
                elif k-k_1 == 1:
                    e.append(k)
                    k_1 = k
                else:
                    all_e.append(e)
                    e = [k]
                    k_1 = k
            all_e.append(e)
            return all_e
            
        # loop through all sentences
        features = self.T['features'].keys()
        for s in self.S:
            sentence = self.S[s].split(' ')
            indices = {}
            for feature in features:
                indices[feature] = []
                for hyp in self.T['features'][feature]:
                    A = [i for i, x in enumerate(sentence) if x == hyp[0]]
                    for i in A:
                        indices[feature].append(i)

            # plug in the hypotheses of each word
            parsed_sentence = []
            entity_sentence = []                        #to check connectivity of an entity
            relation_sentence = []                        #to check connectivity of an entity
            for ind,word in enumerate(sentence):
                parsed_sentence.append('_')
                entity_sentence.append(0)
                relation_sentence.append(0)
                for feature in indices:
                    if ind in indices[feature]:
                        parsed_sentence[ind] = feature
                        if feature in entity_features:
                            entity_sentence[ind] = 1
                        if feature in relation_features:
                            relation_sentence[ind] = 1
                            
            # find the number of entity based on connectivity of features in a sentence
            A1 = [i for i, x in enumerate(entity_sentence) if x == 1]
            all_entities = _find_entities(A1)
            
            # find the number of relations based on between objects
            all_relations = []
            for m in range(len(all_entities)-1):
                sent = relation_sentence[all_entities[m][-1]+1:all_entities[m+1][0]]
                A = [i+A1[m]+1 for i, x in enumerate(sent) if x == 1]
                all_relations.append(A)
            #print all_relations
                
                        
            #print sentence
            #print parsed_sentence
            #print self.scene,entity_sentence
                
            # update the non-terminal counter
            for entity in all_entities:
                if entity != []:
                    h = ()
                    for j in entity:
                        h += (parsed_sentence[j],)
                    if h not in self.N['e']:        self.N['e'][h] =  1.0
                    else:        self.N['e'][h] += 1.0
                    self.N['e']['sum'] += 1.0
                    
                    
            # update the non-terminal counter
            for entity in all_relations:
                if entity != []:
                    h = ()
                    for j in entity:
                        if j == '_': continue
                        h += (parsed_sentence[j],)
                    if h not in self.N['r']:        self.N['r'][h] =  1.0
                    else:        self.N['r'][h] += 1.0
                    self.N['r']['sum'] += 1.0
                    
        # add entities, ++ to grammer    
        for feature in self.N:
            sorted_f = sorted(self.N[feature].items(), key=operator.itemgetter(1))
            for l in range(len(sorted_f),0,-1):
                hyp = sorted_f[l-1]
                if hyp[0] != 'sum':
                    val = hyp[1]/self.N[feature]['sum']
                    if val > 1e-4:
                        small_msg = ''
                        if len(hyp[0]) == 1:
                            small_msg += hyp[0][0]
                        else:
                            for j in range(len(hyp[0])-1):
                                small_msg += hyp[0][j]+' '
                            small_msg += hyp[0][j+1]
                        self.grammar += feature+" -> '"+small_msg+"' ["+str(val)+"]"+'\n'
                        
                        
    
    #--------------------------------------------------------------------------------------------------------#
    def _build_PCFG(self):
        if self.grammar != '':
            self.pcfg1 = PCFG.fromstring(self.grammar)
            print self.pcfg1
            if self.write:
                #print self.scene,self.grammar
                self.file.write(str(self.scene))
                self.file.write("\n")
                self.file.write(self.grammar)
            

