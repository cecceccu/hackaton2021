from numpy.core.fromnumeric import prod
import pygame
import matplotlib
import matplotlib.pyplot as plt
import random
from pygame import draw

from pygame.constants import KEYDOWN
import excelLoader
import numpy as np
import slider

from groupe_production import Groupe_Production
from point_production import Point_Production
from point_conso import Point_conso
from ligne import Ligne


matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

fig = pylab.figure(figsize=[8, 6], # Inches
                   dpi=50,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
fig2 = pylab.figure(figsize=[8, 6], # Inches
                   dpi=50,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )

drawn = False
points = []
listeroutes2=[]
listeroutes=[]
nbReseau=0
selected2=[]
list_reseau= {nbReseau: points}
lignes = []
selected=0
selecroute=0
game_speed = 10

x_window = 1050
y_window = 700

color = (255, 0, 0)

blue = (0, 0, 255)
SCENE = "admin"

pygame.init()
nbClick=0
nbProd=0
nbRoute = 0
list_route={}
moving = False
list_prod = {}
list_conso = {}
boutons_villes = []
value_text_name = ''
value_text_pourcentage = ''
name = ''
pourcentage = 0
nameExist = False
pourcentageExist = False
i_conso = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((x_window, y_window))
done = False
bg = pygame.image.load("corse.png").convert()
data = excelLoader.load_excel("Fichier-source.csv")
del data[0]
for i in range(-9, 1):
        data[i] = {"charge":"0", "date_heure": "                         ", "renouvelable":"0"}

ax = fig.gca()
ax2 = fig2.gca()
canvas = agg.FigureCanvasAgg(fig)
canvas2 = agg.FigureCanvasAgg(fig2)

speed_slider = slider.Slider((30, 30))

points_production = []
boutons_groupes = []


rect = pygame.Rect(30,30,200, 100)
slider_surface = pygame.Surface(rect.size)

screen.blit(bg, ((x_window/4)+20,0))

renouvelable = []
list_prod_totale = [0]*10
list_prod_renouvelable = [0]*10
PAUSED = False

value_text=''
active = 0
selected_object = None
selected_conso = None
prod_active=False
rect_obj = None
prod_totale=0
prod_renouvelable=0
nbConso=0
while not done:
        if SCENE == "player":
                for event in pygame.event.get():
                        
                        pygame.draw.rect(slider_surface, (255,255,255), slider_surface.get_rect())
                        screen.blit(slider_surface, rect)
                        speed_slider.render(screen)
                        speed_slider.changeValue()
                        screen.blit(bg, (x_window, y_window))
                        game_speed = speed_slider.getValue()              
                        if event.type == pygame.QUIT:
                                done = True

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p: 
                                        PAUSED = True
                                if event.key == pygame.K_s: 
                                        PAUSED = False
                        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                
                                for key, value in list_prod.items():
                                        if value.rect.collidepoint(event.pos):
                                                selected_object = value
                                                active = value.on
                                                text  = pygame.font.SysFont("timesnewroman", 15).render("Centrale : " + str(selected_object.nom), True, (0,0,0,0))
                                                pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(0, 200, x_window/4, y_window))
                                                rect_obj = pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(0, 200, x_window/4, 50))
                                                text_rect = text.get_rect(center=rect_obj.center)
                                                screen.blit(text, text_rect)
                                                rect_obj = pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(0, 400, x_window/4, 50))
                                                text  = pygame.font.SysFont("timesnewroman", 15).render("Capacité de production : " + str(selected_object.capacite), True, (0,0,0,0))
                                                text_rect = text.get_rect(center=rect_obj.center)
                                                screen.blit(text, text_rect)

                                                if active:
                                                        rect_obj = pygame.draw.rect(screen, (0,255,0), pygame.Rect(x_window/9, 500, x_window/16, 50))
                                                        text  = pygame.font.SysFont("timesnewroman", 15).render("On", True, (0,0,0,0))
                                                        text_rect = text.get_rect(center=rect_obj.center)
                                                        screen.blit(text, text_rect)
                                                else:
                                                        rect_obj = pygame.draw.rect(screen, (255,0,0), pygame.Rect(x_window/9, 500, x_window/16, 50))
                                                        text  = pygame.font.SysFont("timesnewroman", 15).render("Off", True, (0,0,0,0))
                                                        text_rect = text.get_rect(center=rect_obj.center)
                                                        screen.blit(text, text_rect)   
                                        

                                if (rect_obj and rect_obj.collidepoint(event.pos)):
                                        selected_object.switch_state()
                                        if selected_object.on:
                                                rect_obj = pygame.draw.rect(screen, (0,255,0), pygame.Rect(x_window/9, 500, x_window/16, 50))
                                                text  = pygame.font.SysFont("timesnewroman", 15).render("On", True, (0,0,0,0))
                                                text_rect = text.get_rect(center=rect_obj.center)
                                                screen.blit(text, text_rect)
                                        else:
                                                rect_obj = pygame.draw.rect(screen, (255,0,0), pygame.Rect(x_window/9, 500, x_window/16, 50))
                                                text  = pygame.font.SysFont("timesnewroman", 15).render("Off", True, (0,0,0,0))
                                                text_rect = text.get_rect(center=rect_obj.center)
                                                screen.blit(text, text_rect)   
                                        prod_totale = sum([obj.capacite for obj in list_prod.values() if obj.on])
                                        prod_renouvelable = sum([obj.capacite for obj in list_prod.values() if obj.on and obj.categorie != "thermique"])

                                        print(prod_totale)
                clock.tick(game_speed)






                                                


                                
                    
                if not PAUSED:
                        ax.clear()
                        ax2.clear()
                        y = np.array([0,50,100,150,200,250,300])
                                
                        items = [data[k] for k in sorted(data.keys())[:10]]
                        charges = np.array([float(val['charge'].replace('"', '')) for val in items])
                        renouvelable = np.array([float(val['renouvelable'].replace('"', '')) for val in items])
                        
                        # if len(production) >=10:
                        #         production = production[1:]
                        # prod = sum([p.capacite for p in points_production])
                        # production = np.append(production, prod)

                        if len(list_prod_totale)>=10:
                                list_prod_totale= list_prod_totale[1:]
                                list_prod_totale.append(prod_totale)

                        if len(list_prod_renouvelable)>=10:
                                list_prod_renouvelable = list_prod_renouvelable[1:]
                                list_prod_renouvelable.append(prod_renouvelable)

                        x = np.array([val['date_heure'].replace('"', '')[-5:] for val in items])
                        ax.set_ylim([0, 300])
                        min_key = min(data.keys())
                        ax.set_title("Consommation " + str(items[0]['date_heure'])[:-6].replace('"', ''))
                        ax.plot(x, charges, label="Consommation globale")

                        if len(list_prod_totale)==10:
                                ax.plot(x, list_prod_totale, label="Production globale")

                        print(renouvelable)
                        ax2.set_ylim([0, 150])

                        ax2.set_title("Production issue des énergies renouvelables")
                        ax2.plot(x, renouvelable, label="Imposée")

                        if len(list_prod_renouvelable)==10:
                                ax2.plot(x, list_prod_renouvelable, label="Actuelle")
                        ax.legend()
                        ax2.legend()

                        
                        canvas.draw()
                        renderer = canvas.get_renderer()
                        raw_data = renderer.tostring_rgb()
                        size = canvas.get_width_height()        
                        graph = pygame.image.fromstring(raw_data, size, "RGB")
                        screen.blit(graph, (650,0))

                        canvas2.draw()
                        renderer2 = canvas2.get_renderer()
                        raw_data2 = renderer2.tostring_rgb()
                        size2 = canvas2.get_width_height()        
                        graph2 = pygame.image.fromstring(raw_data2, size2, "RGB")
                        screen.blit(graph2, (650,300))
                        
                        data.pop(min_key)
                        pygame.display.flip()
                else:
                        pygame.display.flip()
                
                
        
        elif SCENE == "admin":
                for ev in pygame.event.get():
                        screen.blit(bg, (x_window, y_window))
                        if ev.type == pygame.QUIT:
                                pygame.quit()
                        # Drawing Rectangle
                        #c origine, y origine, largeur, longueur
                        pygame.draw.rect(screen, color, pygame.Rect(0, 0, x_window/4, y_window))
                        eolien =  pygame.draw.rect(screen, blue, pygame.Rect(10, 10, ((x_window/4) - 20), 50 ))
                        thermique = pygame.draw.rect(screen, blue, pygame.Rect(10, 70, ((x_window / 4) - 20), 50))
                        photovoltaique = pygame.draw.rect(screen, blue, pygame.Rect(10, 130, ((x_window / 4) - 20), 50))
                        hydrolique = pygame.draw.rect(screen, blue, pygame.Rect(10, 190, ((x_window / 4) - 20), 50))
                        biogaz = pygame.draw.rect(screen, blue, pygame.Rect(10, 250, ((x_window / 4) - 20), 50))
                        pointDeConso = pygame.draw.rect(screen, blue, pygame.Rect(10, 310, ((x_window / 4) - 20), 50))
                        route = pygame.draw.rect(screen, blue, pygame.Rect(10, 370, ((x_window / 4) - 20), 50))
                        delete = pygame.draw.rect(screen, blue, pygame.Rect(10, 430, ((x_window / 4) - 20), 50))
                        changescene = pygame.draw.rect(screen, blue, pygame.Rect(10, 490, ((x_window / 4) - 20), 50))
                        
                        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button!= 3:
                                for key, value in list_prod.items():
                                        if value.rect.collidepoint(ev.pos): 
                                                selected_object = value
                                                text  = pygame.font.SysFont("timesnewroman", 15).render("Nom de la centrale", True, (0,0,0,0))
                                                pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                                rect_obj1 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                                text_rect = text.get_rect(center=rect_obj1.center)
                                                screen.blit(text, text_rect)
                                                text  = pygame.font.SysFont("timesnewroman", 15).render("Ajouter un groupe de production", True, (0,0,0,0))
                                                rect_obj2 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                                text_rect = text.get_rect(center=rect_obj2.center)
                                                screen.blit(text, text_rect)
                                                rect_obj3 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 350, x_window/4, 50))
                                                text_rect = text.get_rect(center=rect_obj3.center)
                                                screen.blit(text, text_rect)
                                                rect_obj4 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 450, x_window/4, 50))
                                                text_rect = text.get_rect(center=rect_obj4.center)
                                                screen.blit(text, text_rect)
                                                rect_obj5 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 550, x_window/4, 50))
                                                text_rect = text.get_rect(center=rect_obj5.center)
                                                screen.blit(text, text_rect)

                                                boutons_groupes = [rect_obj1, rect_obj2, rect_obj3, rect_obj4, rect_obj5]

                                                



                                for (i, bouton) in enumerate(boutons_groupes):
                                        if bouton.collidepoint(ev.pos):
                                                if i == 0:
                                                        pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                                        active = 1
                                                elif i== 1:
                                                        if 1 in selected_object.groupes:
                                                                selected_object.remove_group(1)
                                                        pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                                        active = 2
                                                elif i== 2:
                                                        if 2 in selected_object.groupes:
                                                                selected_object.remove_group(2)
                                                        pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 350, x_window/4, 50))
                                                        active = 3
                                                elif i== 3:
                                                        if 3 in selected_object.groupes:
                                                                selected_object.remove_group(3)
                                                        pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 450, x_window/4, 50))
                                                        active = 4
                                                elif i== 4:
                                                        if 4 in selected_object.groupes:
                                                                selected_object.remove_group(4)
                                                        pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 550, x_window/4, 50))
                                                        active = 5
                        if ev.type == pygame.KEYDOWN:
                                if active == 1:
                                        string_format = "Nom de la centrale : "
                                        if ev.key == pygame.K_RETURN:
                                                selected_object.nom = value_text
                                                print(selected_object.nom)
                                                value_text = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text = value_text[:-1]
                                        else:
                                                value_text += ev.unicode
                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj1.center)
                                        if value_text!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                        screen.blit(font_text, text_rect)
                                elif active == 2:
                                        string_format = "Capacité : "
                                        if ev.key == pygame.K_RETURN:
                                                selected_object.add_group(1, Groupe_Production(int(value_text)))
                                                print(selected_object.capacite)
                                                value_text = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text = value_text[:-1]
                                        else:
                                                value_text += ev.unicode
                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj2.center)
                                        if value_text!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                        screen.blit(font_text, text_rect)
                                elif active == 3:
                                        string_format = "Capacité : "
                                        if ev.key == pygame.K_RETURN:
                                                selected_object.add_group(2, Groupe_Production(int(value_text)))
                                                print(selected_object.capacite)
                                                value_text = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text = value_text[:-1]
                                        else:
                                                value_text += ev.unicode
                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj3.center)
                                        if value_text!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 350, x_window/4, 50))
                                        screen.blit(font_text, text_rect)
                                elif active == 4:
                                        string_format = "Capacité : "
                                        if ev.key == pygame.K_RETURN:
                                                selected_object.add_group(3, Groupe_Production(int(value_text)))
                                                print(selected_object.capacite)
                                                value_text = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text = value_text[:-1]
                                        else:
                                                value_text += ev.unicode

                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj4.center)

                                        if value_text!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 450, x_window/4, 50))
                                        screen.blit(font_text, text_rect)
                                elif active == 5:
                                        string_format = "Capacité : "
                                        if ev.key == pygame.K_RETURN:
                                                selected_object.add_group(4, Groupe_Production(int(value_text)))
                                                print(selected_object.capacite)
                                                value_text = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text = value_text[:-1]
                                        else:
                                                value_text += ev.unicode
                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj5.center)

                                        if value_text!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 550, x_window/4, 50))
                                        screen.blit(font_text, text_rect)

                
                        if ev.type == pygame.MOUSEBUTTONDOWN :
                        #if select 1->eolienne, 2->thermique, 3->photovoltaique, 4->hydraulique, 5->biogaz


                                if ev.button!=3:
                                        if nbClick == 1:
                                                if selected == 1 and pygame.mouse.get_pos()[0]>x_window/4:
                                                        print(1)
                                                        image_file = "eolienne.png"
                                                        image = pygame.image.load(image_file).convert_alpha()
                                                        screen.blit(image, pygame.mouse.get_pos())
                                                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                                                        nbProd+=1

                                                        list_prod[nbProd] = Point_Production("eolienne", pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 41, 42), 1))
                                                        nbClick+=1
                                                if selected == 2 and pygame.mouse.get_pos()[0]>x_window/4:
                                                        print(2)
                                                        image_file = "thermique.png"
                                                        image = pygame.image.load(image_file).convert_alpha()
                                                        screen.blit(image, pygame.mouse.get_pos())
                                                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                                                        nbProd+=1
                                                        list_prod[nbProd] = Point_Production("thermique", pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 50, 41), 1))
                                                        nbClick+=1
                                                if selected == 3 and pygame.mouse.get_pos()[0]>x_window/4:
                                                        print(3)
                                                        image_file = "photovoltaique.png"
                                                        image = pygame.image.load(image_file).convert_alpha()
                                                        screen.blit(image, pygame.mouse.get_pos())
                                                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                                                        nbProd+=1
                                                        list_prod[nbProd] = Point_Production("photovoltaique", pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 33), 1))
                                                        nbClick+=1
                                                if selected == 4 and pygame.mouse.get_pos()[0]>x_window/4:
                                                        print(4)
                                                        image_file = "hydraulique.png"
                                                        image = pygame.image.load(image_file).convert_alpha()
                                                        screen.blit(image, pygame.mouse.get_pos())
                                                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                                                        nbProd+=1
                                                        list_prod[nbProd] = Point_Production("hydraulique", pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 63, 32), 1))
                                                        nbClick+=1
                                                if selected == 5 and pygame.mouse.get_pos()[0]>x_window/4:
                                                        print(5)
                                                        image_file = "biogaz.png"
                                                        image = pygame.image.load(image_file).convert_alpha()
                                                        screen.blit(image, pygame.mouse.get_pos())
                                                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                                                        nbProd+=1
                                                        list_prod[nbProd] = Point_Production("biogaz", pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 32), 1))
                                                        nbClick+=1
                                                if selected == 7 and pygame.mouse.get_pos() > (x_window/4, y_window):
                                                        print(7)
                                                        ###Création des paramètres de conso
                                                        text  = pygame.font.SysFont("timesnewroman", 15).render("Nom de la ville", True, (0,0,0,0))
                                                        text2  = pygame.font.SysFont("timesnewroman", 15).render("Pourcentage de conso", True, (0,0,0,0))



                                                        if (not nameExist and not pourcentageExist):
                                                                pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                                                rect_obj1 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                                                text_rect = text.get_rect(center=rect_obj1.center)
                                                                screen.blit(text, text_rect)
                                                                rect_obj2 = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                                                text_rect = text2.get_rect(center=rect_obj2.center)
                                                                screen.blit(text2, text_rect)
                                                
                                                        boutons_villes = [rect_obj1, rect_obj2]

                                                        for (i, bouton) in enumerate(boutons_villes):
                                                                if bouton.collidepoint(ev.pos):
                                                                        if i == 0:
                                                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                                                                active = 6
                                                                        elif i== 1:
                                                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                                                                active = 7
                                                        if(i_conso==0):
                                                                image_file = "conso.png"
                                                                image = pygame.image.load(image_file).convert_alpha()
                                                                screen.blit(image, pygame.mouse.get_pos())
                                                                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                                                                nbConso+=1
                                                                list_conso[nbConso] = Point_conso(rect = pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 32), 1))
                                                                i_conso+=1

                                        if eolien.collidepoint(ev.pos):
                                                nbClick = 0
                                                selected = 1
                                                nbClick += 1
                                        if thermique.collidepoint(ev.pos):
                                                nbClick = 0
                                                selected = 2
                                                nbClick += 1
                                        if photovoltaique.collidepoint(ev.pos):
                                                nbClick = 0
                                                selected = 3
                                                nbClick += 1
                                        if hydrolique.collidepoint(ev.pos):
                                                nbClick = 0
                                                selected = 4
                                                nbClick += 1
                                        if biogaz.collidepoint(ev.pos):
                                                nbClick = 0
                                                selected = 5
                                                nbClick += 1
                                        if route.collidepoint(ev.pos):
                                                nbClick = 0
                                                selected = 6
                                                nbReseau+=1
                                                list_reseau[nbReseau]=[]
                                                nbClick+=1
                                        if pointDeConso.collidepoint(ev.pos):
                                                print('A')
                                                nbClick = 0
                                                selected = 7
                                                nbClick+=1
                                        if route.collidepoint(ev.pos):
                                                if (len(points) >= 2):
                                                        points.pop()
                                        if delete.collidepoint(ev.pos):
                                                selected = 8
                                        if changescene.collidepoint(ev.pos):
                                                pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(0, 0, x_window/4, y_window))
                                                pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                                selected_object = None
                                                SCENE = "player"
                                        for key, value in list_prod.items():
                                                print(list_prod)
                                                if selected==8:
                                                        if value.rect.collidepoint(ev.pos):
                                                                del list_prod[key]
                                                                pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                                                pygame.draw.rect(screen, (255,255,255,255), value)
                                                                break
                                                
                                                
                                
                                        for key, value in list_conso.items():
                                                if selected==8:
                                                        if value.rect.collidepoint(ev.pos):
                                                                del list_conso[key]
                                                                pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                                                pygame.draw.rect(screen, (255,255,255,255), value.rect)
                                                                break

                                else:
                                        for key, value in list_prod.items():
                                                
                                                if value.rect.collidepoint(ev.pos):
                                                        #pos = pygame.mouse.get_pos()
                                                        list_reseau[nbReseau].append(ev.pos)
                                                        list_reseau_prod= value
                                                                
                                        for key, value in list_conso.items():
                                                if value.rect.collidepoint(ev.pos):
                                                        #pos = pygame.mouse.get_pos()
                                                        list_reseau[nbReseau].append(ev.pos)
                                                        list_reseau_conso = value

                        if ev.type == pygame.KEYDOWN:
                                print('aaaa')
                                if active == 6:
                                        string_format = "Nom de la ville : "
                                        # if ev.key==13: #pygame.K_KP_ENTER:
                                        #         name = value_text_name
                                        #         print(name)
                                        #         nameExist = True
                                        #         value_text_name = ''
                                        #         string_format = ''
                                        if ev.key == pygame.K_RETURN:
                                                name = value_text_name
                                                print(name)
                                                nameExist = True
                                                value_text_name = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text_name = value_text_name[:-1]
                                        else:
                                                value_text_name += ev.unicode
                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text_name), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj1.center)
                                        if value_text_name!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                        screen.blit(font_text, text_rect)
                                elif active == 7:
                                        string_format = "Pourcentage de conso : "
                                        # if ev.key==13:#pygame.K_KP_ENTER:
                                        #         pourcentage = int(value_text_pourcentage)
                                        #         print(pourcentage)
                                        #         pourcentageExist = True
                                        #         value_text_pourcentage = ''
                                        #         string_format = ''
                                        if ev.key == pygame.K_RETURN:
                                                pourcentage = value_text_pourcentage
                                                print(pourcentage)
                                                pourcentageExist = True
                                                value_text_pourcentage = ''
                                                string_format = ''
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text_pourcentage = value_text_pourcentage[:-1]
                                        else:
                                                value_text_pourcentage += ev.unicode
                                        font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text_pourcentage), True, (0,0,0,0))
                                        text_rect = font_text.get_rect(center=rect_obj2.center)
                                        if value_text_pourcentage!="":
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                        screen.blit(font_text, text_rect)
                                        
                                if nameExist and pourcentageExist:
                                        list_conso[nbConso].nom = name
                                        list_conso[nbConso].pourcentage = pourcentage
                                        nbClick+=1
                                        nameExist = False
                                        pourcentageExist = False
                                        pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                        i_conso=0

                        if nbReseau in list_reseau and  len(list_reseau[nbReseau]) >= 2:
                                print("bbbbbb")
                                active = 9
                                if not drawn:
                                        pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                        drawn = True
                                rect_obj = pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 325, x_window/4, 50))
                                if ev.type == pygame.KEYDOWN:
                                        print("ccccc")
                                        string_format = "Capacité : "
                                        if ev.key == pygame.K_RETURN:
                                                capacite = int(value_text)
                                                value_text = ''
                                                string_format = ''
                                                drawn = False
                                                pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                                                prod = list_reseau_prod
                                                cons = list_reseau_conso
                                                nbRoute+=1
                                                list_route[nbRoute] = Ligne(reseau = pygame.draw.lines(screen, blue, False, list_reseau[nbReseau]), prod = prod, conso = cons, capacite=capacite)
                                                list_reseau= {}
                                                list_reseau[0] = []
                                                list_reseau[1] = []
                                                prod = None
                                                cons = None
                                                print(list_route[nbRoute])
                                        elif ev.key == pygame.K_BACKSPACE:
                                                value_text = value_text[:-1]
                                        else:
                                                value_text += ev.unicode
                                
                                
                                font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text), True, (0,0,0,0))
                                text_rect = font_text.get_rect(center=rect_obj.center)

                                if value_text!="":
                                        pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(3*x_window/4, 325, x_window/4, 50))
                                screen.blit(font_text, text_rect)

                                #my_rect = pygame.draw.rect(surface, blue, pygame.Rect(list_reseau[nbReseau][0][0],  list_reseau[nbReseau][0][1],
                                #abs(list_reseau[nbReseau][1][0] - list_reseau[nbReseau][0][0]), abs(list_reseau[nbReseau][1][1] - list_reseau[nbReseau][0][1])))
                                #0 = Prod, 1 = Conso
                                

                pygame.display.flip()