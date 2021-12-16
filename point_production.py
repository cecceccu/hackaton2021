import pygame



class Point_Production:
    def __init__(self, categorie, rect, groupes = []):
        self.groupes = groupes
        self.rect = rect
        self.categorie = categorie
        self.capacite = 0

    def add_group(self, groupe):
        self.groupes.append(groupe)
        self.capacite = sum([groupe.capacite for groupe in self.groupes])