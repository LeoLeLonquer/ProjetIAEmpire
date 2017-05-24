#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:00:48 2017

@author: Nathan Balblanc and Yacine Smini
"""

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



first_size = 37
possible_actions = 7
first_hidden_layers_size_terrestre = 48
snd_hidden_layers_size_terrestre = 48
learning_rate = 0.001

#Definition des reseaux des neurones pour unités terrestres
def init_layer_terrestre():
	# network weights
    first_weights_terre = tf.Variable(tf.zeros([fist_size, first_hidden_layers_size_terrestre]))
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
    logits_terre = tf.matmul(snd_layer_terrer, last_weights_terre) + last_biases_terre #matrice de poids non remis entre 0 et 1 IL faut une logits[1;7]
    out_layer_terre = tf.nn.softmax(logits_terre) #Matrice avec les probabilités entre 0 et 1 dont la somme vaut 1
    out_decision_terre = tf.argmax(out_layer_terre, dimension=1) #Choix final de mouvement 
      




first_hidden_layers_size_flight = 42
snd_hidden_layers_size_flight = 42  
#Definition des reseaux des neurones pour unités Volantes
def init_layer_flight():
	# network weights
    first_weights_flight = tf.Variable(tf.zeros([fist_size, first_hidden_layers_size_flight]))
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
def init_layer_boat():
	# network weights
    first_weights_boat = tf.Variable(tf.zeros([fist_size, first_hidden_layers_size_boat]))
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
first_size = 37
possible_actions = 7
first_hidden_layers_size_city = 5 #TODO : A remplacer par le bon nombre de pocibilité
snd_hidden_layers_size_city = 5
learning_rate = 0.001
def init_layer_city() :
    
    
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
       
def init_layer() : 
    init_layer_boat()
    init_layer_flight()
    init_layer_terrestre()
    init_layer_city()
    

        
        
def main() : 
       		
    #Creation variable pour l'initialisation du reseau ensuite
    step = tf.Variable(0, trainable=False)
    one = tf.constant(1)
    new_value = tf.add(step, one)
    update_step = tf.assign(step, new_value)
        
   
    tf.initialize_all_variables().run()
    init = tf.initialize_all_variables()
        
    with tf.Session() as sess:
        #Init de tous les reseaux de neurones
        sess.run(init_layer)
        #Init du step a 0
        sess.run(step.assign(0))
    
        
		
		
        
        
        

               
        