#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:48:31 2017

@author: nathan BALBLANC and Yacine SMINI
"""

import tensorflow as tf
import numpy as np
import os

#import des results de train
from result import maps, decisions_piece_type, decisions, even_further_contexts,far_contexts
from result1 import maps1, decisions_piece_type1, decisions1,even_further_contexts1,far_contexts1
from result2 import maps2, decisions_piece_type2, decisions2,even_further_contexts2,far_contexts2
from result3 import maps3, decisions_piece_type3, decisions3,even_further_contexts3,far_contexts3
from result4 import maps4, decisions_piece_type4, decisions4,even_further_contexts4,far_contexts4
from result5 import maps5, decisions_piece_type5, decisions5, even_further_contexts5,far_contexts5
from result6 import maps6, decisions_piece_type6, decisions6, even_further_contexts6,far_contexts6
from result7 import maps7, decisions_piece_type7, decisions7, even_further_contexts7,far_contexts7
from result8 import maps8, decisions_piece_type8, decisions8, even_further_contexts8,far_contexts8
from result9 import maps9, decisions_piece_type9, decisions9, even_further_contexts9,far_contexts9
from result10 import maps10, decisions_piece_type10, decisions10, even_further_contexts10,far_contexts10


from result11 import maps11, decisions_piece_type11, decisions11, even_further_contexts11,far_contexts11
from result12 import maps12, decisions_piece_type12, decisions12,even_further_contexts12,far_contexts12
from result13 import maps13, decisions_piece_type13, decisions13,even_further_contexts13,far_contexts13
from result14 import maps14, decisions_piece_type14, decisions14,even_further_contexts14,far_contexts14
from result15 import maps15, decisions_piece_type15, decisions15, even_further_contexts15,far_contexts15
from result16 import maps16, decisions_piece_type16, decisions16, even_further_contexts16,far_contexts16
from result17 import maps17, decisions_piece_type17, decisions17, even_further_contexts17,far_contexts17
from result18 import maps18, decisions_piece_type18, decisions18, even_further_contexts18,far_contexts18
from result19 import maps19, decisions_piece_type19, decisions19, even_further_contexts19,far_contexts19
from result20 import maps20, decisions_piece_type20, decisions20, even_further_contexts20,far_contexts20
from result21 import maps21, decisions_piece_type21, decisions21, even_further_contexts21,far_contexts21

from result22 import maps22, decisions_piece_type22, decisions22, even_further_contexts22,far_contexts22
from result23 import maps23, decisions_piece_type23, decisions23, even_further_contexts23,far_contexts23
from result24 import maps24, decisions_piece_type24, decisions24, even_further_contexts24,far_contexts24
from result25 import maps25, decisions_piece_type25, decisions25, even_further_contexts25,far_contexts25
from result26 import maps26, decisions_piece_type26, decisions26, even_further_contexts26,far_contexts26
from result27 import maps27, decisions_piece_type27, decisions27, even_further_contexts27,far_contexts27
from result28 import maps28, decisions_piece_type28, decisions28, even_further_contexts28,far_contexts28
from result29 import maps29, decisions_piece_type29, decisions29, even_further_contexts29,far_contexts29
from result30 import maps30, decisions_piece_type30, decisions30, even_further_contexts30,far_contexts30
from result31 import maps31, decisions_piece_type31, decisions31, even_further_contexts31,far_contexts31

from result32 import maps32, decisions_piece_type32, decisions32, even_further_contexts32,far_contexts32
from result33 import maps33, decisions_piece_type33, decisions33, even_further_contexts33,far_contexts33
from result34 import maps34, decisions_piece_type34, decisions34, even_further_contexts34,far_contexts34
from result35 import maps35, decisions_piece_type35, decisions35, even_further_contexts35,far_contexts35
from result36 import maps36, decisions_piece_type36, decisions36, even_further_contexts36,far_contexts36
from result37 import maps37, decisions_piece_type37, decisions37, even_further_contexts37,far_contexts37
from result38 import maps38, decisions_piece_type38, decisions38, even_further_contexts38,far_contexts38
from result39 import maps39, decisions_piece_type39, decisions39, even_further_contexts39,far_contexts39
from result40 import maps40, decisions_piece_type40, decisions40, even_further_contexts40,far_contexts40
from result41 import maps41, decisions_piece_type41, decisions41, even_further_contexts41,far_contexts41
from result42 import maps42, decisions_piece_type42, decisions42, even_further_contexts42,far_contexts42
from result43 import maps43, decisions_piece_type43, decisions43, even_further_contexts43,far_contexts43
from result44 import maps44, decisions_piece_type44, decisions44, even_further_contexts44,far_contexts44
from result45 import maps45, decisions_piece_type45, decisions45, even_further_contexts45,far_contexts45
from result46 import maps46, decisions_piece_type46, decisions46, even_further_contexts46,far_contexts46
from result47 import maps47, decisions_piece_type47, decisions47, even_further_contexts47,far_contexts47
from result48 import maps48, decisions_piece_type48, decisions48, even_further_contexts48,far_contexts48
from result49 import maps49, decisions_piece_type49, decisions49, even_further_contexts49,far_contexts49
from result50 import maps50, decisions_piece_type50, decisions50, even_further_contexts50,far_contexts50
from result51 import maps51, decisions_piece_type51, decisions51, even_further_contexts51,far_contexts51
from result52 import maps52, decisions_piece_type52, decisions52, even_further_contexts52,far_contexts52



possible_actions = 7
#DEF type unite
#TODO : A CHANGER CECI EST POUR UN TRAIN DE TEST A CHANGER PAR LES VRAIES VALEURS
ARMY = 0
FLIGHT = 1
BOAT = 4
CITY = -1
PATROL = 3
TRANSPORT = 2

#Info de Linear
y_true = tf.placeholder(tf.float32, [None, possible_actions])
y_true_cls = tf.placeholder(tf.int64, [None])

maps_global = [maps,maps1,maps2,maps3,maps5,maps6,maps7,maps8,maps9,maps10,maps11,maps12,maps13,maps14,maps15,maps16,maps17,maps18,maps19,maps20,maps21,maps22,maps23,maps24,maps25,maps26,maps27,maps28,maps29,maps30,maps31,maps32,maps33,maps34,maps35,maps36,maps37,maps38,maps39,maps40]
decisions_global =[decisions,decisions1,decisions2,decisions3,decisions5,decisions6,decisions7,decisions8,decisions9,decisions10,decisions11,decisions12,decisions13,decisions14,decisions15,decisions16,decisions17,decisions18,decisions19,decisions20,decisions21,decisions22,decisions23,decisions24,decisions25,decisions26,decisions27,decisions28,decisions29,decisions30,decisions31,decisions32,decisions33,decisions34,decisions35,decisions36,decisions37,decisions38,decisions39,decisions40]
decisions_piece_type_global = [decisions_piece_type,decisions_piece_type1,decisions_piece_type2,decisions_piece_type3,decisions_piece_type5,decisions_piece_type6,decisions_piece_type7,decisions_piece_type8,decisions_piece_type9,decisions_piece_type10,decisions_piece_type11,decisions_piece_type12,decisions_piece_type13,decisions_piece_type14,decisions_piece_type15,decisions_piece_type16,decisions_piece_type17,decisions_piece_type18,decisions_piece_type19,decisions_piece_type20,decisions_piece_type21,decisions_piece_type22,decisions_piece_type23,decisions_piece_type24,decisions_piece_type25,decisions_piece_type26,decisions_piece_type27,decisions_piece_type28,decisions_piece_type29,decisions_piece_type30,decisions_piece_type31,decisions_piece_type32,decisions_piece_type33,decisions_piece_type34,decisions_piece_type35,decisions_piece_type36,decisions_piece_type37,decisions_piece_type38,decisions_piece_type39,decisions_piece_type40]
far_contexts_global = [far_contexts,far_contexts1,far_contexts2,far_contexts3,far_contexts5,far_contexts6,far_contexts7,far_contexts8,far_contexts9,far_contexts10,far_contexts11,far_contexts12,far_contexts13,far_contexts14,far_contexts15,far_contexts16,far_contexts17,far_contexts18,far_contexts19,far_contexts20,far_contexts21,far_contexts22,far_contexts23,far_contexts24,far_contexts25,far_contexts26,far_contexts27,far_contexts28,far_contexts29,far_contexts30,far_contexts31,far_contexts32,far_contexts33,far_contexts34,far_contexts35,far_contexts36,far_contexts37,far_contexts38,far_contexts39,far_contexts40]
even_further_contexts_global =[even_further_contexts,even_further_contexts1,even_further_contexts2,even_further_contexts3,even_further_contexts5,even_further_contexts6,even_further_contexts7,even_further_contexts8,even_further_contexts9,even_further_contexts10,even_further_contexts11,even_further_contexts12,even_further_contexts13,even_further_contexts14,even_further_contexts15,even_further_contexts16,even_further_contexts17,even_further_contexts18,even_further_contexts19,even_further_contexts20,even_further_contexts21,even_further_contexts22,even_further_contexts23,even_further_contexts24,even_further_contexts25,even_further_contexts26,even_further_contexts27,even_further_contexts28,even_further_contexts29,even_further_contexts30,even_further_contexts31,even_further_contexts32,even_further_contexts33,even_further_contexts34,even_further_contexts35,even_further_contexts36,even_further_contexts37,even_further_contexts38,even_further_contexts39,even_further_contexts40]


maps_train = [maps41,maps42,maps43,maps44,maps45,maps46,maps47,maps48,maps49,maps50,maps51,maps52,maps4]
decisions_train = [decisions41,decisions42,decisions43,decisions44,decisions45,decisions46,decisions47,decisions48,decisions49,decisions50,decisions51,decisions52,decisions4]
decisions_piece_type_train= [decisions_piece_type41,decisions_piece_type42,decisions_piece_type43,decisions_piece_type44,decisions_piece_type45,decisions_piece_type46,decisions_piece_type47,decisions_piece_type48,decisions_piece_type49,decisions_piece_type50,decisions_piece_type51,decisions_piece_type52,decisions_piece_type4]
far_contexts_train= [far_contexts41,far_contexts42,far_contexts43,far_contexts44,far_contexts45,far_contexts46,far_contexts47,far_contexts48,far_contexts49,far_contexts50,far_contexts51,far_contexts52,far_contexts4]
even_further_contexts_train= [even_further_contexts41,even_further_contexts42,even_further_contexts43,even_further_contexts44,even_further_contexts45,even_further_contexts46,even_further_contexts47,even_further_contexts48,even_further_contexts49,even_further_contexts50,even_further_contexts51,even_further_contexts52,even_further_contexts4]
       
first_size = 49
possible_actions = 7
first_hidden_layers_size_terrestre = 48
snd_hidden_layers_size_terrestre = 48
#learning_rate = 0.6
global_step = tf.Variable(0, trainable=False)
starter_learning_rate = 0.1
learning_rate = tf.train.exponential_decay(starter_learning_rate, global_step,
                                       100000, 0.96, staircase=True)

# Passing global_step to minimize() will increment it at each step.

#Definition des reseaux des neurones pour unités terrestres
#first_weights_terre = tf.Variable(tf.zeros([first_size, first_hidden_layers_size_terrestre]))
#first_biases_terre = tf.Variable(tf.zeros([first_hidden_layers_size_terrestre]))
first_weights_terre = (tf.Variable(tf.truncated_normal([first_size,first_hidden_layers_size_terrestre], stddev=5.0)))
first_biases_terre = tf.abs(tf.Variable(tf.truncated_normal([first_hidden_layers_size_terrestre],stddev=5.0)))
    
#snd_weights_terre = tf.Variable(tf.zeros([first_hidden_layers_size_terrestre, snd_hidden_layers_size_terrestre]))
#snd_biases_terre = tf.Variable(tf.zeros([snd_hidden_layers_size_terrestre]))
snd_weights_terre = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_terrestre,snd_hidden_layers_size_terrestre], stddev=5.0)))
snd_biases_terre = tf.abs(tf.Variable(tf.truncated_normal([snd_hidden_layers_size_terrestre], stddev=5.0)))
   
#last_weights_terre = tf.Variable(tf.zeros([snd_hidden_layers_size_terrestre, possible_actions]))
#last_biases_terre = tf.Variable(tf.zeros([possible_actions]))
last_weights_terre = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_terrestre,possible_actions], stddev=5.0)))
last_biases_terre = tf.abs(tf.Variable(tf.truncated_normal([possible_actions], stddev=5.0)))  
	# input layer
input_layer_terre = tf.placeholder(tf.float32, [None, first_size])#Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones
    
	# hidden layers
first_layer_terre = tf.nn.relu(tf.matmul(input_layer_terre, first_weights_terre) + first_biases_terre) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_terre = tf.nn.relu(tf.matmul(first_layer_terre, snd_weights_terre) + snd_biases_terre) #Prend une [1;50] et sors une [1;7]    
    #out layers On n'a qu'un seul neurones de sorties
logits_terre = tf.matmul(snd_layer_terre, last_weights_terre) + last_biases_terre #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_terre = tf.nn.softmax(logits_terre) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_terre = tf.argmax(out_layer_terre, dimension=1) #Choix final de mouvement     
    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_terre = tf.nn.softmax_cross_entropy_with_logits(logits = logits_terre,
                                                        labels=y_true)
cost_terre = tf.reduce_mean(cross_entropy_terre)
#optimizer_terre = tf.train.AdagradOptimizer(learning_rate).minimize(cost_terre)
optimizer_terre=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_terre, global_step=global_step))
correct_prediction_terre = tf.equal(out_decision_terre, y_true_cls)
accuracy_terre = tf.reduce_mean(tf.cast(correct_prediction_terre, tf.float32))

      

first_hidden_layers_size_flight = 42
snd_hidden_layers_size_flight = 42  
#Definition des reseaux des neurones pour unités Volantes
	# network weights
first_weights_flight = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_flight], stddev=5.0)))
first_biases_flight = tf.abs(tf.Variable(tf.truncated_normal([first_hidden_layers_size_flight], stddev=5.0)))
    
snd_weights_flight = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_flight, snd_hidden_layers_size_flight], stddev=5.0)))
snd_biases_flight = tf.abs(tf.Variable(tf.truncated_normal([snd_hidden_layers_size_flight], stddev=5.0)))
    
last_weights_flight = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_flight, possible_actions], stddev=5.0)))
last_biases_flight = tf.abs(tf.Variable(tf.truncated_normal([possible_actions], stddev=5.0)))
    
	# input layer
input_layer_flight = tf.placeholder(tf.float32, [None, first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones
    
	# hidden layers
first_layer_flight = tf.nn.relu(tf.matmul(input_layer_flight, first_weights_flight) + first_biases_flight) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_flight = tf.nn.relu(tf.matmul(first_layer_flight, snd_weights_flight) + snd_biases_flight) #Prend une [1;50] et sors une [1;7]
    
    #out layers On n'a qu'un seul neurones de sorties
logits_flight = tf.matmul(snd_layer_flight, last_weights_flight) + last_biases_flight #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_flight = tf.nn.softmax(logits_flight) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_flight = tf.argmax(out_layer_flight, dimension=1) #Choix final de mouvement 
    
    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_flight = tf.nn.softmax_cross_entropy_with_logits(logits = logits_flight,
                                                        labels=y_true)
cost_flight = tf.reduce_mean(cross_entropy_flight)

#optimizer_flight = tf.train.AdagradOptimizer(learning_rate).minimize(cost_flight)
optimizer_flight=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_flight, global_step=global_step))
correct_prediction_flight = tf.equal(out_decision_flight, y_true_cls)
accuracy_flight = tf.reduce_mean(tf.cast(correct_prediction_flight, tf.float32))

    
    
first_hidden_layers_size_boat = 30
snd_hidden_layers_size_boat = 30  
#Definition des reseaux des neurones pour unités aquatiques

	# network weights
first_weights_boat = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_boat], stddev=5.0)))
first_biases_boat = tf.abs(tf.Variable(tf.truncated_normal([first_hidden_layers_size_boat], stddev=1.0)))
        
snd_weights_boat = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_boat, snd_hidden_layers_size_boat], stddev=5.0)))
snd_biases_boat = tf.abs(tf.Variable(tf.truncated_normal([snd_hidden_layers_size_boat], stddev=5.0)))
        
last_weights_boat = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_boat, possible_actions], stddev=5.0)))
last_biases_boat = tf.abs(tf.Variable(tf.truncated_normal([possible_actions], stddev=5.0)))
        
	# input layer
input_layer_boat = tf.placeholder(tf.float32, [None, first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones
    
	# hidden layers
first_layer_boat = tf.nn.relu(tf.matmul(input_layer_boat, first_weights_boat) + first_biases_boat) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_boat = tf.nn.relu(tf.matmul(first_layer_boat, snd_weights_boat) + snd_biases_boat) #Prend une [1;50] et sors une [1;7]
    
    #out layers On n'a qu'un seul neurones de sorties
logits_boat = tf.matmul(snd_layer_boat, last_weights_boat) + last_biases_boat #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_boat = tf.nn.softmax(logits_boat) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_boat = tf.argmax(out_layer_boat, dimension=1) #Choix final de mouvement 
    
    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_boat = tf.nn.softmax_cross_entropy_with_logits(logits = logits_boat,
                                                        labels=y_true)
cost_boat = tf.reduce_mean(cross_entropy_boat)

#optimizer_boat = tf.train.AdagradOptimizer(learning_rate).minimize(cost_boat)
optimizer_boat=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_boat, global_step=global_step))
correct_prediction_boat = tf.equal(out_decision_boat, y_true_cls)
accuracy_boat = tf.reduce_mean(tf.cast(correct_prediction_boat, tf.float32))



#CITY LAYER
first_hidden_layers_size_city = 48 #TODO : A remplacer par le bon nombre de pocibilité
snd_hidden_layers_size_city = 48

#Definition des reseaux des neurones pour unités terrestres
    
	# network weights
first_weights_city = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_city], stddev=5.0)))
first_biases_city= tf.abs(tf.Variable(tf.truncated_normal([first_hidden_layers_size_city], stddev=5.0)))
    
snd_weights_city= (tf.Variable(tf.truncated_normal([first_hidden_layers_size_city, snd_hidden_layers_size_city], stddev=5.0)))
snd_biases_city= tf.abs(tf.Variable(tf.truncated_normal([snd_hidden_layers_size_city], stddev=5.0)))
    
last_weights_city= (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_city, possible_actions], stddev=5.0)))
last_biases_city= tf.abs(tf.Variable(tf.truncated_normal([possible_actions], stddev=5.0)))
    
	# input layer
input_layer_city= tf.placeholder(tf.float32, [None, first_size])#Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones
    
	# hidden layers
first_layer_city= tf.nn.relu(tf.matmul(input_layer_city, first_weights_city) + first_biases_city) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_city= tf.nn.relu(tf.matmul(first_layer_city, snd_weights_city) + snd_biases_city) #Prend une [1;50] et sors une [1;7]
    
    #out layers On n'a qu'un seul neurones de sorties
logits_city= tf.matmul(snd_layer_city, last_weights_city) + last_biases_city #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_city= tf.nn.softmax(logits_city) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_city= tf.argmax(out_layer_city, dimension=1) #Choix final de mouvement 
    
    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_city= tf.nn.softmax_cross_entropy_with_logits(logits = logits_city,
                                                        labels=y_true)
cost_city= tf.reduce_mean(cross_entropy_city)

#optimizer_city= tf.train.AdagradOptimizer(learning_rate).minimize(cost_city)
optimizer_city=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_city, global_step=global_step))
correct_prediction_city= tf.equal(out_decision_city, y_true_cls)
accuracy_city= tf.reduce_mean(tf.cast(correct_prediction_city, tf.float32))


# Best validation accuracy seen so far.
best_validation_accuracy = 0.0
saver = tf.train.Saver()
save_dir = 'checkpoints/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
save_path = os.path.join(save_dir, 'best_validation')


def concat_tab(tab1,tab2,tab3) : 
    tail1 = len(tab1)
    tail2 = len(tab2)
    tail3 = len(tab3)
    tab_retour = np.zeros(shape = (1, (tail1+tail2+tail3))) 
    j = 0
    for i in range(tail1):
        tab_retour[0][j] = tab1[i]
        j = j+1
    for i in range(tail2):
        tab_retour[0][j] = tab2[i]
        j = j+1
    for i in range(tail3):
        tab_retour[0][j] = tab3[i]
        j = j+1
        
    return tab_retour
    

def test_egalite(c1,c2):
    c7 = len(c1) *[0]
    for i in range(len(c1)) :
        c3 = c1[i]
        c4 = c2[i]
        preci1 = np.argmax(c3)
        preci2 = c4
#        print (preci2)
#        print(preci1)
#        print (preci2)
#        print("-----------------------------------------------------------------")
#        
        if preci1 == preci2 :
            c7[i] =1

    return c7


def predict_cls_validation(maps_train,decisions_train,decisions_piece_type_train,far_contexts_train,even_further_contexts_train):
    return predict_cls(maps = maps_train,
                       labels = decisions_train,
                       decisions = decisions_train,
                       decisions_piece_type = decisions_piece_type_train,
                       far_contexts = far_contexts_train,
                       even_further_contexts = even_further_contexts_train)
    
def create_label_test(decisions):
    labels_create = len(decisions)*[0]
    for i in range(len(decisions)):
        decision = decisions[i]
        decision_tab = np.zeros((1,7))  
        decision_tab[0][decision] = 1
        for j in range(len(decision_tab)):
            labels_create[i] = decision_tab
    return labels_create


def predict_cls(maps, labels, decisions, decisions_piece_type,far_contexts,even_further_contexts):
    nb_maps = len(maps)
    decision_tab = create_label_test(decisions)

    cls_pred = nb_maps*[0]
    for i in range(nb_maps):
        decision_piece_type = decisions_piece_type[i]
        far_context = far_contexts[i]
        even_further_context = even_further_contexts[i]
        mape = maps[i]
        tab_context_far = far_context.split()       
                
        tab_context_further = even_further_context.split()
            
        tab_mape = mape.split()
        tab_float_map = len(tab_mape) *[0]
        for j in range(len(tab_mape)):
            tab_float_map[j] = ord(tab_mape[j])
        #print (tab_float_map)
        tab_float = concat_tab(tab_float_map,tab_context_far,tab_context_further)
        #print (tab_float)
        if decision_piece_type == ARMY :
            feed_dict_train = {input_layer_terre: tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_terre, feed_dict=feed_dict_train)
            
        if decision_piece_type == FLIGHT :
            feed_dict_train = {input_layer_flight: tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_flight, feed_dict=feed_dict_train)
        if decision_piece_type == BOAT :
            feed_dict_train = {input_layer_boat : tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_boat, feed_dict=feed_dict_train)    
        if decision_piece_type == CITY :
            feed_dict_train = {input_layer_city : tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_city, feed_dict=feed_dict_train)
    correct = test_egalite(decision_tab,cls_pred)


    return correct, cls_pred

  
def cls_accuracy(correct,maps):
 
    somme = 0
    for i in range (len(correct)) :
        somme = somme + correct[i]

    acc = float(somme) / len(maps)
    return acc, somme

def validation_accuracy():
    i =0
    for i in range(len(maps_train)) : 
#        print ("TRAIN %d en cours d'execution !!"%i)
        correct, _ = predict_cls_validation(maps_train[i],decisions_train[i],decisions_piece_type_train[i],far_contexts_train[i],even_further_contexts_train[i])
    return cls_accuracy(correct,maps_train[i])


session = tf.Session()
session.run(tf.global_variables_initializer())

def optimize():
    global best_validation_accuracy
    for w in range(10):
        j = 0
        print ("Bloc %d" %w)
        for j in range(len(maps_global)) :
            i = 0
            print ("Partie %d en cours de test"%j)
    #        print (session.run(first_weights_terre))
            maps = maps_global[j]
            far_contexts = far_contexts_global[j]
            even_further_contexts = even_further_contexts_global[j]
            decisions = decisions_global[j]
            decisions_piece_type = decisions_piece_type_global[j]
            for i in range(len(maps)):
                #print ("Je train le coup %d" %i)
                mape = maps[i]
                far_context = far_contexts[i]
                even_further_context = even_further_contexts[i]
                tab_context_far = far_context.split()                
                tab_context_further = even_further_context.split()
                tab_mape = mape.split()
               # print (tab_mape)
                tab_float = len(tab_mape) *[0]
                for j in range(len(tab_mape)):
                    tab_float[j] = ord(tab_mape[j])
               # print (tab_float)
                tab_float = concat_tab(tab_float,tab_context_far,tab_context_further)
               # print (tab_float)
                decision = decisions[i]
                decision_piece_type = decisions_piece_type[i]
                if decision_piece_type == ARMY :
                    decision_tab = np.zeros((1,7))  
                    decision_tab[0][decision] = 1
                   # print (decision_tab)
                    feed_dict_train = {input_layer_terre: tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_terre, feed_dict=feed_dict_train)
                   # acc_train = session.run(accuracy_terre, feed_dict=feed_dict_train)
    
                if decision_piece_type == FLIGHT :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                   # print (decision_tab)
                    feed_dict_train = {input_layer_flight: tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_flight, feed_dict=feed_dict_train)
                   # acc_train = session.run(accuracy_terre, feed_dict=feed_dict_train)
    
                if decision_piece_type == BOAT :
                    decision_tab = np.zeros((1,7)) 
                    decision_tab[0][decision] = 1
                 #   print (decision_tab)
                    feed_dict_train = {input_layer_boat : tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_boat, feed_dict=feed_dict_train)
                  #  acc_train = session.run(accuracy_terre, feed_dict=feed_dict_train)
    
                if decision_piece_type == CITY :
                    decision_tab = np.zeros((1,7)) 
                    decision_tab[0][decision] = 1
                #    print (decision_tab)
                    feed_dict_train = {input_layer_city : tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_city, feed_dict=feed_dict_train)
                  #  acc_train = session.run(accuracy_city, feed_dict=feed_dict_train)
            acc_validation, _ = validation_accuracy()
          #  print (acc_validation)
            if acc_validation > best_validation_accuracy:
                # print (best_validation_accuracy)
                # Update the best-known validation accuracy.
                best_validation_accuracy = acc_validation
                print ("NOUVELLE SAUVEGARDE -------------------------------------------------------")
                print (best_validation_accuracy)
                print ("---------------------------------------------------------------------------")
                # Save all variables of the TensorFlow graph to file.
                saver.save(sess=session, save_path=save_path)
                #print ("j'ai sauvegarde !!! %d"% best_validation_accuracy)
    print(best_validation_accuracy)


optimize()
#TODO : FAIRE LIMPLEMENTATION DU SAVE ET DU RESEAU DE NEURONES DES VILLES