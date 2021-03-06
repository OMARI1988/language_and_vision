#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import cPickle as pickle
import math
import numpy as np
import getpass
import pdb
import random
from sklearn import metrics, svm


def segmented_videos():
    d ={

    '2016-04-05' : [('2016-04-05', 'vid437'), ('2016-04-05', 'vid400'), ('2016-04-05', 'vid465'), ('2016-04-05', 'vid486'), ('2016-04-05', 'vid376'), ('2016-04-05', 'vid441'), ('2016-04-05', 'vid458'), ('2016-04-05', 'vid374'), ('2016-04-05', 'vid481'), ('2016-04-05', 'vid489'), ('2016-04-05', 'vid365'), ('2016-04-05', 'vid429'), ('2016-04-05', 'vid451'), ('2016-04-05', 'vid454'), ('2016-04-05', 'vid436'), ('2016-04-05', 'vid361'), ('2016-04-05', 'vid351'), ('2016-04-05', 'vid372'), ('2016-04-05', 'vid446'), ('2016-04-05', 'vid388'), ('2016-04-05', 'vid392'), ('2016-04-05', 'vid466'), ('2016-04-05', 'vid409'), ('2016-04-05', 'vid460'), ('2016-04-05', 'vid358'), ('2016-04-05', 'vid453'), ('2016-04-05', 'vid359'), ('2016-04-05', 'vid382'), ('2016-04-05', 'vid490'), ('2016-04-05', 'vid364'), ('2016-04-05', 'vid395'), ('2016-04-05', 'vid352'), ('2016-04-05', 'vid350'), ('2016-04-05', 'vid484'), ('2016-04-05', 'vid394'), ('2016-04-05', 'vid348'), ('2016-04-05', 'vid399'), ('2016-04-05', 'vid405'), ('2016-04-05', 'vid450'), ('2016-04-05', 'vid448'), ('2016-04-05', 'vid416'), ('2016-04-05', 'vid487'), ('2016-04-05', 'vid411'), ('2016-04-05', 'vid387'), ('2016-04-05', 'vid360'), ('2016-04-05', 'vid421'), ('2016-04-05', 'vid383'), ('2016-04-05', 'vid424'), ('2016-04-05', 'vid377'), ('2016-04-05', 'vid455'), ('2016-04-05', 'vid483'), ('2016-04-05', 'vid369'), ('2016-04-05', 'vid438'), ('2016-04-05', 'vid461'), ('2016-04-05', 'vid386'), ('2016-04-05', 'vid468'), ('2016-04-05', 'vid356'), ('2016-04-05', 'vid434'), ('2016-04-05', 'vid493'), ('2016-04-05', 'vid403'), ('2016-04-05', 'vid469'), ('2016-04-05', 'vid473'), ('2016-04-05', 'vid433'), ('2016-04-05', 'vid425'), ('2016-04-05', 'vid449'), ('2016-04-05', 'vid459'), ('2016-04-05', 'vid378'), ('2016-04-05', 'vid389'), ('2016-04-05', 'vid367'), ('2016-04-05', 'vid479'), ('2016-04-05', 'vid485'), ('2016-04-05', 'vid474'), ('2016-04-05', 'vid406'), ('2016-04-05', 'vid456'), ('2016-04-05', 'vid491'), ('2016-04-05', 'vid475'), ('2016-04-05', 'vid431'), ('2016-04-05', 'vid432'), ('2016-04-05', 'vid375'), ('2016-04-05', 'vid444'), ('2016-04-05', 'vid428'), ('2016-04-05', 'vid357'), ('2016-04-05', 'vid355'), ('2016-04-05', 'vid480'), ('2016-04-05', 'vid419'), ('2016-04-05', 'vid368'), ('2016-04-05', 'vid371'), ('2016-04-05', 'vid380'), ('2016-04-05', 'vid488'), ('2016-04-05', 'vid393'), ('2016-04-05', 'vid353'), ('2016-04-05', 'vid442'), ('2016-04-05', 'vid467'), ('2016-04-05', 'vid443'), ('2016-04-05', 'vid362'), ('2016-04-05', 'vid423'), ('2016-04-05', 'vid422'), ('2016-04-05', 'vid391'), ('2016-04-05', 'vid463'), ('2016-04-05', 'vid381'), ('2016-04-05', 'vid404'), ('2016-04-05', 'vid476'), ('2016-04-05', 'vid435'), ('2016-04-05', 'vid396'), ('2016-04-05', 'vid349'), ('2016-04-05', 'vid397'), ('2016-04-05', 'vid401'), ('2016-04-05', 'vid402'), ('2016-04-05', 'vid430'), ('2016-04-05', 'vid390'), ('2016-04-05', 'vid370'), ('2016-04-05', 'vid412'), ('2016-04-05', 'vid385'), ('2016-04-05', 'vid439'), ('2016-04-05', 'vid410'), ('2016-04-05', 'vid464'), ('2016-04-05', 'vid363'), ('2016-04-05', 'vid470'), ('2016-04-05', 'vid354'), ('2016-04-05', 'vid417'), ('2016-04-05', 'vid452'), ('2016-04-05', 'vid472'), ('2016-04-05', 'vid440'), ('2016-04-05', 'vid482'), ('2016-04-05', 'vid478'), ('2016-04-05', 'vid447'), ('2016-04-05', 'vid477'), ('2016-04-05', 'vid413'), ('2016-04-05', 'vid379'), ('2016-04-05', 'vid445'), ('2016-04-05', 'vid492'), ('2016-04-05', 'vid366'), ('2016-04-05', 'vid427'), ('2016-04-05', 'vid420'), ('2016-04-05', 'vid414'), ('2016-04-05', 'vid426'), ('2016-04-05', 'vid407'), ('2016-04-05', 'vid415'), ('2016-04-05', 'vid398'), ('2016-04-05', 'vid471'), ('2016-04-05', 'vid457'), ('2016-04-05', 'vid384'), ('2016-04-05', 'vid373'), ('2016-04-05', 'vid462'), ('2016-04-05', 'vid418'), ('2016-04-05', 'vid408')]
    ,
    '2016-04-06': [('2016-04-06', 'vid144'), ('2016-04-06', 'vid222'), ('2016-04-06', 'vid200'), ('2016-04-06', 'vid195'), ('2016-04-06', 'vid159'), ('2016-04-06', 'vid187'), ('2016-04-06', 'vid296'), ('2016-04-06', 'vid314'), ('2016-04-06', 'vid287'), ('2016-04-06', 'vid148'), ('2016-04-06', 'vid157'), ('2016-04-06', 'vid295'), ('2016-04-06', 'vid267'), ('2016-04-06', 'vid264'), ('2016-04-06', 'vid280'), ('2016-04-06', 'vid209'), ('2016-04-06', 'vid176'), ('2016-04-06', 'vid217'), ('2016-04-06', 'vid204'), ('2016-04-06', 'vid259'), ('2016-04-06', 'vid163'), ('2016-04-06', 'vid224'), ('2016-04-06', 'vid291'), ('2016-04-06', 'vid154'), ('2016-04-06', 'vid271'), ('2016-04-06', 'vid262'), ('2016-04-06', 'vid290'), ('2016-04-06', 'vid219'), ('2016-04-06', 'vid218'), ('2016-04-06', 'vid220'), ('2016-04-06', 'vid183'), ('2016-04-06', 'vid306'), ('2016-04-06', 'vid164'), ('2016-04-06', 'vid266'), ('2016-04-06', 'vid190'), ('2016-04-06', 'vid155'), ('2016-04-06', 'vid215'), ('2016-04-06', 'vid244'), ('2016-04-06', 'vid173'), ('2016-04-06', 'vid225'), ('2016-04-06', 'vid208'), ('2016-04-06', 'vid250'), ('2016-04-06', 'vid221'), ('2016-04-06', 'vid234'), ('2016-04-06', 'vid308'), ('2016-04-06', 'vid203'), ('2016-04-06', 'vid298'), ('2016-04-06', 'vid238'), ('2016-04-06', 'vid286'), ('2016-04-06', 'vid210'), ('2016-04-06', 'vid312'), ('2016-04-06', 'vid196'), ('2016-04-06', 'vid282'), ('2016-04-06', 'vid153'), ('2016-04-06', 'vid226'), ('2016-04-06', 'vid309'), ('2016-04-06', 'vid161'), ('2016-04-06', 'vid269'), ('2016-04-06', 'vid142'), ('2016-04-06', 'vid301'), ('2016-04-06', 'vid245'), ('2016-04-06', 'vid231'), ('2016-04-06', 'vid145'), ('2016-04-06', 'vid303'), ('2016-04-06', 'vid168'), ('2016-04-06', 'vid316'), ('2016-04-06', 'vid275'), ('2016-04-06', 'vid198'), ('2016-04-06', 'vid311'), ('2016-04-06', 'vid281'), ('2016-04-06', 'vid305'), ('2016-04-06', 'vid283'), ('2016-04-06', 'vid292'), ('2016-04-06', 'vid184'), ('2016-04-06', 'vid294'), ('2016-04-06', 'vid270'), ('2016-04-06', 'vid233'), ('2016-04-06', 'vid297'), ('2016-04-06', 'vid169'), ('2016-04-06', 'vid160'), ('2016-04-06', 'vid194'), ('2016-04-06', 'vid273'), ('2016-04-06', 'vid201'), ('2016-04-06', 'vid230'), ('2016-04-06', 'vid258'), ('2016-04-06', 'vid223'), ('2016-04-06', 'vid172'), ('2016-04-06', 'vid152'), ('2016-04-06', 'vid213'), ('2016-04-06', 'vid178'), ('2016-04-06', 'vid285'), ('2016-04-06', 'vid175'), ('2016-04-06', 'vid261'), ('2016-04-06', 'vid242'), ('2016-04-06', 'vid186'), ('2016-04-06', 'vid313'), ('2016-04-06', 'vid207'), ('2016-04-06', 'vid263'), ('2016-04-06', 'vid177'), ('2016-04-06', 'vid255'), ('2016-04-06', 'vid307'), ('2016-04-06', 'vid151'), ('2016-04-06', 'vid284'), ('2016-04-06', 'vid293'), ('2016-04-06', 'vid254'), ('2016-04-06', 'vid146'), ('2016-04-06', 'vid214'), ('2016-04-06', 'vid150'), ('2016-04-06', 'vid278'), ('2016-04-06', 'vid276'), ('2016-04-06', 'vid227'), ('2016-04-06', 'vid256'), ('2016-04-06', 'vid253'), ('2016-04-06', 'vid197'), ('2016-04-06', 'vid147'), ('2016-04-06', 'vid162'), ('2016-04-06', 'vid188'), ('2016-04-06', 'vid211'), ('2016-04-06', 'vid182'), ('2016-04-06', 'vid180'), ('2016-04-06', 'vid199'), ('2016-04-06', 'vid149'), ('2016-04-06', 'vid299'), ('2016-04-06', 'vid212'), ('2016-04-06', 'vid165'), ('2016-04-06', 'vid310'), ('2016-04-06', 'vid277'), ('2016-04-06', 'vid191'), ('2016-04-06', 'vid265'), ('2016-04-06', 'vid170'), ('2016-04-06', 'vid143'), ('2016-04-06', 'vid240'), ('2016-04-06', 'vid171'), ('2016-04-06', 'vid304'), ('2016-04-06', 'vid237'), ('2016-04-06', 'vid236'), ('2016-04-06', 'vid257'), ('2016-04-06', 'vid174'), ('2016-04-06', 'vid232'), ('2016-04-06', 'vid205'), ('2016-04-06', 'vid179'), ('2016-04-06', 'vid268'), ('2016-04-06', 'vid206'), ('2016-04-06', 'vid248'), ('2016-04-06', 'vid252'), ('2016-04-06', 'vid249'), ('2016-04-06', 'vid243'), ('2016-04-06', 'vid166'), ('2016-04-06', 'vid202'), ('2016-04-06', 'vid279'), ('2016-04-06', 'vid288'), ('2016-04-06', 'vid192'), ('2016-04-06', 'vid193'), ('2016-04-06', 'vid228'), ('2016-04-06', 'vid247'), ('2016-04-06', 'vid246'), ('2016-04-06', 'vid239'), ('2016-04-06', 'vid181'), ('2016-04-06', 'vid241'), ('2016-04-06', 'vid289'), ('2016-04-06', 'vid272'), ('2016-04-06', 'vid251'), ('2016-04-06', 'vid229'), ('2016-04-06', 'vid156'), ('2016-04-06', 'vid235'), ('2016-04-06', 'vid189'), ('2016-04-06', 'vid158'), ('2016-04-06', 'vid260'), ('2016-04-06', 'vid315'), ('2016-04-06', 'vid167'), ('2016-04-06', 'vid216'), ('2016-04-06', 'vid274'), ('2016-04-06', 'vid185'), ('2016-04-06', 'vid300'), ('2016-04-06', 'vid302')]
    ,
    '2016-04-07': [('2016-04-07', 'vid15'), ('2016-04-07', 'vid33'), ('2016-04-07', 'vid19'), ('2016-04-07', 'vid11'), ('2016-04-07', 'vid24'), ('2016-04-07', 'vid9'), ('2016-04-07', 'vid21'), ('2016-04-07', 'vid5'), ('2016-04-07', 'vid14'), ('2016-04-07', 'vid7'), ('2016-04-07', 'vid26'), ('2016-04-07', 'vid16'), ('2016-04-07', 'vid13'), ('2016-04-07', 'vid28'), ('2016-04-07', 'vid36'), ('2016-04-07', 'vid3'), ('2016-04-07', 'vid35'), ('2016-04-07', 'vid22'), ('2016-04-07', 'vid2'), ('2016-04-07', 'vid18'), ('2016-04-07', 'vid30'), ('2016-04-07', 'vid12'), ('2016-04-07', 'vid34'), ('2016-04-07', 'vid4'), ('2016-04-07', 'vid25'), ('2016-04-07', 'vid27'), ('2016-04-07', 'vid8'), ('2016-04-07', 'vid23'), ('2016-04-07', 'vid1'), ('2016-04-07', 'vid32'), ('2016-04-07', 'vid20'), ('2016-04-07', 'vid29'), ('2016-04-07', 'vid6'), ('2016-04-07', 'vid17'), ('2016-04-07', 'vid31'), ('2016-04-07', 'vid10')]
    ,
    '2016-04-08':[ ('2016-04-08', 'vid318'), ('2016-04-08', 'vid345'), ('2016-04-08', 'vid333'), ('2016-04-08', 'vid335'), ('2016-04-08', 'vid338'), ('2016-04-08', 'vid319'), ('2016-04-08', 'vid321'), ('2016-04-08', 'vid326'), ('2016-04-08', 'vid342'), ('2016-04-08', 'vid322'), ('2016-04-08', 'vid334'), ('2016-04-08', 'vid317'), ('2016-04-08', 'vid329'), ('2016-04-08', 'vid343'), ('2016-04-08', 'vid336'), ('2016-04-08', 'vid325'), ('2016-04-08', 'vid331'), ('2016-04-08', 'vid337'), ('2016-04-08', 'vid324'), ('2016-04-08', 'vid320'), ('2016-04-08', 'vid340'), ('2016-04-08', 'vid323'), ('2016-04-08', 'vid347'), ('2016-04-08', 'vid332'), ('2016-04-08', 'vid328'), ('2016-04-08', 'vid327'), ('2016-04-08', 'vid330'), ('2016-04-08', 'vid341'), ('2016-04-08', 'vid344'), ('2016-04-08', 'vid346'), ('2016-04-08', 'vid339')]
    ,
    '2016-04-11':[ ('2016-04-11', 'vid68'), ('2016-04-11', 'vid51'), ('2016-04-11', 'vid114'), ('2016-04-11', 'vid103'), ('2016-04-11', 'vid123'), ('2016-04-11', 'vid131'), ('2016-04-11', 'vid83'), ('2016-04-11', 'vid100'), ('2016-04-11', 'vid87'), ('2016-04-11', 'vid109'), ('2016-04-11', 'vid62'), ('2016-04-11', 'vid91'), ('2016-04-11', 'vid49'), ('2016-04-11', 'vid55'), ('2016-04-11', 'vid129'), ('2016-04-11', 'vid115'), ('2016-04-11', 'vid82'), ('2016-04-11', 'vid64'), ('2016-04-11', 'vid96'), ('2016-04-11', 'vid77'), ('2016-04-11', 'vid107'), ('2016-04-11', 'vid38'), ('2016-04-11', 'vid71'), ('2016-04-11', 'vid90'), ('2016-04-11', 'vid125'), ('2016-04-11', 'vid88'), ('2016-04-11', 'vid127'), ('2016-04-11', 'vid58'), ('2016-04-11', 'vid133'), ('2016-04-11', 'vid139'), ('2016-04-11', 'vid69'), ('2016-04-11', 'vid97'), ('2016-04-11', 'vid93'), ('2016-04-11', 'vid92'), ('2016-04-11', 'vid116'), ('2016-04-11', 'vid67'), ('2016-04-11', 'vid95'), ('2016-04-11', 'vid104'), ('2016-04-11', 'vid66'), ('2016-04-11', 'vid86'), ('2016-04-11', 'vid40'), ('2016-04-11', 'vid126'), ('2016-04-11', 'vid48'), ('2016-04-11', 'vid120'), ('2016-04-11', 'vid72'), ('2016-04-11', 'vid105'), ('2016-04-11', 'vid44'), ('2016-04-11', 'vid50'), ('2016-04-11', 'vid47'), ('2016-04-11', 'vid122'), ('2016-04-11', 'vid45'), ('2016-04-11', 'vid79'), ('2016-04-11', 'vid46'), ('2016-04-11', 'vid94'), ('2016-04-11', 'vid117'), ('2016-04-11', 'vid59'), ('2016-04-11', 'vid137'), ('2016-04-11', 'vid128'), ('2016-04-11', 'vid53'), ('2016-04-11', 'vid54'), ('2016-04-11', 'vid63'), ('2016-04-11', 'vid132'), ('2016-04-11', 'vid61'), ('2016-04-11', 'vid119'), ('2016-04-11', 'vid56'), ('2016-04-11', 'vid65'), ('2016-04-11', 'vid41'), ('2016-04-11', 'vid111'), ('2016-04-11', 'vid124'), ('2016-04-11', 'vid73'), ('2016-04-11', 'vid39'), ('2016-04-11', 'vid57'), ('2016-04-11', 'vid84'), ('2016-04-11', 'vid52'), ('2016-04-11', 'vid136'), ('2016-04-11', 'vid81'), ('2016-04-11', 'vid76'), ('2016-04-11', 'vid141'), ('2016-04-11', 'vid121'), ('2016-04-11', 'vid140'), ('2016-04-11', 'vid102'), ('2016-04-11', 'vid113'), ('2016-04-11', 'vid80'), ('2016-04-11', 'vid70'), ('2016-04-11', 'vid98'), ('2016-04-11', 'vid85'), ('2016-04-11', 'vid138'), ('2016-04-11', 'vid78'), ('2016-04-11', 'vid60'), ('2016-04-11', 'vid110'), ('2016-04-11', 'vid37'), ('2016-04-11', 'vid130'), ('2016-04-11', 'vid43'), ('2016-04-11', 'vid75'), ('2016-04-11', 'vid99'), ('2016-04-11', 'vid112'), ('2016-04-11', 'vid108'), ('2016-04-11', 'vid134'), ('2016-04-11', 'vid135'), ('2016-04-11', 'vid42'), ('2016-04-11', 'vid101'), ('2016-04-11', 'vid74'), ('2016-04-11', 'vid89'), ('2016-04-11', 'vid106'), ('2016-04-11', 'vid118')]
    }

    segmented_videos = {}
    for date, list_ in d.items():
        segmented_videos[date]=[]
        for i in list_:
            segmented_videos[date].append(i[1])
    return segmented_videos

def term_frequency_mat(codebook_length, wordids, wordcnts):
    term_freq = []
    for counter, (ids, cnts) in enumerate(zip(wordids, wordcnts)):
        # print ids, cnts
        vec = np.array([0] * codebook_length)
        for i, cnt in zip(ids, cnts):
            # print i, cnt
            vec[i] = cnt
        # print "vec: ", vec
        term_freq.append(vec)
        # print "tf: ", term_freq
    feature_space = np.vstack(term_freq)

    # for e, i in enumerate(term_freq):
    #     print e, sum(i)
    #     if sum(i) == 0:
    #         print ">", wordids[e], wordcnts[e]
    # pdb.set_trace()
    return feature_space

def get_file(task, directory):
    video = "%s.p" % task
    d_video = os.path.join(directory, video)
    with open(d_video, 'r') as f:
        try:
            (uuid, label, ids, histogram) = pickle.load(f)
        except:
            "failed to load properly: \n %s" % (video)

    if sum(ids) == 0:
        import pdb; pdb.set_trace()

    return ids, histogram, video, label


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage: please provide a QSR run folder number."
        sys.exit(1)
    else:
        run = sys.argv[1]

    ### load file of dates vs clips
    videos_by_day = segmented_videos()            # actually per day

    # ****************************************************************************************************
    # load qsr videos
    # ****************************************************************************************************
    directory = '/home/'+getpass.getuser()+'/Datasets/ECAI_Data/dataset_segmented_15_12_16/QSR_path/run_%s' % run
    # if not os.path.exists(os.path.join(directory, 'inc_results')): os.makedirs(os.path.join(directory, 'inc_results'))
    print "directory: ", directory

    videos = []
    for k in sorted(videos_by_day):
        for i in videos_by_day[k]:
            videos.append(i)

    codebook_length = 0
    wordids, wordcts, video_names, labels  = [], [], [], []

    for task in videos:
        ids, histogram, video, label = get_file(task, directory)
        wordids.append(ids)
        wordcts.append(histogram)
        video_names.append(video)
        labels.append(label)

        if max(ids) > codebook_length:
            codebook_length = max(ids)

    codebook_length+=1
    print "learning codebook length: ", codebook_length

    v_scores = []
    for l in xrange(10):

        merged = zip(wordids, wordcts, video_names, labels)
        random.shuffle(merged)

        wordids = [a for (a,b,c,d) in merged]
        wordcts = [b for (a,b,c,d) in merged]
        video_names = [c for (a,b,c,d) in merged]
        labels = [d for (a,b,c,d) in merged]

        X = term_frequency_mat(codebook_length, wordids, wordcts)

        C = 1.0
        num_folds = 4
        subset_size = len(videos)/num_folds

        pred_labels, true_labels = [], []
        print "\nLOOP: ", l

        for fold in range(num_folds):
            X_train, X_test, Y_train, Y_test = [], [], [], []
            for i, vid in enumerate(videos):
                if vid in videos[:fold*subset_size] + videos[(fold+1)*subset_size:]:
                    X_train.append(X[i])
                    Y_train.append(labels[i])
                else:
                    X_test.append(X[i])
                    Y_test.append(labels[i])

            X_train = np.vstack(X_train)
            X_test = np.vstack(X_test)

            keep_inds = np.where(X_train.sum(axis=0) > 0)[0]
            X_train = X_train.T[keep_inds].T
            X_test = X_test.T[keep_inds].T

            svc = svm.SVC(kernel='linear', C=C).fit(X_train, Y_train)
            #svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X_train, Y_train)

            for cnt, j in enumerate(X_test):
                label = svc.predict(j.reshape(1, len(j)))[0]
                pred_labels.append(label)

            true_labels.extend(Y_test)
            v_scores.append(metrics.v_measure_score(true_labels, pred_labels))

        # print "\n supervised number of clusters:", len(set(true_labels))
        print("V-measure: %0.3f" % metrics.v_measure_score(true_labels, pred_labels))
        # print("Homogeneity: %0.3f" % metrics.homogeneity_score(true_labels, pred_labels))
        # print("Completeness: %0.3f" % metrics.completeness_score(true_labels, pred_labels))
        # print("Adjusted Rand-Index: %.3f" % metrics.adjusted_rand_score(true_labels, pred_labels))
        # print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(true_labels, pred_labels))


    print "\n VSCORES:",v_scores
    print "average v_score = ", sum(v_scores)/len(v_scores)
