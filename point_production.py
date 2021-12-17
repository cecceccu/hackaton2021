import pygame



class Point_Production:
    def __init__(self, categorie, rect, groupes = {}):
        self.groupes = groupes
        self.rect = rect
        self.categorie = categorie
        self.capacite = 0
        self.nom = ""
        self.on = False

    def add_group(self, ind, groupe):
        self.groupes[ind] = groupe
        self.capacite = sum([groupe.capacite for groupe in self.groupes.values()])

    def remove_group(self, ind):
        del self.groupes[ind]
        self.capacite = sum([groupe.capacite for groupe in self.groupes.values()])

    def switch_state(self):
        self.on = not self.on