import random
class Cell:
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

	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.h=random.random()

	def getMaxVelocity:
		return max(self.nV,self.sV,self.wU,self.eU)
