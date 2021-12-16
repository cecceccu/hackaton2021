import pygame



class Point_conso:
    

    def __init__(self, nom, pourcentage, total_conso):
        self.nom = nom
        self.pourcentage = pourcentage
        
        self.conso = total_conso * pourcentage/100

    def set_conso(self, pourcentage, total_conso):
        self.conso = total_conso * pourcentage/100
        