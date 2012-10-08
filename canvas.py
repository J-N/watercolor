from cell import *
class Canvas:
	width=0
	height=0
	cells = {}
	boundries = {}

	def __init__(self,width,height):
		self.width=width;
		self.height=height;
		for x in range (0,self.width-1):
			for y in range (0,self.height-1):
				self.cells[(x,y)] = Cell(x,y)
		for x in range (0,self.width-1):
			for y in range (0,self.height-1):
				borderCell = Cell(-1,-1)
				if(y==0):
					self.cells[(x,y)].nCell=borderCell
				else:
					self.cells[(x,y)].nCell=self.cells[(x,y-1)])
				if(x==0):
					self.cells[(x,y)].wCell=borderCell
				else:
					self.cells[(x,y)].wCell=self.cells[(x-1,y)])
				if(y==self.height-1):
					self.cells[(x,y)].sCell=borderCell
				else:
					self.cells[(x,y)].sCell=self.cells[(x,y+1)])
				if(x==self.width-1):
					self.cells[(x,y)].eCell=borderCell
				else:
					self.cells[(x,y)].eCell=self.cells[(x+1,y)])

	def deltaStep(self):
		for x in range (0,self.width):
			for y in range (0,self.height):
				self.cells[(x,y)].deltaStep()
	def getMaxVelocity(self):
		max=0;
		for x in range (0,self.width):
			for y in range (0,self.height):
				if(self.cells[(x,y)].getMaxVelocity > max)
					max=self.cells[(x,y)].getMaxVelocity
		return max
	
	def updateVelocities(self,M,u,v,p):
		self.deltaStep()
		dt=1/self.getMaxVelocity()
		for i in range (0,1,dt):
			for x in range (0,self.width):
				for y in range (0,self.height):
					self.cells[(x,y)].updateVelocity(dt)
		for x in range (0,self.width):
			for y in range (0,self.height):
				if ((x,y) in M):
					self.cells[(x,y)].nV=self.cells[(x,y)].northVPrime
					self.cells[(x,y)].eU=self.cells[(x,y)].eastUPrime
				else:
					self.cells[(x,y)].nV=0
					self.cells[(x,y)].eU=0
					self.cells[(x,y)].sU=0
					self.cells[(x,y)].wU=0
					
	def relaxDivergence(self,u,v,p):
		t=0
		while 1:
			for x in range (0,self.width):
				for y in range (0,self.height):
					self.cells[(x,y)].eastUPrime=self.cells[(x,y)].eU
					self.cells[(x,y)].westUPrime=self.cells[(x,y)].wU
					self.cells[(x,y)].northVPrime=self.cells[(x,y)].nV
					self.cells[(x,y)].southVPrime=self.cells[(x,y)].sV
            deltaMax=0
			for x in range (0,self.width):
				for y in range (0,self.height):
                    deltaMax=self.cells[(x,y)].relaxDivergence(deltaMax)
			for x in range (0,self.width):
				for y in range (0,self.height):
					self.cells[(x,y)].eU=self.cells[(x,y)].eastUPrime
					self.cells[(x,y)].wU=self.cells[(x,y)].westUPrime
					self.cells[(x,y)].nV=self.cells[(x,y)].northVPrime
					self.cells[(x,y)].sV=self.cells[(x,y)].southVPrime
            t=t+1
            if((deltMax<=.01)||(t>=50))
                break
        
