import pygame



class Point_conso:
    

    def __init__(self, nom="", pourcentage=0, total_conso=0, recu=0,  rect = pygame.Rect):
        self.nom = nom
        self.pourcentage = pourcentage
        
        self.conso = total_conso * pourcentage/100
        self.rect = rect
        self.recu = recu

    def set_conso(self, pourcentage, total_conso):
        self.conso = total_conso * pourcentage/100
        