from ex1 import findRandomNumber
import random
import pygame

n = random.randint(1,10)
# import pandas as pd

# l = [1,2,3,4,5,6]
# genObject = e.genFindEven(l)
# for i in genObject:
#     print(i)
    
# findRandomNumber(n)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))  # Set screen size of pygame window
    SPEED = 2
    ball = pygame.image.load('intro_ball.gif')
    ball_rect = ball.get_rect()
    direction = pygame.math.Vector2(SPEED, SPEED)
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # ensures pygame window closes cleanly
                exit()
                
        ball_rect.x += direction.x
        ball_rect.y += direction.y

        # Check if the ball hits the side of the window
        if ball_rect.left < 0 or ball_rect.right > 640:
            direction.x *= -1  # Reverse the ball direction
        if ball_rect.top < 0 or ball_rect.bottom > 480:
            direction.y *= -1  # Reverse the ball direction

        screen.fill((0, 0, 0))  # fill screen with black
        screen.blit(ball, ball_rect) 
        pygame.display.flip()  # update display
        
        clock.tick(150)

if __name__=="__main__":
    main()