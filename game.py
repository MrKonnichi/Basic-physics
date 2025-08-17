import pygame
import physics
#pygame setup
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.			current_w, info.current_h))
running=True
#setting colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
clock = pygame.time.Clock()
radius=20
physics.set_fps(60)
ball=physics.Object(0,0,1,"sphere",0.1) #summon ball
while True:
	screen.fill(black) 
	ball.enable() #make ball move (must be in loop)
	pygame.draw.rect(screen, red, (0, info.current_h-100, info.current_w, 100))
	if ball.y>info.current_h-121:
		ball.y=info.current_h-120
	pygame.draw.circle(screen,white,(ball.x,ball.y),radius) #draw the ball
	pygame.display.update() #refresh screen
	clock.tick(60)
