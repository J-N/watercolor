import random
class Cell:
	mew=.1
        drag=.01

	x=0
	y=0
	h=0		#paper height at cell
	c=0		#fluid capacity of cell
	epsilon=0 	#min saturation lvl a pixel must have before it can diffuse
	delta=0		#saturation value below which pixel will not receive diffusion
	pressure=0
	pigmentConcentration=0
	
        nV=0             #north vertical water velocity
        sV=0             #south vertical water velocity


	wU=0             #west horizontal water velocity
	eU=0             #east horizontal water velocity

	nDT=0
	wDT=0
	sDT=0
	eDT=0

	nCell=0
	wCell=0
	sCell=0
	eCell=0

	eastUPrime=0
	westUPrime=0
	northVPrime=0	
	southVPrime=0	
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.h=random.random()

	def deltaStep(self):
		if((self.x>-1)&&(self.y>-1)):
			self.nV=self.nv-self.nDT
                	self.wU=self.wU-self.wDT
                	self.sV=self.sV-self.sDT
                	self.eU=self.eU-self.eDT
		
	def getMaxVelocity(self):
		return max(self.nV,self.sV,self.wU,self.eU)
	def getU(self):
		return (self.wU+self.eU)/2
	def getV(self):
		return (self.nV+self.sV)/2
	def updateVelocity(self,dt):
		 u=self.getU()
                 v=self.getV()

                 A=u^2-self.eCell.getU()^2+(self.eU*self.sV)-(self.eU*self.nV)
                 B=(self.eCell.eU+self.wU+self.nCell.eU+self.sCell.eU-(4*self.eU))
                 self.eastUPrime=self.eU+dt(A-(mew*B)+self.pressure-eCell.pressure-(drag*self.eU))	
		 	
                 A=v^2-self.nCell.getV()^2+(self.wU*self.nV)-(self.eU*self.nV)
                 B=(self.eCell.nV+self.wCell.sV+self.nCell.nV+self.sV-(4*self.nV))
                 self.northVPrime=self.nV+dt(A-(mew*B)+self.pressure-nCell.pressure-(drag*self.nV))	
	def relaxDivergence(self,deltaMax):
		delta=.1*(self.eU-self.wU+self.nV+self.sV)
		self.pressure=self.pressure+delta
		self.eastUPrime=self.eastUPrime+delta
		self.westUPrime=self.westUPrime-delta
		self.northVPrime=self.northVprime+delta
		self.southVPrime=self.southVprime-delta
		return max(deltaMax,delta)
			
		
