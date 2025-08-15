import time

x, y, z = 0, 0, 0 #axis
Fx, Fy, Fz = 0, 0, 0 #axis forces
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
vx,vy,vz=0,0,0 #old velocity
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
	time.sleep(t)
while True:
	#Drag
	DragX=-0.5*Pair*vx*abs(vx)*Cd*A
	DragY=-0.5*Pair*vy*abs(vy)*Cd*A
	DragZ=-0.5*Pair*vz*abs(vz)*Cd*A
	#Acceleration
	ax= DragX/m
	ay= -g + DragY/m
	az= DragZ/m
	#Velocity
	vx+=ax*t
	vy+=ay*t
	vz+=az*t
	#Displacement
	x=x+vx*t
	y=y+vy*t
	z=z+vz*t
	#printing coordinates
	print(f"Coordinates: x={x:.2f}, y={y:.2f}, z={z:.2f}",end="\r")
	time.sleep(t)
