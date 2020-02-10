#!/usr/bin/python3
# Dominic Macias
# 1/28/2020

import pickle

class Reset:
    def __init__(self):
        games = {}
        
        datafile = open("game_lib.pickle", "wb")
        pickle.dump(games, datafile)
        datafile.close()