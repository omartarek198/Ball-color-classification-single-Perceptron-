import  random
from Perceptron import CPerceptron
import sys
import pygame
import  CBall



def MakeDataSet(n):
    for i in range(n):
        temp = CBall.Ball()
        balls.append(temp)


def MakeBall(x,y):

    temp = CBall.Ball()
    temp.x = x
    temp.y  = y
    temp.label = P.Guess([temp.x,temp.y])
    print(temp.label)
    balls.append(temp)

def DrawScene():
    while True:
        screen.fill((20, 20, 20))
        pygame.draw.line(screen, [255,255,255], (0, 0), (600, 600))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                MakeBall(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            for ball in balls:
                if ball.label == -1:
                    ball.color = [0,0,255]
                else:
                    ball.color = [255,0,0]

             #   if ball.label == P.Guess([ball.x,ball.y]):
              #      ball.color = [0,255,0]
                pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.radius)

            pygame.display.flip()
            fpsClock.tick(fps)




# Configuration
P = CPerceptron()
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
screen = pygame.display.set_mode((width, height))
balls = []
MakeDataSet(190)
for ball in balls:
    P.Train([ball.x,ball.y] , ball.label)

DrawScene()
