import sys
import os

# Pygame pakken må installeres. Fra cmd: pip install pygame
# Pygame: https://www.pygame.org
import pygame
# Importerer variabler fra pygame
from pygame.locals import *
from settings import *
import control # Importerer vår egen fil: control.py 

#ball_angle = 0
ball_dx = BALL_INITIAL_SPEED
ball_dy = BALL_INITIAL_SPEED
# Bruker et pygame.Rect for å holde kontroll på ballen
ball_rect = pygame.Rect(DISPLAY_RESOLUTION[0]/2, 0, 50,50)

p1_rect = pygame.Rect(0, DISPLAY_RESOLUTION[1]//2 - PADDLE_SIZE[1] // 2, PADDLE_SIZE[0], PADDLE_SIZE[1])
# Setter Paddle 1 en bredde fra venstre
p1_rect.left = PADDLE_SIZE[0]
p2_rect = pygame.Rect(0, DISPLAY_RESOLUTION[1]//2 - PADDLE_SIZE[1] // 2, PADDLE_SIZE[0], PADDLE_SIZE[1])
# Setter Paddle 2 en bredde fra høyre
p2_rect.right = DISPLAY_RESOLUTION[0] - PADDLE_SIZE[0]



def handle_event(event):
    global ball_dx
    global ball_dy

    # Avslutter ved vindu [X]
    if (event.type == QUIT):
        pygame.quit()
        sys.exit()
    # Et tastetrykk? Dokuemtasjon: https://www.pygame.org/docs/ref/key.html
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            p2_rect.top -= PADDLE_SPEED
        elif event.key == K_DOWN:
            p2_rect.top += PADDLE_SPEED
        elif event.key == K_q:
            p1_rect.top -= PADDLE_SPEED
        elif event.key == K_a:
            p1_rect.top += PADDLE_SPEED

# Tegner ting
def draw():
    # Tegner en hvit bakgrunn på "surface"
    # Dokumentasjon: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
    surface.fill((0, 0, 0))
    # Tegner en fylt sirkel
    # Dokuemtasjon: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    '''
    pygame.draw.circle( 
        surface, # surface vi tegner på
        (255, 0, 0), # farge - RGB
        (ball_rect.left, ball_rect.top), # posisjon
        int(ball_rect.width/2) # radius
        )
    '''
    # Tegner Paddle 1
    pygame.draw.rect(surface, PADDLE_COLOR, p1_rect)
    # Tegner Paddle 2
    pygame.draw.rect(surface, PADDLE_COLOR, p2_rect)


    # "Tegner" bilde
    surface.blit(ball_image, ball_rect)

    # Vi kan også rotere ballen
    #surface.blit(pygame.transform.rotate(ball_image, ball_angle), ball_rect)


# Oppdatere ting
def update():
    global ball_dx
    global ball_dy

    ball_rect.top += ball_dy
    ball_rect.left += ball_dx
    if (ball_rect.right >= DISPLAY_RESOLUTION[0] - PADDLE_SIZE[0]):
        pass
    if (ball_rect.left <= 0):
        ball_dx = ball_dx*-1

    if (ball_rect.bottom >= DISPLAY_RESOLUTION[1]) or (ball_rect.top <= 0):
        ball_dy = ball_dy*-1

    if p1_rect.colliderect(ball_rect):
        ball_dx = ball_dx*-1

    if p2_rect.colliderect(ball_rect):
        ball_dx = ball_dx*-1

    
    
    #Roterende ball
    #global ball_angle
    #ball_angle += 1
    
    #if ball_angle >= 360:
    #    ball_angle = 0
    

screen, surface, clock = control.pygame_init() # Initialiserer pygame mm.
# Vi kan også bruke et bilde
ball_image = control.pygame_load_image('chrome.png', (50,50))



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
    
    
    