from typing import ChainMap
import pygame


class Ligne:


    def __init__(self, prod = None, conso = None, capacite = 0, transit = 0):
        self.capacite = capacite
        self.prod = prod
        self.conso = conso
        self.transit = transit

    def set_prod(self, prod):
        self.prod = prod

    def set_conso(self, conso):
        self.conso = conso

    def set_capacite(self, capacite):
        self.capacite = capacite

    def set_transit(self, transit):

        if self.transit <= self.prod.capacite:
            self.transit = transit
        else:
            self.transit = self.prod.capacite

    def transport(self):

        return self.transit if self.prod.capacite < self.capacite else self.capacite