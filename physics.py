import time
print("The initial coordinates of the object are 0,0,0 (every digit represents a meter)")
Fx= float(input("Add a horizontal force (positive is right negative is left): "))
Fy= float(input("Add a vertical force ( positive is up negative is down): "))
Fz= float(input("Add a depth force (positve is forward negative is backward): "))
m = float(input("Set mass: "))
if m<=0:
	print("Mass must be positive")
	exit()
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
Cd=0.47
A=1
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
	print(round(x,2),round(y,2),round(z,2))
	time.sleep(t)
