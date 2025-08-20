import time
import random
import math
Gconstant=9.80665
g=9.80665 #gravity
Pair=1.225 #density of air
dt=1/60
PositionIterations=3
VelocityIterations=8
objects= []

boom=False
"""
def aabb(object1, object2):
	global boom
	left1= object1.x
	right1= object1.x + object1.width
	top1= object1.y
	bottom1= object1.y + object1.height
	left2= object2.x
	right2= object2.x + object2.width
	top2= object2.y
	bottom2= object2.y + object2.height
	overlapX=min(right1, right2) - max(left1, left2)
	overlapY=min(top1, top2) - max(bottom1, bottom2)
	if overlapX>0 and overlapY>0:
		boom=True
	else:
		boom=False
	
		if object1.type == "dynamic" and object2.type == "dynamic":
			
		elif (object1.type == "dynamic" or object1.type == "kinematic" or object1.type == "static") and object2.type == "sensor":
			object2.sensor_triggered=object1
		elif object1.type == "sensor" and (object2.type == "dynamic" or object2.type == "kinematic" or object2.type == "static"):
			object1.sensor_triggered=object2
					"""
def marurect(object1, object2):
	rectleft=object2.x
	rectright=object2.x + object2.width
	recttop=object2.y
	rectbottom=object2.y+object2.height
	closeX=clamp(object1.x,rectleft,rectright,)
	closeY=clamp(object1.y,recttop,rectbottom)
	dx=object1.x-closeX
	dy=object1.y-closeY
	distance=math.sqrt((dx**2+dy**2))
	if distance<object1.radius:
		global boom
		boom=True
def marumaru(object1, object2):
	dx=object2.x - object1.x
	dy=object2.y - object1.y
	distance=math.sqrt((dx**2+dy**2)) #Pythagorean theorem
	overlap=object1.radius+object2.radius-distance #if over 0 then overlapping
	if distance<1: #saves from crashing if distance=0 (2 objects same x,y)
		distance=1
		angle = random.uniform(0, 2 * math.pi)
		nx = math.cos(angle)
		ny = math.sin(angle)
	else:
		nx=dx/distance
		ny=dy/distance
	#tangent
	tx = -ny 
	ty = nx
	#dot product tangent (how much of velocity will be at the direction of tangent)
	dptan1 = object1.vx * tx + object1.vy * ty
	dptan2  = object2.vx * tx + object2.vy *ty
	#dot product normal
	dpnorm1 = object1.vx * nx + object1.vy * ny
	dpnorm2 = object2.vx * nx + object2.vy * ny
	#conservation of momentum
	m1 = (dpnorm1 * (object1.m - object2.m) + 2 * object2.m * dpnorm2) / (object1.m+object2.m)
	m2 = (dpnorm2 * (object2.m - object1.m) + 2 * object1.m * dpnorm1) / (object1.m+object2.m)
		
	if overlap>0:
		#update velocity temporary
		object1.vx = dptan1 * tx + nx * m1
		object1.vy = dptan1 * ty + ny * m1
	
		if object1.type == "dynamic" and object2.type == "dynamic":
			object1.x -= nx * overlap / 2
			object1.y -= ny * overlap / 2
			object2.x += nx * overlap / 2
			object2.y += ny * overlap / 2
		elif object1.type == "dynamic" and (object2.type == "kinematic" or object2.type == "static"):
			object1.x -= nx * overlap 
			object1.y -= ny * overlap
		elif (object1.type == "kinematic" or object1.type == "static") and object2.type == "dynamic":
			object2.x += nx * overlap 
			object2.y += ny * overlap 
		elif (object1.type == "dynamic" or object1.type == "kinematic" or object1.type == "static") and object2.type == "sensor":
			sensor_triggered=object1
		elif object1.type == "sensor" and (object2.type == "dynamic" or object2.type == "kinematic" or object2.type == "static"):
			sensor_triggered=object2
			
			

						

def collision():
	for i, object1 in enumerate(objects):
		for object2 in objects[i+1:]:
			if object1.type == "static" and object2.type == "static":
				continue
			if object1.shape=="circle" and object2.shape=="circle":
				marumaru(object1, object2)
			elif object1.shape == "rectangle" and object2.shape == "rectangle":
				pass
				#aabb(object1, object2)
			elif object1.shape == "circle" and object2.shape == "rectangle":
				marurect(object1, object2)
				
def update_velocity(self):
		#Drag
		DragX=-0.5*Pair*self.vx*abs(self.vx)*self.Cd*self.FA
		DragY=-0.5*Pair*self.vy*abs(self.vy)*self.Cd*self.FA
		#Acceleration
		ax= DragX/self.m
		ay= DragY/self.m - self.g
		#Velocity
		self.vx+=ax*dt
		self.vy+=ay*dt

def update_position():
	for obj in objects:
		if obj.type != "static":
			obj.ox=obj.x
			obj.oy=obj.y
			obj.meterx=obj.x/ppm + obj.vx*dt
			obj.metery=obj.y/-ppm + obj.vy*dt		
			obj.x=obj.meterx*ppm
			obj.y=obj.metery*-ppm
			obj.position=obj.x,obj.y
	

				
def update():
	global boom
	boom=False
	update_position()
	collision()

	

class Object:
	def __init__(self,position,size,shape="rectangle",m=None):
		self.type=None
		self.g=g
		self.position=position
		self.x,self.y=position
		self.ax=0
		self.ay=0
		self.vx=0
		self.vy=0
		self.meterx=self.x/ppm
		self.metery=self.y/-ppm
		self.shape=shape.lower()
		if self.shape == "rectangle":
			self.Cd=1.05
			self.width=size[0]
			self.height=size[1]
			mathsize=self.width/ppm
			self.FA=mathsize*mathsize
		elif self.shape == "circle":
			self.Cd=0.47
			mathsize=size/ppm
			self.FA=3.1416*mathsize*mathsize
			self.radius=size
			self.diameter=size*2
		if m==None:
			if shape == "circle":
				self.m=self.radius/2
			elif shape == "rectangle":
				self.m=(self.width+self.height)/2/2
		else:
			self.m=m
		objects.append(self)
			

			
	def dynamic(self):
		self.type="dynamic"
		update_velocity(self)
		

	def kinematic(self):
		self.type="kinematic"
	def static(self):
		self.type="static"
	def sensor(self):
		self.type="sensor"
	def impulse(self, x, y):
		self.vx+=x
		self.vy+=y
def set_fps(fps):
	global dt
	dt=1/fps
ppm=64
def set_ppm(new_ppm):
	global ppm
	ppm=new_ppm
	
def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))
	
