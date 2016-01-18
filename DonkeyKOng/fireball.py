#For generating Fireballs
from pplayer import Player
import sys
class Fireball(object):
	
	def __init__(self):
		self.cnt = 0
		self.firearr = []
		self.movfl = []
		self.cord = []

	def fireball(self):


		self.cnt=self.cnt+1
		if self.cnt==1 or self.cnt%5==0:
			self.fire()
		for i in range(len(self.firearr)):
			if self.movfl[i]==0:	
				if self.arr[self.cord[i][0]][int(self.cord[i][1])+2]==' ' and self.arr[int(self.cord[i][0])+1][int(self.cord[i][1])+2]==' ':
					self.movfl[i]=1
					__x=self.cord[i][0]		#encapsulation for private variables
					__y=self.cord[i][1]
					self.cord[i][1]=self.cord[i][1]+2
					while self.arr[self.cord[i][0]][self.cord[i][1]]!='X':
						self.cord[i][0]=self.cord[i][0]+1
					self.cord[i][0]=self.cord[i][0]-1
					self.arr[__x][__y]=' '
					if self.cord[i][0]==28 and self.cord[i][1]==1:
						self.arr[self.cord[i][0]][self.cord[i][1]]=' '
					else:
						self.arr[self.cord[i][0]][self.cord[i][1]]='O'
				elif self.arr[self.cord[i][0]][int(self.cord[i][1])+1]==' ' and self.arr[int(self.cord[i][0])+1][int(self.cord[i][1])+1]==' ':
					self.movfl[i]=1
					__x=self.cord[i][0]		#encapsulation
					__y=self.cord[i][1]
					self.cord[i][1]=self.cord[i][1]+1
					while self.arr[self.cord[i][0]][self.cord[i][1]]!='X':
						self.cord[i][0]=self.cord[i][0]+1
					self.cord[i][0]=self.cord[i][0]-1
					self.arr[__x][__y]=' '
					if self.cord[i][0]!=28 and self.cord[i][1]!=1:
						self.arr[self.cord[i][0]][self.cord[i][1]]='O'
				else:
					__x=self.cord[i][0]		#encapsulation
					__y=self.cord[i][1]
					prev=self.arr[self.cord[i][0]][self.cord[i][1]]
					if self.arr[self.cord[i][0]][int(self.cord[i][1])+2]=='C' or self.arr[self.cord[i][0]][int(self.cord[i][1])+2]=='H':
						self.cord[i][1]=self.cord[i][1]+1
					else:
						self.cord[i][1]=self.cord[i][1]+2
					self.arr[__x][__y]=' '
					if self.cord[i][0]==28 and self.cord[i][1]==1:
						self.arr[self.cord[i][0]][self.cord[i][1]]=' '
					else:
						self.arr[self.cord[i][0]][self.cord[i][1]]='O'	
				if self.arr[self.pposx][self.pposy]==self.arr[self.cord[i][0]][int(self.cord[i][1])+2]:
					self.life=self.life-1
#	print 'sssss'
					break

			elif self.movfl[i]==1:
				if self.arr[self.cord[i][0]][int(self.cord[i][1])-2]==' ' and self.arr[int(self.cord[i][0])+1][int(self.cord[i][1])-2]==' 'and self.cord[i][0]+1!=29:
					self.movfl[i]=0
					__x=self.cord[i][0]
					__y=self.cord[i][1]
					self.cord[i][1]=self.cord[i][1]-2
					while self.arr[self.cord[i][0]][self.cord[i][1]]!='X':
						self.cord[i][0]=self.cord[i][0]+1
					self.cord[i][0]=self.cord[i][0]-1
					self.arr[__x][__y]=' '
					if self.cord[i][0]==28 and self.cord[i][1]==1:
						self.arr[self.cord[i][0]][self.cord[i][1]]=' '
					else:
						self.arr[self.cord[i][0]][self.cord[i][1]]='O'
				elif self.arr[self.cord[i][0]][int(self.cord[i][1])-1]==' ' and self.arr[int(self.cord[i][0])+1][int(self.cord[i][1])-1]==' ' and self.cord[i][0]+1!=29:
					self.movfl[i]=1
					__x=self.cord[i][0]
					__y=self.cord[i][1]
					self.cord[i][1]=self.cord[i][1]-1
					while self.arr[self.cord[i][0]][self.cord[i][1]]!='X':
						self.cord[i][0]=self.cord[i][0]+1
					self.cord[i][0]=self.cord[i][0]-1
					self.arr[__x][__y]=' '
					if self.cord[i][0]==28 and self.cord[i][1]==1:
						self.arr[self.cord[i][0]][self.cord[i][1]]==' '
					else:	
						self.arr[self.cord[i][0]][self.cord[i][1]]='O'
				elif self.cord[i][0]-1!=29:
					__x=self.cord[i][0]
					__y=self.cord[i][1]
					if self.arr[self.cord[i][0]][int(self.cord[i][1])-2]=='C' or self.arr[self.cord[i][0]][int(self.cord[i][1])-2]=='H':
						self.cord[i][1]=self.cord[i][1]-1
					else:	
						self.cord[i][1]=self.cord[i][1]-2
					self.arr[__x][__y]=' '
					if self.cord[i][0]==28 and self.cord[i][1]==1:
						self.arr[self.cord[i][0]][self.cord[i][1]]=' '
					else:
						self.arr[self.cord[i][0]][self.cord[i][1]]='O'	

#				print self.pposx,self.pposy,self.cord[i][0],self.cord[i][1]
				if self.arr[self.pposx][self.pposy]==self.arr[self.cord[i][0]][int(self.cord[i][1])+2]:
					self.life=self.life-1
#					print "left"
					break		
	

	
	def fire(self):
		self.firearr.append('O')
		self.cord.append([7,2])
		self.movfl.append(0)	
	
