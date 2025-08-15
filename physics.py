import time
#axis
x, y, z = 0, 0, 0
#axis forces
Fx, Fy, Fz = 0, 0, 0

m = 0.058#mass
A=0.00353 #frontal area

#sets the drag coeffecient
shape = "sphere"
if shape.lower() == "cube":
	Cd=1.05
elif shape.lower() == "sphere":
	Cd=0.47
g=9.80665 #gravity
Pair=1.225 #density of air
t=1/60 #60hz
throw=0.2 #simulating a hand throw
#calculating acceleration
ax=Fx/m
ay=Fy/m
az=Fz/m 
#old velocity
vx=0
vy=0
vz=0

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
	time.sleep(t)
while True:
	DragX=-0.5*Pair*vx*abs(vx)*Cd*A
	DragY=-0.5*Pair*vy*abs(vy)*Cd*A
	DragZ=-0.5*Pair*vz*abs(vz)*Cd*A
	#Drag
	ax= DragX/m
	ay= -g + DragY/m
	az= DragZ/m
	#Acceleration
	vx+=ax*t
	vy+=ay*t
	vz+=az*t
	#Velocity
	x=x+vx*t
	y=y+vy*t
	z=z+vz*t
	#Displacement
	print(f"Coordinates: x={x:.2f}, y={y:.2f}, z={z:.2f}",end="\r")
	#Printing
	time.sleep(t)
