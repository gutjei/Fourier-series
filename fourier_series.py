import pygame
import random
from math import *
import numpy as np


WIDTH = 1500
HEIGHT = 1000
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 225, 53)



def toFixed(numObj, digits=3):
    return f"{numObj:.{digits}f}"
def show_fps(window, clock):
    fps_overlay = FPS_FONT.render(str(clock.get_fps()), True, GOLDENROD)
    #lines = FPS_FONT.render(str(toFixed(d1)+' '+str(toFixed(d2))), True, GOLDENROD)
    #rr = FPS_FONT.render("x="+str(Mx)+"y="+str(My)+"z="+str(toFixed(math.asin(math.sin(ShowZ)))), True, GOLDENROD)
    #window.blit(fps_overlay, (0, 0))
    #window.blit(rr, (300, 0))
    #window.blit(lines, (Mx+50, My-50))

def speedT(g):
	for i in newC:
		i.speed = (2 * pi) / 53

class segment():
	def __init__(self,amp,phase,freq):
		self.x = 50
		self.y = 50
		self.v = 0
		self.speed = (2 * pi) / 53
		self.time = 370
		self.shift_x = 0
		self.shift_y = 0
		self.radius = 0
		self.old = []
		self.phase = 0
		self.freq = freq
		self.amp = amp
		
		self.g = 1
					 		   
	def Rotate_Z(self,az,temp):
		self.coordP = np.dot(Mz(az),self.coordP)
		self.depthF()
	def Rotate_Y(self,ay,temp):
		self.coordP = np.dot(My(ay),self.coordP)
		self.depthF()
	def Rotate_X(self,ax,temp):
		self.coordP = np.dot(Mx(ax),self.coordP)
		self.depthF()
	
	def getX(self): return self.x
	def getY(self): return self.y
	
	def update(self,shift_x,shift_y):
		
		#print(radius)
		shift_x = int(shift_x - self.amp)
		shift_y = int(shift_y - self.amp)
		radius = int(self.amp)
		
		self.shift_x = shift_x
		self.shift_y = shift_y
		self.radius = radius
		
		
		self.x = int(radius*cos(self.freq*(-self.v)+self.phase))+radius+shift_x
		self.y = int(radius*sin(self.freq*(-self.v)+self.phase))+radius+shift_y
		
		#self.y //= 500 
		#self.x //= 500
		
		
		pygame.draw.circle(screen, GREEN, (self.x, self.y), 2, 1)
		
		if radius > 1:
			pygame.draw.arc(screen, WHITE, (shift_x, shift_y, radius*2, radius*2), 0, 2*pi, 1)
		
		self.v += self.speed
		#if self.v >= 2*pi: 
			#self.v = 0
			#self.speed = (2 * pi) / 53
		
		
	def render(self):

		sf = pygame.Surface((WIDTH, HEIGHT))
		ar = pygame.PixelArray(sf)
		
		self.old.insert(0,[self.x,self.y])

		j = 0
		for i in self.old:
			ar[i[0],i[1]] = (255,0,255)
			j-=1
		
		j = 0
		for i in range(len(self.old)-1):
			pygame.draw.aaline(screen, ORANGE, (self.old[i][0],self.old[i][1]),
												(self.old[i+1][0],self.old[i+1][1]))
			j-=1
		
		#self.time += 1
		if len(self.old) > 52: 
			self.old.pop()
			self.old = []
			speedT(self.g)
			self.g +=1
		#if self.time == WIDTH: self.time = 300
		return sf
		

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS_FONT = pygame.font.SysFont("Verdana", 20)
GOLDENROD = pygame.Color("goldenrod")
 

running = True


circles=[
		segment(pi/100),
		segment(pi/(100/3)),
		segment(pi/(100/5))]
		
		#segment(pi/(100/7)),
		#segment(pi/(100/9))]
'''
import waves 
w = waves.getWaves()

newC = []
for i in w:
	newC.append(segment(i.amp*2,i.phase,i.freq))
'''
while running:
	screen.fill(BLACK)
	
	clock.tick(FPS)
	pygame.event.pump()
	
	surface = newC[len(circles)-1].render()
	#screen.blit(surface, (0, 0))
	
	circles[0].update(500,500)
	
	
	#for i in range(1,len(circles)):
	#		circles[i].update(circles[i-1].getX(),newC[i-1].getY())
		

	circles[0].update(2/pi*100,200,200)
	j=1
	for i in range(3,len(circles)*2+1,2):
		p = 2/(pi*i)*100
		circles[j].update(p,circles[j-1].getX()-p,circles[j-1].getY()-p)
		j+=1
	


	#circle.update(2/pi*100,200,200)
	#circle2.update((1-(-1)**2)/(pi*2)*100,circle.getX()-(1-(-1)**2)/(pi*2)*100,circle.getY()-(1-(-1)**2)/(pi*2)*100)
	#circle3.update((1-(-1)**3)/(pi*3)*100,circle.getX()-(1-(-1)**3)/(pi*3)*100,circle.getY()-(1-(-1)**3)/(pi*3)*100)
	#circle4.update((1-(-1)**4)/(pi*4)*100,circle3.getX()-(1-(-1)**4)/(pi*4)*100,circle3.getY()-(1-(-1)**4)/(pi*4)*100)
	#circle5.update((1-(-1)**5)/(pi*5)*100,circle3.getX()-(1-(-1)**5)/(pi*4)*100,circle3.getY()-(1-(-1)**5)/(pi*5)*100)
	#
	#pygame.draw.aaline(screen, ORANGE, (circles[len(circles)-1].getX(),circles[len(circles)-1].getY()), (370,circles[len(circles)-1].getY()))
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	show_fps(screen, clock)
	pygame.display.flip()

pygame.quit()
