import sys
import os

# Pygame pakken må installeres. Fra cmd: pip install pygame
# Pygame: https://www.pygame.org
import pygame
# Importerer variabler fra pygame
from pygame.locals import *
from settings import *
import control # Importerer vår egen fil: control.py 

ball_dx = 0
ball_dy = 1
# Bruker et pygame.Rect for å holde kontroll på ballen
ball = pygame.Rect(DISPLAY_RESOLUTION[0]/2, 0, 50,50)



def handle_event(event):
    # Avslutter ved vindu [X]
    if (event.type == QUIT):
        pygame.quit()
        sys.exit()
    # Et tastetrykk? Dokuemtasjon: https://www.pygame.org/docs/ref/key.html
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            pass
        elif event.key == K_DOWN:
            pass
    

# Tegner ting
def draw():
    # Tegner en hvit bakgrunn på "surface"
    # Dokumentasjon: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
    surface.fill((255, 255, 255))
    # Tegner en fylt sirkel
    # Dokuemtasjon: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    pygame.draw.circle( 
        surface, # surface vi tegner på
        (255, 0, 0), # farge - RGB
        (ball.left, ball.top), # posisjon
        int(ball.width/2) # radius
        )

# Oppdatere ting
def update():
    ball.top += ball_dy

screen, surface, clock = control.pygame_init() # Initialiserer pygame mm.
# Program løkken som gjentar seg "evig"    
while True:
    # Fanger opp hendelser 
    # https://www.pygame.org/docs/ref/event.html#pygame.event.pump
    pygame.event.pump()
    # Sjekker om det er tastetrykk eller musklikk mm.
    for event in pygame.event.get():
        handle_event(event) # Kaller funskjonen som håndterer event
    
    update() # Kaller update() funksjonen
    draw() # Kaller draw() funksjonen
    
    # Tegner surface til "skjermen"
    # Dokumentasjon: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(surface, (0,0)) 
    pygame.display.flip() # Oppdaterer skjermen https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    clock.tick(60) # Tikker "klokken" sånn at løkken vår går 60 ganger pr. sekund https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    
    
    