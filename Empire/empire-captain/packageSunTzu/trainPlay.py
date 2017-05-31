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
from results.result import maps, decisions_piece_type, decisions, even_further_contexts,far_contexts
from results.result1 import maps1, decisions_piece_type1, decisions1,even_further_contexts1,far_contexts1
from results.result2 import maps2, decisions_piece_type2, decisions2,even_further_contexts2,far_contexts2
from results.result3 import maps3, decisions_piece_type3, decisions3,even_further_contexts3,far_contexts3
from results.result4 import maps4, decisions_piece_type4, decisions4,even_further_contexts4,far_contexts4

from results.result41 import maps41, decisions_piece_type41, decisions41, even_further_contexts41,far_contexts41
from results.result42 import maps42, decisions_piece_type42, decisions42, even_further_contexts42,far_contexts42
from results.result43 import maps43, decisions_piece_type43, decisions43, even_further_contexts43,far_contexts43
from results.result44 import maps44, decisions_piece_type44, decisions44, even_further_contexts44,far_contexts44
from results.result45 import maps45, decisions_piece_type45, decisions45, even_further_contexts45,far_contexts45
from results.result46 import maps46, decisions_piece_type46, decisions46, even_further_contexts46,far_contexts46
from results.result47 import maps47, decisions_piece_type47, decisions47, even_further_contexts47,far_contexts47
from results.result48 import maps48, decisions_piece_type48, decisions48, even_further_contexts48,far_contexts48
from results.result49 import maps49, decisions_piece_type49, decisions49, even_further_contexts49,far_contexts49
from results.result50 import maps50, decisions_piece_type50, decisions50, even_further_contexts50,far_contexts50
from results.result51 import maps51, decisions_piece_type51, decisions51, even_further_contexts51,far_contexts51
from results.result52 import maps52, decisions_piece_type52, decisions52, even_further_contexts52,far_contexts52



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


maps_train = [maps41,maps42,maps43,maps44,maps45,maps46,maps47,maps48,maps49,maps50,maps51,maps52,maps4]
decisions_train = [decisions41,decisions42,decisions43,decisions44,decisions45,decisions46,decisions47,decisions48,decisions49,decisions50,decisions51,decisions52,decisions4]
decisions_piece_type_train= [decisions_piece_type41,decisions_piece_type42,decisions_piece_type43,decisions_piece_type44,decisions_piece_type45,decisions_piece_type46,decisions_piece_type47,decisions_piece_type48,decisions_piece_type49,decisions_piece_type50,decisions_piece_type51,decisions_piece_type52,decisions_piece_type4]
far_contexts_train= [far_contexts41,far_contexts42,far_contexts43,far_contexts44,far_contexts45,far_contexts46,far_contexts47,far_contexts48,far_contexts49,far_contexts50,far_contexts51,far_contexts52,far_contexts4]
even_further_contexts_train= [even_further_contexts41,even_further_contexts42,even_further_contexts43,even_further_contexts44,even_further_contexts45,even_further_contexts46,even_further_contexts47,even_further_contexts48,even_further_contexts49,even_further_contexts50,even_further_contexts51,even_further_contexts52,even_further_contexts4]



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
    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_terre = tf.nn.softmax_cross_entropy_with_logits(logits = logits_terre,
                                                        labels=y_true)
cost_terre = tf.reduce_mean(cross_entropy_terre)
optimizer_terre = tf.train.AdagradOptimizer(learning_rate).minimize(cost_terre,var_list=[first_weights_terre,snd_weights_terre,third_weights_terre,last_weights_terre,first_biases_terre,snd_biases_terre,third_biases_terre,last_biases_terre])
#optimizer_terre=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_terre, global_step=global_step))
correct_prediction_terre = tf.equal(out_decision_terre, y_true_cls)
accuracy_terre = tf.reduce_mean(tf.cast(correct_prediction_terre, tf.float32))



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

    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_flight = tf.nn.softmax_cross_entropy_with_logits(logits = logits_flight,
                                                        labels=y_true)
cost_flight = tf.reduce_mean(cross_entropy_flight)

optimizer_flight = tf.train.AdagradOptimizer(learning_rate).minimize(cost_flight,var_list=[first_biases_flight,snd_biases_flight,third_biases_flight,last_biases_flight,first_weights_flight,snd_weights_flight,third_weights_flight,last_weights_flight])
#optimizer_flight=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_flight, global_step=global_step))
correct_prediction_flight = tf.equal(out_decision_flight, y_true_cls)
accuracy_flight = tf.reduce_mean(tf.cast(correct_prediction_flight, tf.float32))



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

    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_boat = tf.nn.softmax_cross_entropy_with_logits(logits = logits_boat,
                                                        labels=y_true)
cost_boat = tf.reduce_mean(cross_entropy_boat)

optimizer_boat = tf.train.AdagradOptimizer(learning_rate).minimize(cost_boat,var_list=[ first_biases_boat,  snd_biases_boat,third_biases_boat, last_biases_boat,first_weights_boat,snd_weights_boat,third_weights_boat,last_weights_boat])
#optimizer_boat=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_boat, global_step=global_step))
correct_prediction_boat = tf.equal(out_decision_boat, y_true_cls)
accuracy_boat = tf.reduce_mean(tf.cast(correct_prediction_boat, tf.float32))



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

    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_patrol = tf.nn.softmax_cross_entropy_with_logits(logits = logits_patrol,
                                                        labels=y_true)
cost_patrol = tf.reduce_mean(cross_entropy_patrol)

optimizer_patrol = tf.train.AdagradOptimizer(learning_rate).minimize(cost_patrol,var_list=[ first_biases_patrol,  snd_biases_patrol,third_biases_patrol, last_biases_patrol,first_weights_patrol,snd_weights_patrol,third_weights_patrol,last_weights_patrol])
#optimizer_boat=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_boat, global_step=global_step))
correct_prediction_patrol = tf.equal(out_decision_patrol, y_true_cls)
accuracy_patrol = tf.reduce_mean(tf.cast(correct_prediction_patrol, tf.float32))






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

    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_transport = tf.nn.softmax_cross_entropy_with_logits(logits = logits_transport,
                                                        labels=y_true)
cost_transport = tf.reduce_mean(cross_entropy_transport)

optimizer_transport = tf.train.AdagradOptimizer(learning_rate).minimize(cost_transport,var_list=[ first_biases_transport,  snd_biases_transport,third_biases_transport, last_biases_transport,first_weights_transport,snd_weights_transport,third_weights_transport,last_weights_transport])
#optimizer_boat=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_boat, global_step=global_step))
correct_prediction_transport = tf.equal(out_decision_transport, y_true_cls)
accuracy_transport = tf.reduce_mean(tf.cast(correct_prediction_transport, tf.float32))



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

    #PARTIE DE TRAIN IMPORTANTE
cross_entropy_city= tf.nn.softmax_cross_entropy_with_logits(logits = logits_city,
                                                        labels=y_true)
cost_city= tf.reduce_mean(cross_entropy_city)

optimizer_city= tf.train.AdagradOptimizer(learning_rate).minimize(cost_city,var_list=[first_biases_city,  snd_biases_city,  third_biases_city ,last_biases_city,first_weights_city,snd_weights_city,third_weights_city,last_weights_city])
#optimizer_city=(tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_city, global_step=global_step))
correct_prediction_city= tf.equal(out_decision_city, y_true_cls)
accuracy_city= tf.reduce_mean(tf.cast(correct_prediction_city, tf.float32))


# Best validation accuracy seen so far.
best_validation_accuracy = 0.0
saver = tf.train.Saver()
#save_dir = 'checkpoints/'
#if not os.path.exists(save_dir):
#    os.makedirs(save_dir)
#save_path = os.path.join(save_dir, 'best_validation')
checkpoint_dir = "checkpoint"
def save(checkpoint_dir,global_step=None):
        print(" [*] Saving checkpoints...")
        model_name = "best_validations"
        model_dir = "checkpoints"
        checkpoint_dir = os.path.join(checkpoint_dir, model_dir)
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
#            saver.save(session, os.path.join(checkpoint_dir, model_name), global_step=global_step)
        print(os.path.join(checkpoint_dir, model_name))
        r = saver.save(session, os.path.join(checkpoint_dir, model_name), global_step=global_step)
        print (r)


session = tf.Session()
session.run(tf.global_variables_initializer())

def optimize():

    global best_validation_accuracy
    for w in range(1):
        j = 0
        print ("Bloc %d" %w)
        for j in range(len(maps_global)) :
            i = 0
            print ("Partie %d en cours de test"%j)
    #        print (session.run(first_weights_terre))
            lamaps = maps_global[j]
            far_contexts = far_contexts_global[j]
            even_further_contexts = even_further_contexts_global[j]
            decisions = decisions_global[j]
            decisions_piece_type = decisions_piece_type_global[j]
            for i in range(len(lamaps)):
                #print ("Je train le coup %d" %i)
                mape = lamaps[i]
                far_context = far_contexts[i]
                even_further_context = even_further_contexts[i]
                tab_context_far = far_context.split()
                tab_context_further = even_further_context.split()
                tab_mape = mape.split()
                tab_float = np.zeros(len(tab_mape))
                for j in range(len(tab_mape)):
                    tab_float[j] = ord(tab_mape[j])
                tab_float = concat_tab(tab_float,tab_context_far,tab_context_further)
                decision = decisions[i]
                decision_piece_type = decisions_piece_type[i]
                if decision_piece_type == ARMY :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                    feed_dict_train = {input_layer_terre: tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_terre, feed_dict=feed_dict_train)



                if decision_piece_type == FLIGHT :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                    feed_dict_train = {input_layer_flight: tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_flight, feed_dict=feed_dict_train)

                if decision_piece_type == BOAT :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                    feed_dict_train = {input_layer_boat : tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_boat, feed_dict=feed_dict_train)

                if decision_piece_type == CITY :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                    feed_dict_train = {input_layer_city : tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_city, feed_dict=feed_dict_train)

                if decision_piece_type == TRANSPORT :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                    feed_dict_train = {input_layer_transport : tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_transport, feed_dict=feed_dict_train)
                if decision_piece_type == PATROL :
                    decision_tab = np.zeros((1,7))
                    decision_tab[0][decision] = 1
                    feed_dict_train = {input_layer_patrol : tab_float,
                                   y_true: decision_tab}
                    session.run(optimizer_patrol, feed_dict=feed_dict_train)

            acc_validation, _ = validation_accuracy()
          #  print (acc_validation)
            if acc_validation > best_validation_accuracy:
                best_validation_accuracy = acc_validation
                print ("NOUVELLE SAUVEGARDE -------------------------------------------------------")
                print (best_validation_accuracy)
                print ("---------------------------------------------------------------------------")
#                saver.save(sess=session, save_path=save_path)
                save(checkpoint_dir,None)
                w = session.run(first_weights_terre)
                wmin = np.min(w)
                wmax = np.max(w)
                print (wmin)
                print(wmax)

    print(best_validation_accuracy)

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
    c7 = np.zeros(len(c1))
    for i in range(len(c1)) :
        c3 = c1[i]
        c4 = c2[i]
        if not(isinstance(c4,int)) :
            preci2 = c4
        else :
            preci2 = c4[0]
        preci1 = np.argmax(c3)
#        print(preci1)
#        print (preci2)
#        print("-----------------------------------------------------------------")
#
        if preci1 == preci2 :
            c7[i] =1
#    print (c7)
    return c7


def predict_cls_validation(zemaps_train,zedecisions_train,zedecisions_piece_type_train,zefar_contexts_train,zeeven_further_contexts_train):
    return predict_cls(zemaps = zemaps_train,
                       zelabels = zedecisions_train,
                       zedecisions = zedecisions_train,
                       zedecisions_piece_type = zedecisions_piece_type_train,
                       zefar_contexts = zefar_contexts_train,
                       zeeven_further_contexts = zeeven_further_contexts_train)

def create_label_test(zedecisions):
    labels_create = len(zedecisions) *[0]
    for i in range(len(zedecisions)):
        zedecision = zedecisions[i]
        zedecision_tab = np.zeros((1,7))
        zedecision_tab[0][zedecision] = 1
        for j in range(len(zedecision_tab)):
            labels_create[i] = zedecision_tab
    return labels_create


def predict_cls(zemaps, zelabels, zedecisions, zedecisions_piece_type,zefar_contexts,zeeven_further_contexts):
    nb_maps = len(zemaps)
    decision_tab = create_label_test(zedecisions)
#    print (nb_maps)
    cls_pred = np.zeros(nb_maps)
    terre_pred  = np.zeros(nb_maps)
    terre_dec = np.zeros(nb_maps)
    indice_terre = 0
    for i in range(nb_maps):
        zedecision_piece_type = zedecisions_piece_type[i]
        zefar_context = zefar_contexts[i]
        zeeven_further_context = zeeven_further_contexts[i]
        zemape = zemaps[i]
        tab_context_far = zefar_context.split()

        tab_context_further = zeeven_further_context.split()
        tab_mape = zemape.split()
        tab_float_map = np.zeros(len(tab_mape))
        for j in range(len(tab_mape)):
            tab_float_map[j] = ord(tab_mape[j])
        #print (tab_float_map)
        tab_float = concat_tab(tab_float_map,tab_context_far,tab_context_further)
        #print (tab_float)
        if zedecision_piece_type == ARMY :

            feed_dict_train = {input_layer_terre: tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_terre, feed_dict=feed_dict_train)
#            print (cls_pred)
            terre_pred[indice_terre] = cls_pred[i]
            terre_dec[indice_terre] = np.argmax(decision_tab[i])
            indice_terre = indice_terre +1

        elif zedecision_piece_type == FLIGHT :
            feed_dict_train = {input_layer_flight: tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_flight, feed_dict=feed_dict_train)
        elif zedecision_piece_type == BOAT :
            feed_dict_train = {input_layer_boat : tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_boat, feed_dict=feed_dict_train)
        elif zedecision_piece_type == CITY :
            feed_dict_train = {input_layer_city : tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_city, feed_dict=feed_dict_train)

        elif zedecision_piece_type == TRANSPORT :
            feed_dict_train = {input_layer_transport : tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_transport, feed_dict=feed_dict_train)
        elif zedecision_piece_type == PATROL :
            feed_dict_train = {input_layer_patrol : tab_float,
                                   y_true: decision_tab[i]}
            cls_pred[i] = session.run(out_decision_patrol, feed_dict=feed_dict_train)
        else :
            cls_pred[i] = np.array(["C MOR"]) #Test au cas ou unité incorrecte
#    print (cls_pred)
    correct = test_egalite(decision_tab,cls_pred)
#    terre_final  =test_egalite(terre_dec,terre_pred)
##    print (terre_final)
#    test_terre_final = 0
#    for t in range (len(terre_final)):
#        if terre_final[t] ==1 :
#            test_terre_final = test_terre_final +1
#    terre_final_somme = test_terre_final / len(terre_final)
#    print (terre_final_somme)
    return correct, cls_pred


def cls_accuracy(tableau):

    somme = 0
    nb_map = 0
    for i in range (len(tableau)) :
        tabresu = tableau[i]
        for j in range (len(tabresu)):
            somme = somme + tabresu[i]
            nb_map = nb_map + 1
    acc = float(somme) / nb_map
    return acc, somme

def validation_accuracy():
    i =0
    resultat_tab = len(maps_train) * [0]
    for i in range(len(maps_train)) :
#        print ("TRAIN %d en cours d'execution !!"%i)
        correct, _ = predict_cls_validation(maps_train[i],decisions_train[i],decisions_piece_type_train[i],far_contexts_train[i],even_further_contexts_train[i])
        resultat_tab[i] = correct
    return cls_accuracy(resultat_tab)

def load(checkpoint_dir):

    print(" [*] Loading checkpoints...")
    model_dir = "checkpoints"
    checkpoint_dir = os.path.join(checkpoint_dir, model_dir)
    ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
    if ckpt and ckpt.model_checkpoint_path:
        ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
        saver.restore(session, os.path.join(checkpoint_dir, ckpt_name))
        print(" [*] Load SUCCESS : %s" %os.path.join(checkpoint_dir, ckpt_name))
        return True
    else:
        print(" [!] Load failed...")
        return False

optimize()
w = session.run(first_weights_terre)
wmin = np.min(w)
wmax = np.max(w)
print (wmin)
print(wmax)
#saver.restore(sess=session, save_path=save_path)
#load(checkpoint_dir)
w = session.run(first_weights_terre)
wmin = np.min(w)
wmax = np.max(w)
print (wmin)
print(wmax)

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
