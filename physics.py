import time
import pygame
g=9.80665 #gravity
Pair=1.225 #density of air
t=1/60
def set_fps(fps):
	global t
	t=1/fps
ppm=64
def set_ppm(new_ppm):
	global ppm
	ppm=new_ppm
class Object:
	def __init__(self,x,y,m,shape,size):
		self.g=g
		self.x=x
		self.y=y
		self.m=m
		self.vx=0
		self.vy=0
		self.meterx=x/ppm
		self.metery=y/-ppm
		self.size=size/ppm
		if shape.lower() == "square":
			self.Cd=1.05
			self.FA=self.size*self.size
			self.length=size
		elif shape.lower() == "circle":
			self.Cd=0.47
			self.FA=3.1416*self.size*self.size
			self.radius=size
	def enable(self):
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
			
		
	def impulse(self, Fx, Fy):
			self.vx+=Fx/self.m
			self.vy+=Fy/self.m
			self.g=g
