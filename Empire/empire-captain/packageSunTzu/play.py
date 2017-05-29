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
BOAT = 4
CITY = -1
PATROL = 3
TRANSPORT = 2

#Info de Linear
y_true = tf.placeholder(tf.float32, [None, possible_actions])
y_true_cls = tf.placeholder(tf.int64, [None])


first_size = 49
possible_actions = 7
first_hidden_layers_size_terrestre = 240
snd_hidden_layers_size_terrestre = 240

#
#global_step = tf.Variable(0, trainable=False)
#starter_learning_rate = 0.0001
#learning_rate = tf.train.exponential_decay(starter_learning_rate, global_step,
#                                       100000, 0.96, staircase=True)
learning_rate = 0.001
# Passing global_step to minimize() will increment it at each step.

#Definition des reseaux des neurones pour unités terrestres
#first_weights_terre = tf.Variable(tf.zeros([first_size, first_hidden_layers_size_terrestre]))
#first_biases_terre = tf.Variable(tf.zeros([first_hidden_layers_size_terrestre]))
first_weights_terre = (tf.Variable(tf.truncated_normal([first_size,first_hidden_layers_size_terrestre], stddev=0.1)))
first_biases_terre = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_terrestre],stddev=0.1)))

snd_weights_terre = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_terrestre,snd_hidden_layers_size_terrestre], stddev=0.1)))
snd_biases_terre = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_terrestre], stddev=0.1)))

#snd_weights_terre = tf.Variable(tf.zeros([first_hidden_layers_size_terrestre, snd_hidden_layers_size_terrestre]))
#snd_biases_terre = tf.Variable(tf.zeros([snd_hidden_layers_size_terrestre]))
third_weights_terre = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_terrestre,snd_hidden_layers_size_terrestre], stddev=0.1)))
third_biases_terre = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_terrestre], stddev=0.1)))

#last_weights_terre = tf.Variable(tf.zeros([snd_hidden_layers_size_terrestre, possible_actions]))
#last_biases_terre = tf.Variable(tf.zeros([possible_actions]))
last_weights_terre = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_terrestre,possible_actions], stddev=0.1)))
last_biases_terre = (tf.Variable(tf.truncated_normal([possible_actions], stddev=0.1)))
	# input layer
input_layer_terre = tf.placeholder(tf.float32, [None, first_size])#Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

	# hidden layers
first_layer_terre = tf.sigmoid(tf.matmul(input_layer_terre, first_weights_terre) + first_biases_terre) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_terre = tf.sigmoid(tf.matmul(first_layer_terre, snd_weights_terre) + snd_biases_terre) #Prend une [1;50] et sors une [1;7]
    #out layers On n'a qu'un seul neurones de sorties
third_layer_terre = tf.sigmoid(tf.matmul(snd_layer_terre, third_weights_terre) + third_biases_terre) #Prend une [1;50] et sors une [1;7]

logits_terre = tf.matmul(third_layer_terre, last_weights_terre) + last_biases_terre #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_terre = tf.sigmoid(logits_terre) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_terre = tf.argmax(out_layer_terre, dimension=1) #Choix final de mouvement




first_hidden_layers_size_flight = 240
snd_hidden_layers_size_flight = 240
#Definition des reseaux des neurones pour unités Volantes
	# network weights
first_weights_flight = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_flight], stddev=0.1)))
first_biases_flight = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_flight], stddev=0.1)))

snd_weights_flight = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_flight, snd_hidden_layers_size_flight], stddev=0.1)))
snd_biases_flight = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_flight], stddev=0.1)))
third_weights_flight = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_flight,snd_hidden_layers_size_flight], stddev=0.1)))
third_biases_flight = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_flight], stddev=0.1)))

last_weights_flight = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_flight, possible_actions], stddev=0.1)))
last_biases_flight = (tf.Variable(tf.truncated_normal([possible_actions], stddev=0.1)))

	# input layer
input_layer_flight = tf.placeholder(tf.float32, [None, first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

	# hidden layers
first_layer_flight = tf.sigmoid(tf.matmul(input_layer_flight, first_weights_flight) + first_biases_flight) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_flight = tf.sigmoid(tf.matmul(first_layer_flight, snd_weights_flight) + snd_biases_flight) #Prend une [1;50] et sors une [1;7]
third_layer_flight = tf.sigmoid(tf.matmul(snd_layer_flight, third_weights_flight) + third_biases_flight) #Prend une [1;50] et sors une [1;7]

    #out layers On n'a qu'un seul neurones de sorties
logits_flight = tf.matmul(third_layer_flight, last_weights_flight) + last_biases_flight #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_flight = tf.sigmoid(logits_flight) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_flight = tf.argmax(out_layer_flight, dimension=1) #Choix final de mouvement




first_hidden_layers_size_boat = 240
snd_hidden_layers_size_boat = 240
#Definition des reseaux des neurones pour unités aquatiques

	# network weights
first_weights_boat = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_boat], stddev=0.1)))
first_biases_boat = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_boat], stddev=0.1)))

snd_weights_boat = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_boat, snd_hidden_layers_size_boat], stddev=0.1)))
snd_biases_boat = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_boat], stddev=0.1)))

third_weights_boat = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_boat,snd_hidden_layers_size_boat], stddev=0.1)))
third_biases_boat = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_boat], stddev=0.1)))

last_weights_boat = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_boat, possible_actions], stddev=0.1)))
last_biases_boat = (tf.Variable(tf.truncated_normal([possible_actions], stddev=0.1)))
	# input layer
input_layer_boat = tf.placeholder(tf.float32, [None, first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

	# hidden layers
first_layer_boat = tf.sigmoid(tf.matmul(input_layer_boat, first_weights_boat) + first_biases_boat) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_boat = tf.sigmoid(tf.matmul(first_layer_boat, snd_weights_boat) + snd_biases_boat) #Prend une [1;50] et sors une [1;7]
third_layer_boat = tf.sigmoid(tf.matmul(snd_layer_boat, third_weights_boat) + third_biases_boat) #Prend une [1;50] et sors une [1;7]

    #out layers On n'a qu'un seul neurones de sorties
logits_boat = tf.matmul(third_layer_boat, last_weights_boat) + last_biases_boat #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_boat = tf.sigmoid(logits_boat) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_boat = tf.argmax(out_layer_boat, dimension=1) #Choix final de mouvement



#PATROL
first_hidden_layers_size_patrol = 240
snd_hidden_layers_size_patrol = 240
#Definition des reseaux des neurones pour unités aquatiques

	# network weights
first_weights_patrol = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_patrol], stddev=0.1)))
first_biases_patrol = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_patrol], stddev=0.1)))

snd_weights_patrol = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_patrol, snd_hidden_layers_size_patrol], stddev=0.1)))
snd_biases_patrol = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_patrol], stddev=0.1)))

third_weights_patrol = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_patrol,snd_hidden_layers_size_patrol], stddev=0.1)))
third_biases_patrol = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_patrol], stddev=0.1)))

last_weights_patrol = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_patrol, possible_actions], stddev=0.1)))
last_biases_patrol = (tf.Variable(tf.truncated_normal([possible_actions], stddev=0.1)))
	# input layer
input_layer_patrol = tf.placeholder(tf.float32, [None, first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

	# hidden layers
first_layer_patrol = tf.sigmoid(tf.matmul(input_layer_patrol, first_weights_patrol) + first_biases_patrol) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_patrol = tf.sigmoid(tf.matmul(first_layer_patrol, snd_weights_patrol) + snd_biases_patrol) #Prend une [1;50] et sors une [1;7]
third_layer_patrol= tf.sigmoid(tf.matmul(snd_layer_patrol, third_weights_patrol) + third_biases_patrol) #Prend une [1;50] et sors une [1;7]

    #out layers On n'a qu'un seul neurones de sorties
logits_patrol = tf.matmul(third_layer_patrol, last_weights_patrol) + last_biases_patrol #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_patrol = tf.sigmoid(logits_patrol) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_patrol = tf.argmax(out_layer_patrol, dimension=1) #Choix final de mouvement







#TRANSPORT
first_hidden_layers_size_transport = 240
snd_hidden_layers_size_transport = 240
#Definition des reseaux des neurones pour unités aquatiques

	# network weights
first_weights_transport = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_transport], stddev=0.1)))
first_biases_transport = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_transport], stddev=0.1)))

snd_weights_transport = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_transport, snd_hidden_layers_size_transport], stddev=0.1)))
snd_biases_transport = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_transport], stddev=0.1)))

third_weights_transport = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_transport,snd_hidden_layers_size_transport], stddev=0.1)))
third_biases_transport = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_transport], stddev=0.1)))

last_weights_transport = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_transport, possible_actions], stddev=0.1)))
last_biases_transport = (tf.Variable(tf.truncated_normal([possible_actions], stddev=0.1)))
	# input layer
input_layer_transport = tf.placeholder(tf.float32, [None, first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

	# hidden layers
first_layer_transport = tf.sigmoid(tf.matmul(input_layer_transport, first_weights_transport) + first_biases_transport) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_transport = tf.sigmoid(tf.matmul(first_layer_transport, snd_weights_transport) + snd_biases_transport) #Prend une [1;50] et sors une [1;7]
third_layer_transport= tf.sigmoid(tf.matmul(snd_layer_transport, third_weights_transport) + third_biases_transport) #Prend une [1;50] et sors une [1;7]

    #out layers On n'a qu'un seul neurones de sorties
logits_transport = tf.matmul(third_layer_transport, last_weights_transport) + last_biases_transport #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_transport = tf.sigmoid(logits_transport) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_transport = tf.argmax(out_layer_transport, dimension=1) #Choix final de mouvement





#CITY LAYER
first_hidden_layers_size_city = 240 #TODO : A remplacer par le bon nombre de pocibilité
snd_hidden_layers_size_city = 240

#Definition des reseaux des neurones pour unités terrestres

	# network weights
first_weights_city = (tf.Variable(tf.truncated_normal([first_size, first_hidden_layers_size_city], stddev=0.1)))
first_biases_city= (tf.Variable(tf.truncated_normal([first_hidden_layers_size_city], stddev=0.1)))

snd_weights_city= (tf.Variable(tf.truncated_normal([first_hidden_layers_size_city, snd_hidden_layers_size_city], stddev=0.1)))
snd_biases_city= (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_city], stddev=0.1)))

third_weights_city = (tf.Variable(tf.truncated_normal([first_hidden_layers_size_city,snd_hidden_layers_size_city], stddev=0.1)))
third_biases_city = (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_city], stddev=0.1)))

last_weights_city= (tf.Variable(tf.truncated_normal([snd_hidden_layers_size_city, possible_actions], stddev=0.1)))
last_biases_city= (tf.Variable(tf.truncated_normal([possible_actions], stddev=0.1)))
	# input layer
input_layer_city= tf.placeholder(tf.float32, [None, first_size])#Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

	# hidden layers
first_layer_city= tf.sigmoid(tf.matmul(input_layer_city, first_weights_city) + first_biases_city) # sors [1;50] donc une val par neurones (50 neurones)
snd_layer_city= tf.sigmoid(tf.matmul(first_layer_city, snd_weights_city) + snd_biases_city) #Prend une [1;50] et sors une [1;7]
third_layer_city= tf.sigmoid(tf.matmul(snd_layer_city, third_weights_city) + third_biases_city) #Prend une [1;50] et sors une [1;7]

    #out layers On n'a qu'un seul neurones de sorties
logits_city= tf.matmul(third_layer_city, last_weights_city) + last_biases_city #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
out_layer_city= tf.sigmoid(logits_city) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
out_decision_city= tf.argmax(out_layer_city, dimension=1) #Choix final de mouvement


#Saver
saver = tf.train.Saver()

#save_path = "/Users/leolelonquer/Dropbox/Etudes/Projet_tutoré/projet_IA/IA/checkpoints/best_validation"
save_path = "checkpoints/best_validation"



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
saver = tf.train.Saver()
save_path = "checkpoints/best_validation"
saver.restore(session,"./empire-captain/packageSunTzu/checkpoints/best_validation")

def jouer(tab_mape, type_unit, tab_context_far, tab_context_further):

    tab_float = np.zeros(len(tab_mape))
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

    if type_unit == TRANSPORT :
        feed_dict_run = {input_layer_transport : tab_float}
        out_decision = session.run(out_decision_transport, feed_dict=feed_dict_run)


    if type_unit == PATROL :
        feed_dict_run = {input_layer_patrol : tab_float}
        out_decision = session.run(out_decision_patrol, feed_dict=feed_dict_run)

    return out_decision
