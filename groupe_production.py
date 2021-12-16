from typing import ChainMap
import pygame

class Groupe_Production:

    def __init__(self, capacite=0):
        self.capacite = capacite

    def set_capacite(self, capacite):
        self.capacite = capacite