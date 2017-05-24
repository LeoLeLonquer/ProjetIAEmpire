#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:48:31 2017

@author: nathan BALBLANC and Yacine SMINI
"""

import tensorflow as tf
import numpy as np
from result import maps,decisions_piece_type,decisions
from result1 import maps1,decisions_piece_type1,decisions1
from result2 import maps2, decisions_piece_type2, decisions2
from result3 import maps3,decisions_piece_type3,decisions3
#from result4 import maps4,decisions_piece_type4,decisions4

possible_actions = 7
#DEF type unite
#TODO : A CHANGER CECI EST POUR UN TRAIN DE TEST A CHANGER PAR LES VRAIES VALEURS
ARMY = 0
FLIGHT = 1
BOAT = 3
CITY = -1

#Info de Linear
y_true = tf.placeholder(tf.float32, [None, possible_actions])
y_true_cls = tf.placeholder(tf.int64, [None])

maps_global = [maps,maps1,maps2,maps3]
decisions_global =[decisions,decisions1,decisions2,decisions3]
decisions_piece_type_global = [decisions_piece_type,decisions_piece_type1,decisions_piece_type2,decisions_piece_type3]

        
first_size = 37
possible_actions = 7
first_hidden_layers_size_terrestre = 48
snd_hidden_layers_size_terrestre = 48
learning_rate = 0.001

#Definition des reseaux des neurones pour unités terrestres
    
	# network weights
first_weights_terre = tf.Variable(tf.zeros([first_size, first_hidden_layers_size_terrestre]))
first_biases_terre = tf.Variable(tf.zeros([first_hidden_layers_size_terrestre]))
    
snd_weights_terre = tf.Variable(tf.zeros([first_hidden_layers_size_terrestre, snd_hidden_layers_size_terrestre]))
snd_biases_terre = tf.Variable(tf.zeros([snd_hidden_layers_size_terrestre]))
    
last_weights_terre = tf.Variable(tf.zeros([snd_hidden_layers_size_terrestre, possible_actions]))
last_biases_terre = tf.Variable(tf.zeros([possible_actions]))
    
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

optimizer_terre = tf.train.AdagradOptimizer(learning_rate).minimize(cost_terre)
correct_prediction_terre = tf.equal(out_decision_terre, y_true_cls)
accuracy_terre = tf.reduce_mean(tf.cast(correct_prediction_terre, tf.float32))

      

first_hidden_layers_size_flight = 42
snd_hidden_layers_size_flight = 42  
#Definition des reseaux des neurones pour unités Volantes
	# network weights
first_weights_flight = tf.Variable(tf.zeros([first_size, first_hidden_layers_size_flight]))
first_biases_flight = tf.Variable(tf.zeros([first_hidden_layers_size_flight]))
    
snd_weights_flight = tf.Variable(tf.zeros([first_hidden_layers_size_flight, snd_hidden_layers_size_flight]))
snd_biases_flight = tf.Variable(tf.zeros([snd_hidden_layers_size_flight]))
    
last_weights_flight = tf.Variable(tf.zeros([snd_hidden_layers_size_flight, possible_actions]))
last_biases_flight = tf.Variable(tf.zeros([possible_actions]))
    
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

optimizer_flight = tf.train.AdagradOptimizer(learning_rate).minimize(cost_flight)
correct_prediction_flight = tf.equal(out_decision_flight, y_true_cls)
accuracy_flight = tf.reduce_mean(tf.cast(correct_prediction_flight, tf.float32))

    
    
first_hidden_layers_size_boat = 30
snd_hidden_layers_size_boat = 30  
#Definition des reseaux des neurones pour unités aquatiques

	# network weights
first_weights_boat = tf.Variable(tf.zeros([first_size, first_hidden_layers_size_boat]))
first_biases_boat = tf.Variable(tf.zeros([first_hidden_layers_size_boat]))
        
snd_weights_boat = tf.Variable(tf.zeros([first_hidden_layers_size_boat, snd_hidden_layers_size_boat]))
snd_biases_boat = tf.Variable(tf.zeros([snd_hidden_layers_size_boat]))
        
last_weights_boat = tf.Variable(tf.zeros([snd_hidden_layers_size_boat, possible_actions]))
last_biases_boat = tf.Variable(tf.zeros([possible_actions]))
        
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

optimizer_boat = tf.train.AdagradOptimizer(learning_rate).minimize(cost_boat)
correct_prediction_boat = tf.equal(out_decision_boat, y_true_cls)
accuracy_boat = tf.reduce_mean(tf.cast(correct_prediction_boat, tf.float32))



#CITY LAYER
first_size = 37
possible_actions = 7
first_hidden_layers_size_city = 48 #TODO : A remplacer par le bon nombre de pocibilité
snd_hidden_layers_size_city = 48
learning_rate = 0.001

#Definition des reseaux des neurones pour unités terrestres
    
	# network weights
first_weights_city = tf.Variable(tf.zeros([first_size, first_hidden_layers_size_city]))
first_biases_city= tf.Variable(tf.zeros([first_hidden_layers_size_city]))
    
snd_weights_city= tf.Variable(tf.zeros([first_hidden_layers_size_city, snd_hidden_layers_size_city]))
snd_biases_city= tf.Variable(tf.zeros([snd_hidden_layers_size_city]))
    
last_weights_city= tf.Variable(tf.zeros([snd_hidden_layers_size_city, possible_actions]))
last_biases_city= tf.Variable(tf.zeros([possible_actions]))
    
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

optimizer_city= tf.train.AdagradOptimizer(learning_rate).minimize(cost_city)
correct_prediction_city= tf.equal(out_decision_city, y_true_cls)
accuracy_city= tf.reduce_mean(tf.cast(correct_prediction_city, tf.float32))







session = tf.Session()
session.run(tf.global_variables_initializer())

def optimize():
    for j in range(len(maps_global)) :
        maps = maps_global[j]
        decisions = decisions_global[j]
        decisions_piece_type = decisions_piece_type_global[j]
        for i in range(len(maps)):
            mape = maps[i]
            #tab_mape = list(mape)
            tab_mape = mape.split()
            print (tab_mape)
            tab_float = np.zeros(shape = (1, len(tab_mape)))
            for j in range(len(tab_mape)):
                tab_float[0][j] = ord(tab_mape[j])
            print (tab_float)
            decision = decisions[i]
            decision_piece_type = decisions_piece_type[i]
            if decision_piece_type == ARMY :
                decision_tab = np.zeros((1,7))  
                decision_tab[0][decision] = 1
                print (decision_tab)
                feed_dict_train = {input_layer_terre: tab_float,
                               y_true: decision_tab}
                session.run(optimizer_terre, feed_dict=feed_dict_train)
            if decision_piece_type == FLIGHT :
                decision_tab = np.zeros((1,7))
                decision_tab[0][decision] = 1
                print (decision_tab)
                feed_dict_train = {input_layer_flight: tab_float,
                               y_true: decision_tab}
                session.run(optimizer_flight, feed_dict=feed_dict_train)
            if decision_piece_type == BOAT :
                decision_tab = np.zeros((1,7)) 
                decision_tab[0][decision] = 1
                print (decision_tab)
                feed_dict_train = {input_layer_boat : tab_float,
                               y_true: decision_tab}
                session.run(optimizer_boat, feed_dict=feed_dict_train)
            if decision_piece_type == CITY :
                decision_tab = np.zeros((1,7)) 
                decision_tab[0][decision] = 1
                print (decision_tab)
                feed_dict_train = {input_layer_city : tab_float,
                               y_true: decision_tab}
                session.run(optimizer_city, feed_dict=feed_dict_train)

optimize()

#TODO : FAIRE LIMPLEMENTATION DU SAVE ET DU RESEAU DE NEURONES DES VILLES