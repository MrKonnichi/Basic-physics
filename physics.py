import time
import pygame
g=9.80665 #gravity
Pair=1.225 #density of air
def set_fps(fps):
	global t
	t=1/fps
class Object:
	def __init__(self,x,y,m,shape,FA):
		self.Fx=0
		self.Fy=0
		self.x=x
		self.y=y
		self.m=m
		self.FA=FA
		self.vx=0
		self.vy=0
		self.meterx=0
		self.metery=0
		if shape.lower() == "cube":
			self.Cd=1.05
		elif shape.lower() == "sphere":
			self.Cd=0.47
			
	def enable(self):
		#Drag
		DragX=-0.5*Pair*self.vx*abs(self.vx)*self.Cd*self.FA
		DragY=-0.5*Pair*self.vy*abs(self.vy)*self.Cd*self.FA
		#Acceleration
		ax= (DragX+self.Fx)/self.m
		ay= (DragY+self.Fy)/self.m -g
		#Velocity
		self.vx+=ax*t
		self.vy+=ay*t
		#Displacement
		self.meterx+=self.vx*t
		self.metery+=self.vy*t
		self.x=int((self.meterx)*64+(pygame.display.get_surface().get_width())/2)
		self.y=int((self.metery)*-64+(pygame.display.get_surface().get_height())/2)
