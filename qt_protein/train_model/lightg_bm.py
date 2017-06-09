import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn import preprocessing
from sklearn.cross_validation import KFold
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from math import sqrt
import matplotlib.pyplot as plt
import time
import random
from train_model.calculate import *

def get_value(list):
    return float(list[0])

def merge_list_ap(data):
    merge_list=[]
    print('get spectrum intensity list...')
    merge_list.append(get_merge_list(data.loc[:,['Number','Peptide','Intensity']]))
    return merge_list

def get_data(data_file):
    print('loading data...')
    data = pd.read_csv(data_file)
    
    print('DataShape: ' + str(data.shape))
    label = data['Intensity'].values
    peptide=data['Peptide'].values
    
    merge_list=merge_list_ap(data)

    del data['Intensity']
    del data['Number']
    del data['Peptide']
    X = data.values

    return label,peptide,X,merge_list

def get_params(depth):
    params = {}
    params['lambda_l1']=0.005
    params['verbose'] = 0
    params['learning_rate'] = 0.4
    params['num_iterations'] = 1000
    params['metric']='l2'
    params['max_depth'] = depth 
    params['num_leaves'] = 31
    params['lambda_l2']=500
    params['feature_fraction'] = 1
    params['application'] = 'regression'
    params['feature_fraction_seed'] = 2
    return params
def get_split_list(array_list,merge_list):
    list=[]
    for m in array_list:
        for n in range(len(merge_list[0][m])):
            list.append(merge_list[0][m][n][0]-1)
    return list
def get_cv(merge_list,n_flod,IsShuffle,random_seed):
    print('K-Folds cross validation...')
    cv=KFold(len(merge_list[0]),n_flod,shuffle=IsShuffle,random_state=random_seed)
    print(cv)
    return cv

def train_model(X,label,cv,plst,merge_list,num_round):
    dtrain_predictions = [];idx=[];
    print('training model ...')
    for i,(train_peptide,test_piptide) in enumerate(cv):
        train=get_split_list(train_peptide,merge_list)
        test=get_split_list(test_piptide,merge_list) 
        train_dataset = lgb.Dataset(X[np.array(train)],label=label[np.array(train)])
        test_dataset=lgb.Dataset(X[np.array(test).astype(int)])
        idx.append([x+1 for x in list(test)])
        tmp = time.time()
        bst = lgb.train(plst,train_dataset,num_boost_round=num_round)
        boost_time = time.time() - tmp
        #rmse = bst.eval(lgb.Dataset(X[test],label=label[test]))
        print('Fold {},Boost Time {}'.format(i+1,str(boost_time)))
        dtrain_predictions.append(bst.predict(X[np.array(test)]))
        del bst
    print('training complete...')
    return dtrain_predictions,idx
def write_pred(idx,peptide,dtrain_predictions,output_dir):
    print('write predict data in file')
    pred_result=[];k=0
    for i in range(len(idx)):
        for j in range(len(idx[i])):
            k+=1
            pred_result.append([idx[i][j],dtrain_predictions[i][j]])
    pred_result.sort(key=get_value)
    pred = pd.DataFrame({"Number":[pred_result[i][0] for i in range(k)],"Peptide":peptide,"Intensity":[pred_result[i][1] for i in range(k)]})
    pred.to_csv(output_dir+'/pred.csv')
    return pred
def get_merge_pred(merge_list,pred):
    print('get predict spectrum intensity list...')
    merge_list.append(get_merge_list(pred))
    return merge_list
def get_pearson_x(merge_list,pos,m):
    x=[]
    for j in range(len(merge_list[0][pos])):
        x.append(merge_list[m][pos][j][1])
    return x
def get_pearson(merge_list):
    person_list = []
    print('calculate person coefficient..')
    sum_person = 0.0
    for i in range(len(merge_list[0])):
        person_list.append(pearson_r(get_pearson_x(merge_list,i,0),get_pearson_x(merge_list,i,1)))

    for i in range(len(person_list)):
        sum_person+=person_list[i]
    person_mean = sum_person / float(len(person_list))
    return person_mean
def lightGbm(data_file,params,n_flod,IsShuffle,random_seed,num_round,output_dir):
    label,peptide,X,merge_list=get_data(data_file)
    cv=get_cv(merge_list,n_flod,IsShuffle,random_seed)
    params['application'] = 'regression'
    dtrain_predictions,idx=train_model(X,label,cv,params,merge_list,num_round)
    pred=write_pred(idx,peptide,dtrain_predictions,output_dir)
    merge_list=get_merge_pred(merge_list,pred)
    person_mean=get_pearson(merge_list)
    print(person_mean)

