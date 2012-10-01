from cell import *
class Canvas:
	width=0
	height=0
	cells = {}
	boundries = {}

	def __init__(self,width,height):
		self.width=width;
		self.height=height;
		for x in range (0,self.width):
			for y in range (0,self.height):
				self.cells[(x,y)] = Cell(x,y)
	def updateVelocities(M,u,v,p):
		max=0;
		for x in range (0,self.width):
			for y in range (0,self.height):
				if(cells[(x,y)].getMaxVelocity > max)
					max=cells[(x,y)].getMaxVelocity
			
		dt=1/max
		for i in range (0,1,dt):
			for x in range (0,self.width):
				for y in range (0,self.height):
					cells[(x,y)].

		paperSlope=0
		u=u-paperSlope
		
