import time
import random
g=9.80665 #gravity
Pair=1.225 #density of air
t=1/60
objects= []


def collision():
	for i, object1 in enumerate(objects):
		for object2 in objects[i+1:]:
			if object1.shape=="circle" and object2.shape=="circle":
				dx=object2.x - object1.x
				dy=object2.y - object1.y
				distance=(dx**2+dy**2)**0.5
				overlap=object1.radius+object2.radius-distance
				if distance==0:
					nx=random.uniform(-1,1)
					ny=random.uniform(-1,1)
					distance=1
				else:
					nx=dx/distance
					ny=dy/distance
				if overlap>0:
					object1.x -= nx * overlap / 2
					object1.y -= ny * overlap / 2
					object2.x += nx * overlap / 2
					object2.y += ny * overlap / 2
	



def set_fps(fps):
	global t
	t=1/fps
ppm=64
def set_ppm(new_ppm):
	global ppm
	ppm=new_ppm
class Object:
	
	def __init__(self,position,m,shape,size):
		self.g=g
		self.position=position
		self.x,self.y=position
		self.m=m
		self.vx=0
		self.vy=0
		self.meterx=self.x/ppm
		self.metery=self.y/-ppm
		self.mathsize=size/ppm
		self.shape=shape
		if shape.lower() == "square":
			self.Cd=1.05
			self.FA=self.mathsize*self.mathsize
			self.length=size
		elif shape.lower() == "circle":
			self.Cd=0.47
			self.FA=3.1416*self.mathsize*self.mathsize
			self.radius=size
			self.length=size*2
			objects.append(self)

			
	def dynamic(self):
		collision()
		#Drag
		DragX=-0.5*Pair*self.vx*abs(self.vx)*self.Cd*self.FA
		DragY=-0.5*Pair*self.vy*abs(self.vy)*self.Cd*self.FA
		#Acceleration
		ax= DragX/self.m
		ay= DragY/self.m -self.g
		#Velocity
		self.vx+=ax*t
		self.vy+=ay*t
		#Displacement

		self.meterx=self.x/ppm + self.vx*t
		self.metery=self.y/-ppm + self.vy*t		
		self.x=self.meterx*64
		self.y=self.metery*-64
		self.position=self.x,self.y
	
	def kinematic(self):
		self.vx
		self.vy
	
	def impulse(self, x, y):
		self.vx+=x
		self.vy+=y
		self.g=g #remove after developing collisions
		
					
				



		
