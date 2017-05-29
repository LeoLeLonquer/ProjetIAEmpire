#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:48:31 2017

@author: nathan BALBLANC and Yacine SMINI
"""

import tensorflow as tf
import numpy as np
from result import maps,decisions_piece_type,decisions, even_further_contexts,far_contexts
from result1 import maps1,decisions_piece_type1,decisions1,even_further_contexts1,far_contexts1
from result2 import maps2, decisions_piece_type2, decisions2,even_further_contexts2,far_contexts2
from result3 import maps3,decisions_piece_type3,decisions3,even_further_contexts3,far_contexts3
import os
from result4 import maps4,decisions_piece_type4,decisions4,even_further_contexts4,far_contexts4

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

maps_global = [maps,maps1,maps2,maps3]
decisions_global =[decisions,decisions1,decisions2,decisions3]
decisions_piece_type_global = [decisions_piece_type,decisions_piece_type1,decisions_piece_type2,decisions_piece_type3]
far_contexts_global = [far_contexts,far_contexts1,far_contexts2,far_contexts3]
even_further_contexts_global =[even_further_contexts,even_further_contexts1,even_further_contexts2,even_further_contexts3]
       
first_size = 49
possible_actions = 7
first_hidden_layers_size_terrestre = 48
snd_hidden_layers_size_terrestre = 48
#learning_rate = 0.6
global_step = tf.Variable(0, trainable=False)
starter_learning_rate = 0.001
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
        preci2 = c4[0]
#        print(preci1)
#        print (preci2)
#        print("-----------------------------------------------------------------")
#        
        if preci1 == preci2 :
            c7[i] =1

    return c7


def predict_cls_validation():
    return predict_cls(maps = maps4,
                       labels = decisions4,
                       decisions = decisions4,
                       decisions_piece_type = decisions_piece_type4,
                       far_contexts = far_contexts4,
                       even_further_contexts = even_further_contexts4)
    
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

def validation_accuracy(maps):
    # Get the array of booleans whether the classifications are correct
    # for the validation-set.
    # The function returns two values but we only need the first.
    correct, _ = predict_cls_validation()
    
    # Calculate the classification accuracy and return it.
    return cls_accuracy(correct,maps)


session = tf.Session()
session.run(tf.global_variables_initializer())

def optimize():
    global best_validation_accuracy
    for w in range(150):
        j = 0
        for j in range(len(maps_global)) :
            i = 0
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
            acc_validation, _ = validation_accuracy(maps4)
          #  print (acc_validation)
            if acc_validation > best_validation_accuracy:
                # print (best_validation_accuracy)
                # Update the best-known validation accuracy.
                best_validation_accuracy = acc_validation
                print (best_validation_accuracy)
                # Save all variables of the TensorFlow graph to file.
                saver.save(sess=session, save_path=save_path)
                #print ("j'ai sauvegarde !!! %d"% best_validation_accuracy)
    


optimize()
#TODO : FAIRE LIMPLEMENTATION DU SAVE ET DU RESEAU DE NEURONES DES VILLES