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
ball=physics.Object((600,100),20,"circle")  
ball2=physics.Object((600,100),20,"circle")  
ball3=physics.Object((600,100),20,"circle")  
ball4=physics.Object((600,100),20,"circle")  
ball5=physics.Object((600,100),20,"circle")  
ball6=physics.Object((600,100),20,"circle")  
ball7=physics.Object((600,100),20,"circle")  
ball8=physics.Object((600,100),20,"circle")  
staticball=physics.Object((600,1200),40,"circle")  
square=physics.Object((800,600),(40,40),"rectangle")  
square2=physics.Object((700,800),(400,400),"rectangle")  
floor=physics.Object((0, info.current_h-99),(info.current_w, 100),"rectangle")
if pygame.joystick.get_count() > 0:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
else:
	joystick=False
while True:
	screen.fill(black)
	if physics.boom:
		screen.fill(red)
	ball.dynamic() 
	ball2.dynamic() 
	ball3.dynamic() 
	ball4.dynamic() 
	ball5.dynamic() 
	ball6.dynamic() 
	ball7.dynamic() 
	ball8.dynamic() 

	square.dynamic()
	square2.static()
	floor.static()
	staticball.static()
	physics.update()
	
	for event in pygame.event.get():
		if event.type==pygame.FINGERMOTION:
			if event.dx !=0:
				ball.impulse(event.dx*25,event.dy*-50)
			elif event.dy !=0:
				ball.impulse(event.dx*25,event.dy*-50)
			
	pygame.draw.rect(screen, red, (floor.x, floor.y, floor.width, floor.height))
	pygame.draw.circle(screen, red, (staticball.x,staticball.y),staticball.radius)
	pygame.draw.circle(screen,white,(ball.x,ball.y),ball.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball2.x,ball2.y),ball2.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball3.x,ball3.y),ball3.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball4.x,ball4.y),ball4.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball5.x,ball5.y),ball5.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball6.x,ball6.y),ball6.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball7.x,ball7.y),ball7.radius) #draw the ball
	pygame.draw.circle(screen,white,(ball8.x,ball8.y),ball8.radius) #draw the ball
	pygame.draw.rect(screen,white,(square.x,square.y, square.width, square.height)) #draw the ball
	pygame.draw.rect(screen,white,(square2.x,square2.y, square2.width, square2.height)) #draw the ball
	#squarex = square.x - square.length/2
	#squarey = square.x-  square.length/2
	pygame.display.update() #refresh screen
	clock.tick(60)
