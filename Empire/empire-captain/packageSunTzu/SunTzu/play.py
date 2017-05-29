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

class Cerveau:

    def __init__(self):
        self.possible_actions = 7
        #DEF type unite
        #TODO : A CHANGER CECI EST POUR UN TRAIN DE TEST A CHANGER PAR LES VRAIES VALEURS
        self.ARMY = 0
        self.FLIGHT = 1
        self.TRANSPORT = 2
        self.PATROL = 3
        self.BOAT = 4
        self.CITY = -1

        #Info de Linear
        self.y_true = tf.placeholder(tf.float32, [None, self.possible_actions])
        self.y_true_cls = tf.placeholder(tf.int64, [None])


        self.first_size = 49
        self.possible_actions = 7
        self.first_hidden_layers_size_terrestre = 48
        self.snd_hidden_layers_size_terrestre = 48


        #Definition des reseaux des neurones pour unités terrestres

        	# network weights
        self.first_weights_terre = tf.Variable(tf.zeros([self.first_size, self.first_hidden_layers_size_terrestre]))
        self.first_biases_terre = tf.Variable(tf.zeros([self.first_hidden_layers_size_terrestre]))

        self.snd_weights_terre = tf.Variable(tf.zeros([self.first_hidden_layers_size_terrestre, self.snd_hidden_layers_size_terrestre]))
        self.snd_biases_terre = tf.Variable(tf.zeros([self.snd_hidden_layers_size_terrestre]))

        self.last_weights_terre = tf.Variable(tf.zeros([self.snd_hidden_layers_size_terrestre, self.possible_actions]))
        self.last_biases_terre = tf.Variable(tf.zeros([self.possible_actions]))

        	# input layer
        self.input_layer_terre = tf.placeholder(tf.float32, [None, self.first_size])#Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

        	# hidden layers
        self.first_layer_terre = tf.nn.relu(tf.matmul(self.input_layer_terre, self.first_weights_terre) + self.first_biases_terre) # sors [1;50] donc une val par neurones (50 neurones)
        self.snd_layer_terre = tf.nn.relu(tf.matmul(self.first_layer_terre, self.snd_weights_terre) + self.snd_biases_terre) #Prend une [1;50] et sors une [1;7]

            #out layers On n'a qu'un seul neurones de sorties
        self.logits_terre = tf.matmul(self.snd_layer_terre, self.last_weights_terre) + self.last_biases_terre #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
        self.out_layer_terre = tf.nn.softmax(self.logits_terre) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
        self.out_decision_terre = tf.argmax(self.out_layer_terre, dimension=1) #Choix final de mouvement



        self.first_hidden_layers_size_flight = 42
        self.snd_hidden_layers_size_flight = 42
        #Definition des reseaux des neurones pour unités Volantes
        	# network weights
        self.first_weights_flight = tf.Variable(tf.zeros([self.first_size, self.first_hidden_layers_size_flight]))
        self.first_biases_flight = tf.Variable(tf.zeros([self.first_hidden_layers_size_flight]))

        self.snd_weights_flight = tf.Variable(tf.zeros([self.first_hidden_layers_size_flight, self.snd_hidden_layers_size_flight]))
        self.snd_biases_flight = tf.Variable(tf.zeros([self.snd_hidden_layers_size_flight]))

        self.last_weights_flight = tf.Variable(tf.zeros([self.snd_hidden_layers_size_flight, self.possible_actions]))
        self.last_biases_flight = tf.Variable(tf.zeros([self.possible_actions]))

        	# input layer
        self.input_layer_flight = tf.placeholder(tf.float32, [None, self.first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

        	# hidden layers
        self.first_layer_flight = tf.nn.relu(tf.matmul(self.input_layer_flight, self.first_weights_flight) + self.first_biases_flight) # sors [1;50] donc une val par neurones (50 neurones)
        self.snd_layer_flight = tf.nn.relu(tf.matmul(self.first_layer_flight, self.snd_weights_flight) + self.snd_biases_flight) #Prend une [1;50] et sors une [1;7]

            #out layers On n'a qu'un seul neurones de sorties
        self.logits_flight = tf.matmul(self.snd_layer_flight, self.last_weights_flight) + self.last_biases_flight #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
        self.out_layer_flight = tf.nn.softmax(self.logits_flight) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
        self.out_decision_flight = tf.argmax(self.out_layer_flight, dimension=1) #Choix final de mouvement



        self.first_hidden_layers_size_boat = 30
        self.snd_hidden_layers_size_boat = 30
        #Definition des reseaux des neurones pour unités aquatiques

        	# network weights
        self.first_weights_boat = tf.Variable(tf.zeros([self.first_size, self.first_hidden_layers_size_boat]))
        self.first_biases_boat = tf.Variable(tf.zeros([self.first_hidden_layers_size_boat]))

        self.snd_weights_boat = tf.Variable(tf.zeros([self.first_hidden_layers_size_boat, self.snd_hidden_layers_size_boat]))
        self.snd_biases_boat = tf.Variable(tf.zeros([self.snd_hidden_layers_size_boat]))

        self.last_weights_boat = tf.Variable(tf.zeros([self.snd_hidden_layers_size_boat, self.possible_actions]))
        self.last_biases_boat = tf.Variable(tf.zeros([self.possible_actions]))

        	# input layer
        self.input_layer_boat = tf.placeholder(tf.float32, [None, self.first_size]) #Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

        	# hidden layers
        self.first_layer_boat = tf.nn.relu(tf.matmul(self.input_layer_boat, self.first_weights_boat) + self.first_biases_boat) # sors [1;50] donc une val par neurones (50 neurones)
        self.snd_layer_boat = tf.nn.relu(tf.matmul(self.first_layer_boat, self.snd_weights_boat) + self.snd_biases_boat) #Prend une [1;50] et sors une [1;7]

            #out layers On n'a qu'un seul neurones de sorties
        self.logits_boat = tf.matmul(self.snd_layer_boat, self.last_weights_boat) + self.last_biases_boat #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
        self.out_layer_boat = tf.nn.softmax(self.logits_boat) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
        self.out_decision_boat = tf.argmax(self.out_layer_boat, dimension=1) #Choix final de mouvement



        #CITY LAYER

        self.first_hidden_layers_size_city = 48 #TODO : A remplacer par le bon nombre de pocibilité
        self.snd_hidden_layers_size_city = 48

        #Definition des reseaux des neurones pour unités terrestres

        	# network weights
        self.first_weights_city = tf.Variable(tf.zeros([self.first_size, self.first_hidden_layers_size_city]))
        self.first_biases_city= tf.Variable(tf.zeros([self.first_hidden_layers_size_city]))

        self.snd_weights_city= tf.Variable(tf.zeros([self.first_hidden_layers_size_city, self.snd_hidden_layers_size_city]))
        self.snd_biases_city= tf.Variable(tf.zeros([self.snd_hidden_layers_size_city]))

        self.last_weights_city= tf.Variable(tf.zeros([self.snd_hidden_layers_size_city, self.possible_actions]))
        self.last_biases_city= tf.Variable(tf.zeros([self.possible_actions]))

        	# input layer
        self.input_layer_city= tf.placeholder(tf.float32, [None, self.first_size])#Prends en entrée une "carte" hexagonale 37 donc comporte 37 neurones

        	# hidden layers
        self.first_layer_city= tf.nn.relu(tf.matmul(self.input_layer_city, self.first_weights_city) + self.first_biases_city) # sors [1;50] donc une val par neurones (50 neurones)
        self.snd_layer_city= tf.nn.relu(tf.matmul(self.first_layer_city, self.snd_weights_city) + self.snd_biases_city) #Prend une [1;50] et sors une [1;7]

            #out layers On n'a qu'un seul neurones de sorties
        self.logits_city= tf.matmul(self.snd_layer_city, self.last_weights_city) + self.last_biases_city #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
        self.out_layer_city= tf.nn.softmax(self.logits_city) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
        self.out_decision_city= tf.argmax(self.out_layer_city, dimension=1) #Choix final de mouvement


        #Saver
        self.saver = tf.train.Saver()
        self.save_path = './empire-captain/packageSunTzu/SunTzu/checkpoints/best_validation'

        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())

        #on recharge les poids
        self.saver.restore(self.session, self.save_path)

    def concat_tab(self,tab1,tab2,tab3) :
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

    def jouer(self,tab_mape, type_unit, tab_context_far, tab_context_further):

        tab_float = len(tab_mape) *[0]
        for j in range(len(tab_mape)):
            tab_float[j] = ord(tab_mape[j])

        tab_float = concat_tab(tab_float,tab_context_far,tab_context_further)
        if type_unit == self.ARMY :
            feed_dict_run = {input_layer_terre : tab_float}
            out_decision =self.session.run(self.out_decision_terre, feed_dict=feed_dict_run)


        if type_unit == self.FLIGHT :
            feed_dict_run = {input_layer_flight : tab_float}
            out_decision = self.session.run(self.out_decision_flight, feed_dict=feed_dict_run)

        if type_unit == self.BOAT :
            feed_dict_run = {input_layer_boat : tab_float}
            out_decision = self.session.run(self.out_decision_boat, feed_dict=feed_dict_run)

        if type_unit == self.CITY :
            feed_dict_run = {input_layer_city : tab_float}
            out_decision = self.session.run(self.out_decision_city, feed_dict=feed_dict_run)

        return out_decision
