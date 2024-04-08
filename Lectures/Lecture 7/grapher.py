# My grapher

# import and set of variables
import pygame
from pygame import *
pygame.init()

font = pygame.font.SysFont('Verdana', 16)
font2 = pygame.font.SysFont('Serif', 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAPH_COLOR = (200, 0, 200) #purple
GRID_COLOR = (100, 250, 240) #light blue

width, height = 500, 500
extraW = 400
screen = pygame.display.set_mode((width + extraW, height))
pygame.display.set_caption("My Personal Grapher")
screen.fill(WHITE)

# graph paper background function
def graph_paper(k):
    screen.set_clip(0, 0, width, height)
    screen.fill(WHITE)
    
    # draw the graph paper
    for i in range(int(width/k)):
        gridx = k*i
        gridy = k*i
        pygame.draw.line(screen, GRID_COLOR, (gridx, 0), (gridx, height), 1)
        pygame.draw.line(screen, GRID_COLOR, (0, gridy), (width, gridy), 1)
    
    # extra thick line
    pygame.draw.line(screen, GRID_COLOR, (width, 0), (width, height), 5)
    
    # graph x and y axis
    midx, midy = width/(2*k), height/(2*k)
    pygame.draw.line(screen, BLACK, (midx*k, 0), (midx*k, height), 3)
    pygame.draw.line(screen, BLACK, (0, midy*k), (width, midy*k), 3)

# main function
def main():
    
    # pixel per grid
    k = 25
    graph_paper(k)
    
    active = True
    while active:
        pygame.display.update()
         
        #keyboard and mouse actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                
    # Quit
    pygame.quit()
    
# Run the program
if __name__ == '__main__':
    main()