import pygame

x_window=900
y_window=750

points = []
lignes=[]
# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((x_window, y_window))

# Initialing Color
color = (255, 0, 0)

blue = (0, 0, 255)

bg = pygame.image.load("corse.png").convert() 
nbClick=0
nbProd=0
surface.blit(bg, ((x_window/4)+20, 0))
moving = False
list_prod = {}

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

            if nbClick == 1:
                if selected == 1:
                    print(1)
                    image_file = "eolien.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 41, 42), 1)
                    nbClick+=1
                if selected == 2:
                    print(2)
                    image_file = "thermique.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 50, 41), 1)
                    nbClick+=1
                if selected == 3:
                    print(3)
                    image_file = "photovoltaique.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 33), 1)
                    nbClick+=1
                if selected == 4:
                    print(4)
                    image_file = "hydrolique.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 63, 32), 1)
                    nbClick+=1
                if selected == 5:
                    print(5)
                    image_file = "biogaz.png"
                    image = pygame.image.load(image_file).convert_alpha()
                    surface.blit(image, pygame.mouse.get_pos())
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    nbProd+=1
                    list_prod[nbProd] = pygame.draw.rect(surface, (255,255,255,255), pygame.Rect(Mouse_x, Mouse_y, 47, 32), 1)
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
            for key, value in list_prod.items():
                print(list_prod)
                if selected==8:
                     if value.collidepoint(ev.pos):
                        del list_prod[key]
                        pygame.draw.rect(surface, (255,255,255,255), value)
                        break
                else:
                    if value.collidepoint(ev.pos):
                        moving = True
                        print("-")
                        print(key, value)
                        print("-")
                
                    elif ev.type == pygame.MOUSEBUTTONUP:
                        moving = False
                        break

                    elif ev.type == pygame.MOUSEMOTION and moving:
                        print("é")
                        pygame.value.move_ip(ev.rel)
                        surface.blit(image, list_prod.get(key))
                        pygame.draw.rect(surface,blue, pygame.Rect(Mouse_x, Mouse_y, 47, 32))
                        pygame.display.update()

        if len(points) >= 2:
            pygame.draw.lines(surface, blue, False, points)

        pygame.display.flip()