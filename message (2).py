import pygame
from point_conso import Point_conso
from point_production import Point_Production
from groupe_production import Groupe_Production
from ligne import Ligne

x_window=900
y_window=750

nbReseau = 0
points = []
list_reseau = {nbReseau: points}
lignes=[]
# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((x_window, y_window))

# Initialing Color
color = (255, 0, 0)

blue = (0, 0, 255)

green = (0, 255, 0)

bg = pygame.image.load("corse.png").convert() 
nbClick=0
nbProd=0
nbConso=0
surface.blit(bg, ((x_window/4)+20, 0))
moving = False
list_prod = {}
list_conso = {}
boutons_villes = []
active = 0
value_text_name = ''
value_text_pourcentage = ''
name = ''
pourcentage = 0
nameExist = False
pourcentageExist = False
i_conso = 0
nbRoute = 0
list_route = {}
list_reseau_conso = {}
list_reseau_prod = {}
font = pygame.font.SysFont("Arial",32)

while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        # Drawing Rectangle
        #c origine, y origine, largeur, longueur
        pygame.draw.rect(surface, color, pygame.Rect(0, 0, x_window/4, y_window))


        eolien =  pygame.draw.rect(surface, blue, pygame.Rect(10, 10, ((x_window/4) - 20), 50 ))
        thermique = pygame.draw.rect(surface, blue, pygame.Rect(10, 70, ((x_window / 4) - 20), 50))
        photovoltaique = pygame.draw.rect(surface, blue, pygame.Rect(10, 130, ((x_window / 4) - 20), 50))
        hydrolique = pygame.draw.rect(surface, blue, pygame.Rect(10, 190, ((x_window / 4) - 20), 50))
        biogaz = pygame.draw.rect(surface, blue, pygame.Rect(10, 250, ((x_window / 4) - 20), 50))
        pointDeConso = pygame.draw.rect(surface, blue, pygame.Rect(10, 310, ((x_window / 4) - 20), 50))
        route = pygame.draw.rect(surface, blue, pygame.Rect(10, 370, ((x_window / 4) - 20), 50))
        delete = pygame.draw.rect(surface, blue, pygame.Rect(10, 430, ((x_window / 4) - 20), 50))
    
        if ev.type == pygame.MOUSEBUTTONDOWN :
            #if select 1->eolien, 2->thermique, 3->photovoltaique, 4->hydrolique, 5->biogaz
            if nbClick != 1:
                pygame.draw.rect(surface, (0,0,0), pygame.Rect(675, 0,  x_window/4, y_window))
            if nbClick == 1:
                if selected == 1 and pygame.mouse.get_pos() > (x_window/4, y_window):
                    print(1)
                    image_file = "eolien.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = Point_Production(rect = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 41, 42), 1))
                    nbClick+=1
                if selected == 2 and pygame.mouse.get_pos() > (x_window/4, y_window):
                    print(2)
                    image_file = "thermique.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = Point_Production(rect = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 50, 41), 1))
                    nbClick+=1
                if selected == 3 and pygame.mouse.get_pos() > (x_window/4, y_window):
                    print(3)
                    image_file = "photovoltaique.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = Point_Production(rect = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 33), 1))
                    nbClick+=1
                if selected == 4 and pygame.mouse.get_pos() > (x_window/4, y_window):
                    print(4)
                    image_file = "hydrolique.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = Point_Production(rect = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 63, 32), 1))
                    nbClick+=1
                if selected == 5 and pygame.mouse.get_pos() > (x_window/4, y_window):
                    print(5)
                    image_file = "biogaz.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = Point_Production(rect = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 32), 1))
                    nbClick+=1
                if selected == 7 and pygame.mouse.get_pos() > (x_window/4, y_window):
                    print(7)
                    ###Création des paramètres de conso
                    text  = pygame.font.SysFont("timesnewroman", 15).render("Nom de la ville", True, (0,0,0,0))
                    text2  = pygame.font.SysFont("timesnewroman", 15).render("Pourcentage de conso", True, (0,0,0,0))

                    pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
                    rect_obj1 = pygame.draw.rect(surface, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                    text_rect = text.get_rect(center=rect_obj1.center)
                    surface.blit(text, text_rect)
                    rect_obj2 = pygame.draw.rect(surface, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                    text_rect = text2.get_rect(center=rect_obj2.center)
                    surface.blit(text2, text_rect)
            
                    boutons_villes = [rect_obj1, rect_obj2]

                    for (i, bouton) in enumerate(boutons_villes):
                        if bouton.collidepoint(ev.pos):
                            if i == 0:
                                    pygame.draw.rect(surface, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                                    active = 1
                            elif i== 1:
                                    pygame.draw.rect(surface, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                                    active = 2
                    if(i_conso==0):
                        image_file = "conso.png"
                        image = pygame.image.load(image_file).convert_alpha()
                        surface.blit(image, pygame.mouse.get_pos())
                        Mouse_x, Mouse_y = pygame.mouse.get_pos()
                        nbConso+=1
                        list_conso[nbConso] = Point_conso(rect = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 32), 1))
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
                nbClick = 0
                selected = 7
                nbClick+=1
            if delete.collidepoint(ev.pos):
                selected = 8
            for key, value in list_prod.items():
                #print(key, value)
                if selected==8:
                     if value.rect.collidepoint(ev.pos):
                        del list_prod[key]
                        pygame.draw.rect(surface, (255,255,255,255), value.rect)
                        break
                elif selected == 6:
                    if value.rect.collidepoint(ev.pos):
                        #pos = pygame.mouse.get_pos()
                        list_reseau[nbReseau].append(ev.pos)
                        list_reseau_prod= value

                # else:
                #     if value.rect.collidepoint(ev.pos):

                #         pygame.draw.rect(surface, green, pygame.Rect(675, 0,  x_window/4, y_window))
                #         ajout_groupe =  pygame.draw.rect(surface, blue, pygame.Rect(675, -400, (x_window/4), y_window - 300))

                #         moving = True
                #         print("-")
                #         print(key, value)
                #         print("-")
                
                    # elif ev.type == pygame.MOUSEBUTTONUP:
                    #     moving = False
                    #     break

                    # elif ev.type == pygame.MOUSEMOTION and moving:
                    #     print("é")
                    #     pygame.value.move_ip(ev.rel)
                    #     surface.blit(image, list_prod.get(key))
                    #     pygame.draw.rect(surface,blue, pygame.Rect(Mouse_x, Mouse_y, 47, 32))
                    #     pygame.display.update()
            for key, value in list_conso.items():
                #print(key, value)
                if selected==8:
                     if value.rect.collidepoint(ev.pos):
                        del list_conso[key]
                        pygame.draw.rect(surface, (255,255,255,255), value.rect)
                        break
                elif selected == 6:
                    if value.rect.collidepoint(ev.pos):
                        #pos = pygame.mouse.get_pos()
                        list_reseau[nbReseau].append(ev.pos)
                        list_reseau_conso = value
                    
        if nbReseau in list_reseau and  len(list_reseau[nbReseau]) >= 2:
            #my_rect = pygame.draw.rect(surface, blue, pygame.Rect(list_reseau[nbReseau][0][0],  list_reseau[nbReseau][0][1],
            #abs(list_reseau[nbReseau][1][0] - list_reseau[nbReseau][0][0]), abs(list_reseau[nbReseau][1][1] - list_reseau[nbReseau][0][1])))
            #0 = Prod, 1 = Conso
            prod = list_reseau_prod
            cons = list_reseau_conso
            nbRoute+=1
            list_route[nbRoute] = Ligne(reseau = pygame.draw.lines(surface, blue, False, list_reseau[nbReseau]), prod = prod, conso = cons)
            list_reseau = {}
            prod = None
            cons = None
            print(list_route[nbRoute].conso.nom)


        if ev.type == pygame.KEYDOWN:
            if active == 1:
                string_format = "Nom de la ville : "
                if ev.key==13: #pygame.K_KP_ENTER:
                    name = value_text_name
                    nameExist = True
                    value_text_name = ''
                    string_format = ''
                elif ev.key == pygame.K_RETURN:
                    value_text_name = ''
                    string_format = ''
                elif ev.key == pygame.K_BACKSPACE:
                    value_text_name = value_text_name[:-1]
                else:
                    value_text_name += ev.unicode
                    font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text_name), True, (0,0,0,0))
                    text_rect = font_text.get_rect(center=rect_obj1.center)
                if value_text_name!="":
                    pygame.draw.rect(surface, (120,120,120,120), pygame.Rect(3*x_window/4, 150, x_window/4, 50))
                surface.blit(font_text, text_rect)
            elif active == 2:
                string_format = "Pourcentage de conso : "
                if ev.key==13:#pygame.K_KP_ENTER:
                    try:
                        pourcentage = int(value_text_pourcentage)
                        pourcentageExist = True
                        value_text_pourcentage = ''
                        string_format = ''
                    except:
                        pass
                elif ev.key == pygame.K_RETURN:
                    value_text_pourcentage = ''
                    string_format = ''
                elif ev.key == pygame.K_BACKSPACE:
                    value_text_pourcentage = value_text_pourcentage[:-1]
                else:
                    value_text_pourcentage += ev.unicode
                    font_text  = pygame.font.SysFont("timesnewroman", 15).render(string_format + str(value_text_pourcentage), True, (0,0,0,0))
                    text_rect = font_text.get_rect(center=rect_obj2.center)
                if value_text_pourcentage!="":
                    pygame.draw.rect(surface, (120,120,120,120), pygame.Rect(3*x_window/4, 250, x_window/4, 50))
                surface.blit(font_text, text_rect)
                
        if nameExist and pourcentageExist:
            list_conso[nbConso].nom = name
            list_conso[nbConso].pourcentage = pourcentage
            nbClick+=1
            nameExist = False
            pourcentageExist = False
            pygame.draw.rect(surface, (0,0,0,0), pygame.Rect(3*x_window/4, 0, x_window/4, y_window))
            i_conso = 0

        pygame.display.flip()