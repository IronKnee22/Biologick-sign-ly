import pygame
from pygame.locals import *
import time
import random

pygame.init()
pygame.joystick.init()

# Inicializace herního ovladače
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Počet pedálů na ovladači (pro G29 je to 3)
num_pedals = joystick.get_numaxes() 

# print("Detekován herní ovladač:", joystick.get_name())
# print("Počet pedálů:", num_pedals)

# Inicializace Pygame okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hra s pedály")

# Definice barev
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializace stopky
start_time = 0
stopwatch_running = False
interval = 0
current_color = None


try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
        pygame.event.pump()

        # Čtení hodnot z pedálů
        pedals = [joystick.get_axis(i) for i in range(num_pedals)]
        
        plyn = -(pedals[1])
        brzda = -(pedals[2])

        # Výstup hodnot
        # print("Plyn:", plyn)
        # print("Brzda:", brzda)

        # Reakce na stisknutí pedálu
        if plyn != 0 or brzda != 0:
            if current_color == BLUE:
                screen.fill(GREEN)
                current_color = GREEN
                interval = random.randint(3,6)
                stopky = time.time()

            akt = time.time() - stopky  
            if interval <= akt:      
                if start_time == 0:
                    start_time = time.time()
                    screen.fill(RED)
                    current_color = RED

            if brzda >= 0 and current_color == RED:
                curr_time = time.time()
                elapsed_time = curr_time - start_time
                print(elapsed_time)
                screen.fill(BLUE)
                current_color = BLUE
                start_time = 0 
            
        else:
            screen.fill(BLUE)
            current_color = BLUE  

        pygame.display.flip()  # Aktualizujte obrazovku

except KeyboardInterrupt:
    print("Program ukončen uživatelem.")

finally:
    pygame.quit()
