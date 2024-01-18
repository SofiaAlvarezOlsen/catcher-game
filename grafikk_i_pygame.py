# -*- coding: utf-8 -*-

import pygame as pg
import sys # hvis pygame ikke lukkes - sys.exit()
import random as rd

# Konstanter
WIDTH = 400
HEIGHT = 700

# Størrelsen til vinduet
SIZE = (WIDTH,HEIGHT)

# Frames per second (bilde per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (142, 142, 142)
LIGHTBLUE = (150, 200, 255)

# Initiere pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjøres
run = True

# Verdier for spilleren
w = 60 # bredde
h = 80 # høyde

# Startposisjon
x = WIDTH//2
y = HEIGHT - h - 10

# Henter bilde til spilleren
player_img = pg.image.load('bucket.png')

# Henter bilde for bakgrunn
background_img = pg.image.load('background_snow_2-3.png')

# Tilpasser bakgrunnsbilde til vår skjermstørrelse
background_img = pg.transform.scale(background_img, SIZE)

# Henter og tilpasser game over bilde
background_img2 = pg.image.load('gameover.png')
background_img2 = pg.transform.scale(background_img2, SIZE)

# Henter font
font = pg.font.SysFont('Arial', 26)

poeng = 0

# Funksjon som viser antall poeng
def display_points():
    text_img = font.render(f"Antall poeng: {poeng}", True, BLACK)
    surface.blit(text_img, (10,10))

liv = 3

# Funksjon som viser liv
def life():
    text_img = font.render(f"Liv: {liv}", True, BLACK)
    surface.blit(text_img, (WIDTH-80,10))

"""
# Klasse for spiller
class Player():
    def __init__(self, startposisjon, color):
        self.startposisjon = startposisjon
        self.color = color
        
# Objekter for spiller
red = Player(WIDTH//3, RED)
blue = Player(WIDTH//1.5, BLUE)

"""

# Klasse for ball:
class Ball():
    def __init__(self):
        self.r = 10
        self.x = rd.randint(self.r,WIDTH-self.r)   #WIDTH//2
        self.y = -self.r
    def update(self):
        self.y += rd.randint(3,6)
    
    def draw(self):
        pg.draw.circle(surface, WHITE, (self.x, self.y), self.r)

# Lager et ball-objekt
ball = Ball()


# Spill-løkken
while run:
    # Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)
    
    # Går gjennom hendelser (events)
    for event in pg.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False # Spillet skal avsluttes
            
    # Fyller skjermen med en farge
    #surface.fill(LIGHTBLUE)
    
    # Bruker bakgrunnsbilde
    surface.blit(background_img,(0,0))
    
    # Hastigheten til spilleren
    vx = 0
            
    # Henter knappene fra tastaturet som trykkes på 
    keys = pg.key.get_pressed()
    
    # Sjekker om ulike taster trykkes på
    if keys[pg.K_LEFT]:
        vx = -5
        
    elif keys[pg.K_RIGHT]:
        vx = 5
    
    # Sjekker kollisjon med høyre side av skjermen
    if x+w >= WIDTH:
        x = WIDTH - w # Sørger for at den ikke stikker av
        
    # Sjekker kollisjon med venstre side
    if x <= 0:
        x = 0
    
    # Oppdaterer posisjonen til rektangelet
    x += vx
    
    # Ball
    ball.update()
    ball.draw()
    
    # Sjekker kollisjon
    if (ball.y + ball.r) >= y and x <= ball.x <= x+w:
        poeng += 1
        ball = Ball()
    
    # Sjekker om vi ikke klarer å fange ballen
    if ball.y + ball.r > HEIGHT:
        liv -= 1
        if liv == 0:
            #run = False # Game over
            surface.blit(background_img2,(0,0))
            
            print("Du klarte ikke å fange ballen.")
            print(f"Du fikk {poeng} poeng")
            
            name = str(input("Hva heter du? "))
            
            filename = "points.txt"
            with open(filename, "a") as file:
                file.write(f"{name};{poeng}\n")
        ball = Ball()
        
        #print("Du klarte ikke fange ballen.")
        #print(f"Du fikk {poeng} poeng.")
        #run = False # Game over   
                   
         
    # Spiller
    #pg.draw.rect(surface, GREY, [x, y, w, h])
    surface.blit(player_img, (x,y))
    
    
    # Tekst
    display_points()
    life()
        
    # "Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()

# Avslutter pygame
pg.quit()
sys.exit()