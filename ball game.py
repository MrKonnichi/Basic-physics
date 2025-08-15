import pygame
#axis
x, y, z = 0, 0, 0
#axis forces
Fx, Fy, Fz = 5, 40, 0

m = 0.75 #mass

shape = "sphere"
if shape == "cube":
	Cd=1.05
elif shape == "sphere":
	Cd=0.47
radius=20
A = (radius/100)**2*3.141
g=9.80665 
Pair=1.225
t=1/60
throw=0.2
ax=Fx/m
ay=Fy/m
az=Fz/m
vx,vy,vz=0,0,0
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.			current_w, info.current_h))
running=True
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
clock = pygame.time.Clock()
throw_steps=int(throw/t)
for steps in range(throw_steps):
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
	screen.fill(black)
	FixX=int(x*100+info.current_w / 2)
	FixY=int(y*-100+info.current_h / 2)
	if FixY>info.current_h-101:
		FixY=info.current_h-100
	pygame.draw.circle(screen,white,(FixX,FixY),radius)
	pygame.display.update()
	DragX=-0.5*Pair*vx*abs(vx)*Cd*A
	DragY=-0.5*Pair*vy*abs(vy)*Cd*A
	DragZ=-0.5*Pair*vz*abs(vz)*Cd*A
	ax= DragX/m
	ay= -g + DragY/m
	az= DragZ/m
	vx=vx+ax*t
	vy=vy+ay*t
	vz=vz+az*t
	x=x+vx*t
	y=y+vy*t
	z=z+vz*t
	clock.tick(60)
