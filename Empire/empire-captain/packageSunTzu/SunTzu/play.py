# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>



#!/usr/bin/env python3
"""
Created on Thu May 11 10:48:31 2017

@author: nathan BALBLANC and Yacine SMINI
"""

import tensorflow as tf
import numpy as np
import os
#from result import maps,decisions_piece_type,decisions
#from result1 import maps1,decisions_piece_type1,decisions1
#from result2 import maps2, decisions_piece_type2, decisions2
#from result3 import maps3,decisions_piece_type3,decisions3
#from result4 import maps4,decisions_piece_type4,decisions4
#save_path =
possible_actions = 7
#DEF type unite
#TODO : A CHANGER CECI EST POUR UN TRAIN DE TEST A CHANGER PAR LES VRAIES VALEURS
ARMY = 0
FLIGHT = 1
TRANSPORT = 2
PATROL = 3
BOAT = 4
CITY = -1

#Info de Linear
y_true = tf.placeholder(tf.float32, [None, possible_actions])
y_true_cls = tf.placeholder(tf.int64, [None])


first_size = 49
possible_actions = 7
first_hidden_layers_size_terrestre = 48
snd_hidden_layers_size_terrestre = 48


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



#CITY LAYER

first_hidden_layers_size_city = 48 #TODO : A remplacer par le bon nombre de pocibilité
snd_hidden_layers_size_city = 48

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


#Saver
saver = tf.train.Saver()
save_path = "./empire-captain/packageSunTzu/SunTzu/checkpoints/best_validation"



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

session = tf.Session()
session.run(tf.global_variables_initializer())

#on recharge les poids
saver.restore(sess=session, save_path=save_path)


def jouer(tab_mape, type_unit, tab_context_far, tab_context_further):

    tab_float = len(tab_mape) *[0]
    for j in range(len(tab_mape)):
        tab_float[j] = ord(tab_mape[j])

    tab_float = concat_tab(tab_float,tab_context_far,tab_context_further)
    if type_unit == ARMY :
        feed_dict_run = {input_layer_terre : tab_float}
        out_decision =session.run(out_decision_terre, feed_dict=feed_dict_run)


    if type_unit == FLIGHT :
        feed_dict_run = {input_layer_flight : tab_float}
        out_decision = session.run(out_decision_flight, feed_dict=feed_dict_run)

    if type_unit == BOAT :
        feed_dict_run = {input_layer_boat : tab_float}
        out_decision = session.run(out_decision_boat, feed_dict=feed_dict_run)

    if type_unit == CITY :
        feed_dict_run = {input_layer_city : tab_float}
        out_decision = session.run(out_decision_city, feed_dict=feed_dict_run)

    return out_decision
