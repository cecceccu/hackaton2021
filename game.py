from numpy.core.fromnumeric import prod
import pygame
import matplotlib
import matplotlib.pyplot as plt
import random
import excelLoader
import numpy as np
import slider

from groupe_production import Groupe_Production
from point_production import Point_Production
from point_conso import Point_conso


matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

fig = pylab.figure(figsize=[8, 6], # Inches
                   dpi=50,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )


points = []
lignes=[]
game_speed = 10

x_window = 1050
y_window = 700

color = (255, 0, 0)

blue = (0, 0, 255)
SCENE = "admin"

pygame.init()
nbClick=0
nbProd=0
moving = False
list_prod = {}

clock = pygame.time.Clock()
screen = pygame.display.set_mode((x_window, y_window))
done = False
bg = pygame.image.load("corse.png").convert()
data = excelLoader.load_excel("Fichier-source.csv")
del data[0]
for i in range(-9, 1):
        data[i] = {"charge":"0", "date_heure": "                         ", "renouvelable":"0"}

ax = fig.gca()
canvas = agg.FigureCanvasAgg(fig)

speed_slider = slider.Slider((30, 30))

points_production = []


rect = pygame.Rect(30,30,200, 100)
slider_surface = pygame.Surface(rect.size)

screen.blit(bg, ((x_window/4)+20,0))

production = []
PAUSED = False
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
                                                text  = pygame.font.SysFont(<your font here>, <font size here>).render(<text>, True, <color>)
                                                pygame.draw.rect(screen, (255,255,255,255), pygame.Rect(0, 0, x_window/4, y_window))
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(0, 150, x_window/4, 50))
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(0, 250, x_window/4, 50))
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(0, 350, x_window/4, 50))
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(0, 450, x_window/4, 50))
                                                pygame.draw.rect(screen, (120,120,120,120), pygame.Rect(0, 550, x_window/4, 50))
                                
                        
                if not PAUSED:
                        ax.clear()
                        y = np.array([0,50,100,150,200,250,300])
                                
                        items = [data[k] for k in sorted(data.keys())[:10]]
                        charges = np.array([float(val['charge'].replace('"', '')) for val in items])
                        production = np.array([float(val['renouvelable'].replace('"', '')) for val in items])
                        # if len(production) >=10:
                        #         production = production[1:]
                        # prod = sum([p.capacite for p in points_production])
                        # production = np.append(production, prod)
                        x = np.array([val['date_heure'].replace('"', '')[-5:] for val in items])
                        ax.set_ylim([0, 300])
                        min_key = min(data.keys())
                        ax.set_title("Consommation " + str(items[0]['date_heure'])[:-6].replace('"', ''))
                        ax.plot(x, charges, label="Consommation globale")

                        print(production)
                        if len(production)==10:
                                ax.plot(x, production, label="Production globale")
                        ax.legend()
                        canvas.draw()
                        renderer = canvas.get_renderer()
                        raw_data = renderer.tostring_rgb()
                        size = canvas.get_width_height()        
                        graph = pygame.image.fromstring(raw_data, size, "RGB")
                        screen.blit(graph, (650,0))
                        
                        data.pop(min_key)
                        pygame.display.flip()
                else:
                        pygame.display.flip()
                
                clock.tick(game_speed)
        
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
                        
                
                        if ev.type == pygame.MOUSEBUTTONDOWN :
                        #if select 1->eolienne, 2->thermique, 3->photovoltaique, 4->hydraulique, 5->biogaz

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
                                        if (len(points) >= 2):
                                                points.pop()
                                if delete.collidepoint(ev.pos):
                                        selected = 8
                                if changescene.collidepoint(ev.pos):
                                        pygame.draw.rect(screen, (0,0,0,0), pygame.Rect(0, 0, x_window/4, y_window))
                                        SCENE = "player"
                                for key, value in list_prod.items():
                                        print(list_prod)
                                        if selected==8:
                                                if value.rect.collidepoint(ev.pos):
                                                        del list_prod[key]
                                                        pygame.draw.rect(screen, (255,255,255,255), value)
                                                        break
                                        else:
                                                if value.rect.collidepoint(ev.pos): 
                                                        moving = True
                                                        print("-")
                                                        print(key, value)
                                                        print("-")
                                        
                                                elif ev.type == pygame.MOUSEBUTTONUP:
                                                        moving = False
                                                        break

                                                elif ev.type == pygame.MOUSEMOTION and moving:
                                                        print("é")
                                                        pygame.value.rect.move_ip(ev.rel)
                                                        screen.blit(image, list_prod.get(key))
                                                        pygame.draw.rect(screen,blue, pygame.Rect(Mouse_x, Mouse_y, 47, 32))
                                                        pygame.display.update()

                                if len(points) >= 2:
                                        pygame.draw.lines(screen, blue, False, points)

                pygame.display.flip()