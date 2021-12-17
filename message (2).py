import pygame
import point_production
import point_conso
import groupe_production
from point_conso import Point_conso
from ligne import Ligne
from point_production import Point_Production
from groupe_production import Groupe_Production
listeroutes2=[]
listeroutes=[]
nbReseau=0
selected2=[]
x_window = 900
y_window = 750

points = []
liste_reseau= {nbReseau: points}
scene = 1

lignes = []
# Initializing Pygame
pygame.init()
selected=0

# Initializing surface
surface = pygame.display.set_mode((x_window, y_window))

# Initialing Color
color = (255, 0, 0)
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue = (0, 0, 255)
selecroute=0


bg = pygame.image.load("corse.png").convert()
nbClick = 0
nbProd = 0
surface.blit(bg, ((x_window / 4) + 20, 0))
moving = False
list_prod = {}

while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if scene ==1:


            # Drawing Rectangle
            # c origine, y origine, largeur, longueur
            pygame.draw.rect(surface, color, pygame.Rect(0, 0, x_window / 4, y_window))
            eolien = pygame.draw.rect(surface, blue, pygame.Rect(10, 10, ((x_window / 4) - 20), 50))
            thermique = pygame.draw.rect(surface, blue, pygame.Rect(10, 70, ((x_window / 4) - 20), 50))
            photovoltaique = pygame.draw.rect(surface, blue, pygame.Rect(10, 130, ((x_window / 4) - 20), 50))
            hydrolique = pygame.draw.rect(surface, blue, pygame.Rect(10, 190, ((x_window / 4) - 20), 50))
            biogaz = pygame.draw.rect(surface, blue, pygame.Rect(10, 250, ((x_window / 4) - 20), 50))
            pointDeConso = pygame.draw.rect(surface, blue, pygame.Rect(10, 310, ((x_window / 4) - 20), 50))
            route = pygame.draw.rect(surface, blue, pygame.Rect(10, 370, ((x_window / 4) - 20), 50))
            delete = pygame.draw.rect(surface, blue, pygame.Rect(10, 430, ((x_window / 4) - 20), 50))
            changescene = pygame.draw.rect(surface, blue, pygame.Rect(10, 490, ((x_window / 4) - 20), 50))

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #print("la sélection "+ str(selected))
                # if select 1->eolien, 2->thermique, 3->photovoltaique, 4->hydrolique, 5->biogaz

                if nbClick == 1:
                    if selected == 1:
                        #print("1")
                        image_file = "eolienne.png"
                        image = pygame.image.load(image_file).convert_alpha()
                        surface.blit(image, pygame.mouse.get_pos())
                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                        nbProd += 1
                        list_prod[nbProd] = Point_Production(
                            rect=pygame.draw.rect(surface, (255, 255, 255, 255), pygame.Rect(Mouse_x, Mouse_y, 41, 42),
                                                  1))
                        list_prod[nbProd] = Point_Production(rect=pygame.draw.rect(surface, (255, 255, 255, 255),
                                                             pygame.Rect(Mouse_x, Mouse_y, 41, 42), 1))
                        nbClick += 1
                    if selected == 2:
                       # print("2")
                        image_file = "thermique.png"
                        image = pygame.image.load(image_file).convert_alpha()
                        surface.blit(image, pygame.mouse.get_pos())
                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                        nbProd += 1
                        list_prod[nbProd] = Point_Production(rect=pygame.draw.rect(surface, (255, 255, 255, 255),
                                                             pygame.Rect(Mouse_x, Mouse_y, 50, 41), 1))
                        nbClick += 1
                    if selected == 3:
                        #print("3")
                        image_file = "photovoltaique.png"
                        image = pygame.image.load(image_file).convert_alpha()
                        surface.blit(image, pygame.mouse.get_pos())
                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                        nbProd += 1
                        list_prod[nbProd] = Point_Production(rect=pygame.draw.rect(surface, (255, 255, 255, 255),
                                                             pygame.Rect(Mouse_x, Mouse_y, 47, 33), 1))
                        nbClick += 1
                    if selected == 4:
                        #print("4")
                        image_file = "hydraulique.png"
                        image = pygame.image.load(image_file).convert_alpha()
                        surface.blit(image, pygame.mouse.get_pos())
                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                        nbProd += 1
                        list_prod[nbProd] = Point_Production(rect=pygame.draw.rect(surface, (255, 255, 255, 255),
                                                             pygame.Rect(Mouse_x, Mouse_y, 63, 32), 1))
                        nbClick += 1
                    if selected == 5:
                        #print("5")
                        image_file = "biogaz.png"
                        image = pygame.image.load(image_file).convert_alpha()
                        surface.blit(image, pygame.mouse.get_pos())
                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                        nbProd += 1
                        list_prod[nbProd] = Point_Production(rect=pygame.draw.rect(surface, (255, 255, 255, 255),
                                                             pygame.Rect(Mouse_x, Mouse_y, 47, 32), 1))
                        nbClick += 1

                        print("on est là héhé")

                        #print(selecroute)
                        if selecroute==0:
                            selecroute=1
                        else:
                            selecroute=0

                            if (len(points) >= 2):
                                points.pop()

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
                    nbReseau += 1
                    liste_reseau[nbReseau] = []
                    nbClick+=1

                    print("coucou les copaings")
                if changescene.collidepoint(ev.pos):
                    scene=2
                    print("on change de scene hophop")
                if delete.collidepoint(ev.pos):
                    selected = 8
                for key, value in list_prod.items():
                    #print(list_prod)
                    if selected == 8:
                        if value.rect.collidepoint(ev.pos):
                            del list_prod[key]
                            pygame.draw.rect(surface, (255, 255, 255, 255), value)
                            break
                    elif selected == 6:
                        if value.rect.collidepoint(ev.pos):
                            print("coucou les copains")
                            pos = pygame.mouse.get_pos()
                            liste_reseau[nbReseau].append(ev.pos)
                    else:
                        if value.rect.collidepoint(ev.pos):
                            moving = True
                            #print("-")
                           # print(key, value)
                           # print("-")

                        elif ev.type == pygame.MOUSEBUTTONUP:
                            moving = False
                            break

                        elif ev.type == pygame.MOUSEMOTION and moving:
                            #print("é")
                            pygame.value.move_ip(ev.rel)
                            surface.blit(image, list_prod.get(key))
                            pygame.draw.rect(surface, blue, pygame.Rect(Mouse_x, Mouse_y, 47, 32))
                            pygame.display.update()

            if len(liste_reseau[nbReseau]) >= 2:
                listeroutes.append(Ligne(point1=liste_reseau[nbReseau][0],point2=liste_reseau[nbReseau][1]))
                pygame.draw.lines(surface, blue, False, liste_reseau[nbReseau])
              #  print(listeroutes[nbReseau-1])


            pygame.display.flip()
        elif scene == 2 :
            pygame.draw.rect(surface, black, pygame.Rect(0, 0, x_window / 4, y_window))
            pygame.display.flip()


            if ev.type == pygame.MOUSEBUTTONDOWN:
                if (ev.button)==1:
                    for key, value in list_prod.items():
                        if value.rect.collidepoint(ev.pos):

                            stats = pygame.draw.rect(surface, green, pygame.Rect(value.rect.x, value.rect.y - 50,100,50))
                            off= pygame.draw.rect(surface, blue, pygame.Rect(value.rect.x , value.rect.y - 30,20,20))
                            on=pygame.draw.rect(surface, blue, pygame.Rect(value.rect.x + 30, value.rect.y - 30,20,20))
                            lastclicked=pygame.Rect(value.rect.x, value.rect.y - 50,100,50)
                            lastvalue=value
                        elif off.collidepoint(ev.pos):
                            lastvalue.capacite=0;
                            print("la capacité est "+ str(lastvalue.capacite))
                        elif on.collidepoint(ev.pos):
                            lastvalue.capacite=50;
                            print("la capacité est "+ str(lastvalue.capacite))
                        else:
                            pygame.draw.rect(surface,white,lastclicked)
                elif(ev.button==3):

                    for key, value in list_prod.items():
                        text = pygame.font.SysFont("timesnewroman", 8).render("transit : ", True, (0, 0, 0, 0))
                        augm = pygame.draw.rect(surface, white,
                                               pygame.Rect(value.rect.x, value.rect.y - 30, 20, 20))
                        low = pygame.draw.rect(surface, white,
                                               pygame.Rect(value.rect.x + 30, value.rect.y - 30, 20, 20))


                        if value.rect.collidepoint(ev.pos):

                            selected2.append(value)
                            lastclicked = pygame.Rect(selected2[0].rect.x, selected2[0].rect.y - 50, 100, 50)
                            if(len(selected2))>=2:
                                print("on rentre ici hophophop")
                                stats = pygame.draw.rect(surface, green,
                                                         pygame.Rect(selected2[0].rect.x, selected2[0].rect.y - 50, 100, 50))
                                augm = pygame.draw.rect(surface, blue,
                                                       pygame.Rect(selected2[0].rect.x, selected2[0].rect.y - 30, 20, 20))
                                low = pygame.draw.rect(surface, blue,
                                                      pygame.Rect(selected2[0].rect.x + 30, selected2[0].rect.y - 30, 20, 20))
                                text_rect = text.get_rect(center=stats.center)
                                surface.blit(text, augm)
                                lastclicked = pygame.Rect(selected2[0].rect.x, selected2[0].rect.y - 50, 100, 50)
                                road=Ligne(point1=selected2[0], point2=selected2[1])
                                listeroutes2.append(road)
                                road.capacite=selected2[0].capacite
                                print("la capacite de la route est "+ str(road.capacite))

                        elif augm.collidepoint(ev.pos):
                            road.transit -=10
                            print("Le transit est "+str(road.transit))

                        elif low.collidepoint(ev.pos):
                            road.transit += 10;

                            print("Le transit est " + str(road.transit))
                        else:
                            pygame.draw.rect(surface, white, lastclicked)
