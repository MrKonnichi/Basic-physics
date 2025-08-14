print("The initial coordinates of the object are 0,0,0 (every digit represents a meter)")
Fx= float(input("Add a horizontal force (positive is right negative is left): "))
Fy= float(input("Add a vertical force ( positive is up negative is down): "))
Fz= float(input("Add a depth force (positve is forward negative is backward): "))
m = float(input("Set mass: "))
if m<=0:
	print("Mass must be positive")
	exit()
t= float(input("Set time: "))
if t<=0:
	print("Time must be positive")
	exit()
gravity= input("""Type 1 if you want gravity
Type 2 if you don't want gravity
: """)
if gravity == "1":
	weight = m*9.8
elif gravity == "2":
	weight=0
else:
	print("Please choose 1 or 2")
	exit()
Fy-=weight
ax=Fx/m
ay=Fy/m
az=Fz/m
vx=0
vy=0
vz=0
x=0.0
y=0.0
z=0.0
x=x+vx*t+0.5*ax*t**2
y=y+vy*t+0.5*ay*t**2
z=z+vz*t+0.5*az*t**2
point = [x,y,z]
print(point)
