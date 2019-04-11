# Modul for diverse funksjonalite
import sys
import os
import pygame
# Pygame: https://www.pygame.org/news
from pygame.locals import *
# Importerer instllingene våre
from settings import *

# Initialisere Pygame mm.
def pygame_init():
    # Globale variabler er tilgjengelige utenfor funksjonen
    global clock
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Setter at vinduet skal åpnes midt på skjermen
    pygame.init() # Initialiserer pygame modulen
    # Setter opp en klokke for at spillet skal gå like fort uavhengig av PC
    # Dokumentasjon: https://www.pygame.org/docs/ref/time.html
    clock = pygame.time.Clock() 
    # Initaliserer fonter 
    # Dokumentasjon: https://www.pygame.org/docs/ref/font.html
    pygame.font.init()
    # Setter opp at tastetrykk skal repeteres automatisk
    # Dokumentasjon: https://www.pygame.org/docs/ref/key.html#pygame.key.set_repeat
    pygame.key.set_repeat(10, 10) 
    # Setter opp "skjerm" - angir størrelse på vinduet.
    # https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode(DISPLAY_RESOLUTION)
    # Setter opp hoved "surface" som er like stort som screen (Winduet)
    # Dokumentasjon: https://www.pygame.org/docs/ref/surface.html
    surface = pygame.Surface(screen.get_size()) 
    surface.convert() # Konverterer Pixel format til samme som screen
    return screen, surface, clock

def pygame_load_image(filename, size = (100, 100)):
    ''' Returnerer en surface med det skalerte bilde
        Bilde bør være transparent (png eller gif)
    ''' 
    img = pygame.image.load(filename)
    img.convert()
    # Skalerer størrelsen på bilde til det som  passer best innenfor målet
    rect =  img.get_rect().fit(pygame.Rect((0, 0), size))
    # Lager en surface med samme størrelse som ønsket bilde (Likk mikk for at den skal bli transparent)
    image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
    image = image.convert_alpha()
    # Tegner skalert bilde på Surface
    image.blit(pygame.transform.smoothscale(img, rect.size), (0,0))
    return image # Returnerer en "Surface"