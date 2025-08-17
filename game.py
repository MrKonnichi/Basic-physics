import pygame

x, y, z = 0, 0, 0 #axis
Fx, Fy, Fz = 5, 40, 0 #axis forces
m = 0.75 #mass
#sets the drag coeffecient
shape = "sphere"
if shape == "cube":
	Cd=1.05
elif shape == "sphere":
	Cd=0.47
radius=20
A = (radius/100)**2*3.141
g=9.80665 #gravity
Pair=1.225 #density of air
t=1/60 #60hz
throw=0.2 #simulating a hand throw
#calculating acceleration
ax=Fx/m
ay=Fy/m
az=Fz/m
vx,vy,vz=0,0,0 #old velocity
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.			current_w, info.current_h))
running=True
#setting colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
clock = pygame.time.Clock()
#initial throw
throw_hz=int(throw/t)
for steps in range(throw_hz):
	DragX=-0.5*Pair*vx*abs(vx)*Cd*A
	DragY=-0.5*Pair*vy*abs(vy)*Cd*A
	DragZ=-0.5*Pair*vz*abs(vz)*Cd*A
	
	ax = (DragX+Fx) / m
	ay = (DragY+Fy) / m -g
	az = (DragZ+Fz) / m
	
	vx+= ax * t
	vy+= ay * t
	vz+= az * t
	
	x+=vx * t
	y+=vy * t
	z+=vz * t
	print(f"Coordinates: x={x:.2f}, y={y:.2f}, z={z:.2f}",end="\r")
	clock.tick(60)
while True:
	screen.fill(black) #fills the screen with black to remove previous ball positions
	pygame.draw.rect(screen, red, (0, info.current_h-100, info.current_w, 100)) #draw ground
	#fixes the weird pygame coordinates system and makes the ball stand in the ground
	FixX=int(x*100+info.current_w / 2)
	FixY=int(y*-100+info.current_h / 2)
	if FixY>info.current_h-121:
		FixY=info.current_h-120
	pygame.draw.circle(screen,white,(FixX,FixY),radius) #draw the ball
	pygame.display.update() #refresh screen
	#drag
	DragX=-0.5*Pair*vx*abs(vx)*Cd*A
	DragY=-0.5*Pair*vy*abs(vy)*Cd*A
	DragZ=-0.5*Pair*vz*abs(vz)*Cd*A
	#acceleration
	ax= DragX/m
	ay= -g + DragY/m
	az= DragZ/m
	#velocity
	vx=vx+ax*t
	vy=vy+ay*t
	vz=vz+az*t
	#displacement
	x=x+vx*t
	y=y+vy*t
	z=z+vz*t
	clock.tick(60)
