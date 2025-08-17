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
ball=physics.Object(600,600,5,"circle",20) 
square=physics.Object(500,500,5,"square",40) 
if pygame.joystick.get_count() > 0:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	joystick=False
else:
	joystick=False
while True:
	screen.fill(black) 
	ball.enable() #make ball move (must be in loop)
	square.enable()
	if ball.y>info.current_h-99-ball.radius:
		ball.y=info.current_h-99-ball.radius
		ball.g=0
		ball.vy=0
	for event in pygame.event.get():
		if joystick:
			if joystick.get_button(0):
				pass
			if event.type==pygame.JOYBUTTONDOWN:
				if event.button==0:
					ball.impulse(0,10)
		else:
			taptime=pygame.time.get_ticks()
			finger_moved=False
			if event.type==pygame.FINGERMOTION:
				finger_moved=True
				if event.dx > 0.01:
					ball.impulse(5,0)
				elif event.dx < -0.01:
					ball.impulse(-5,0)
			elif event.type==pygame.FINGERUP and not finger_moved and taptime>1000:
					ball.impulse(0,50)
				

	pygame.draw.rect(screen, red, (0, info.current_h-99, info.current_w, 100))

	if square.y>info.current_h-100-square.length/2:
		square.y=info.current_h-100-square.length/2
	pygame.draw.circle(screen,white,(ball.x,ball.y),ball.radius) #draw the ball
	squarex = square.x - square.length/2
	squarey = square.x-  square.length/2
	pygame.draw.rect(screen, white, (square.x-square.length/2, square.y-square.length/2, square.length, square.length))
	pygame.display.update() #refresh screen
	clock.tick(60)
