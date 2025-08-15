import time
print("The initial coordinates of the object are 0,0,0 (every digit represents a meter)")
Fx= float(input("Add an initial horizontal force (x axis) (positive is right negative is left): "))
Fy= float(input("Add an initial vertical force (y axis) ( positive is up negative is down): "))
Fz= float(input("Add an initial depth force (z axis) (positive is forward negative is backward): "))
m = float(input("Set mass in kg: "))
if m<=0:
	print("Mass must be positive")
	exit()
shape = input("Whats the shape (cube, sphere): ")
if shape.lower() == "cube":
	Cd=1.05
elif shape.lower() == "sphere":
	Cd=0.47
else:
	print("Please choose a cube or a sphere")
	exit()
A = float(input("Set the frontal area in m²: "))
ax=Fx/m
ay=Fy/m
az=Fz/m
t=1/60
vx=ax*t
vy=ay*t
vz=az*t
x=0
y=0
z=0
while True:
	DragX=-0.6125*vx*abs(vx)*Cd*A
	DragY=-0.6125*vy*abs(vy)*Cd*A
	DragZ=-0.6125*vz*abs(vz)*Cd*A
	ax= DragX/m
	ay= -9.8 + DragY/m
	az= DragZ/m
	vx=vx+ax*t
	vy=vy+ay*t
	vz=vz+az*t
	x=x+vx*t
	y=y+vy*t
	z=z+vz*t
	print(f"Coordinates: x={x:.2f}, y={y:.2f}, z={z:.2f}",end="\r")
	time.sleep(t)
