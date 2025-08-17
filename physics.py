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
ball=physics.Object((600,600),5,"circle",20)  
ball2=physics.Object((600,600),5,"circle",20)  
if pygame.joystick.get_count() > 0:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
else:
	joystick=False
while True:
	screen.fill(black) 
	ball.dynamic() #make ball move (must be in loop)
	ball2.dynamic()
	if ball.y>info.current_h-99-ball.radius:
		ball.y=info.current_h-99-ball.radius
		ball.g=0
		ball.vy=0
	else:
		ball.g=physics.g
	if ball2.y>info.current_h-99-ball.radius:
		ball2.y=info.current_h-99-ball.radius
		ball2.g=0
		ball2.vy=0
	else:
		ball2.g=physics.g
	for event in pygame.event.get():
		if event.type==pygame.FINGERMOTION:
			if event.dx > 0.01:
				ball.impulse(1,0)
			elif event.dx < -0.01:
				ball.impulse(-1,0)
			elif event.dy < -0.01:
				ball.impulse(0,1)
		
	pygame.draw.rect(screen, red, (0, info.current_h-99, info.current_w, 100))

	pygame.draw.circle(screen,white,(ball.x,ball.y),ball.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball2.x,ball2.y),ball2.radius) #draw the ball
	#squarex = square.x - square.length/2
	#squarey = square.x-  square.length/2
	pygame.display.update() #refresh screen
	clock.tick(60)
