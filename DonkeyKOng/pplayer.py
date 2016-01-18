#For moving Player
import sys
class Player(object):
	def __init__(self,posx,posy):
		self.posx = posx
		self.posy = posy
		self.m = None
		self.arr = None
		self.fl1 = 0
		self.fl2 = 0
		self.life = 3
		self.score = 0

	def move(self,m):
		self.m = m
		if self.m=='A':				#If player moves left 

			if self.posy>0:
				__ax=self.posx
				__ay=self.posy
			if self.arr[self.posx][self.posy-1]=='H':
				self.arr[self.posx][self.posy]=' '
				self.posy=self.posy-1
				self.arr[self.posx][self.posy]='P'
				self.fl2=1
			elif self.fl2==1:
				self.arr[self.posx][self.posy]='H'
				self.posy=self.posy-1
				self.arr[self.posx][self.posy]='P'
				self.fl2=0
			elif self.arr[self.posx][self.posy-1]!='X' and self.arr[self.posx+1][self.posy-1]!=' ':
				self.arr[self.posx][self.posy]=' '
				self.posy=self.posy-1
				self.arr[self.posx][self.posy]='P'	
			for i in range(30):
				for j in range(45):
					sys.stdout.write(self.arr[i][j])
				print	
			if self.arr[self.posx][self.posy-1]=='C':
				self.score=self.score+5
		elif self.m=='D':			#If player moves right			
#			print 'sdfdf'
			if self.posy<44:
				__dx=self.posx
			  	__dy=self.posy
				if self.arr[self.posx][self.posy+1]=='H':
					self.arr[self.posx][self.posy]=' '
					self.posy=self.posy+1
					self.arr[self.posx][self.posy]='P'
					self.fl1=1
				elif self.fl1==1:
			 		self.arr[self.posx][self.posy]='H'
		       			self.posy=self.posy+1
					self.arr[self.posx][self.posy]='P'
			     		self.fl1=0		
				elif self.arr[self.posx][self.posy+1]!='X' and self.arr[self.posx+1][self.posy+1]!=' ':			
			 		self.arr[self.posx][self.posy]=' '
		       			self.posy=self.posy+1
					self.arr[self.posx][self.posy]='P'
					
	#	if self.arr[self.posx][self.posy+1]=='C':
	#				self.score=self.score+1	 
		
				  	
			  	
			  		
			for i in range(30):
				for j in range(45):
					sys.stdout.write(self.arr[i][j])
				print	
			if self.arr[self.posx][self.posy+1]=='C':
	 			self.score=self.score+5
		elif self.m=='W':			#If player moves upwards
			__tx=self.posx
			__ty=self.posy
			fl=0

			if self.arr[self.posx-1][self.posy]==' ' and self.arr[self.posx+1][self.posy]=='H' and self.arr[self.posx][self.posy-1]=='X' or self.arr[self.posx-1][self.posy]=='H':
			   	tx=self.posx
				ty=self.posy 
				self.posx=self.posx-1
				fl=1
				self.arr[self.posx][self.posy]='P'	
			if fl==1:
				self.arr[tx][ty]='H'
				fl=0			
			for i in range(30):
				for j in range(45):
					sys.stdout.write(self.arr[i][j])
				print
			if self.arr[self.posx][self.posy+1]=='C':
	 			self.score=self.score+5
			 
		elif self.m=='S':			#If player moves downwards
			if self.posx<29:
				if self.arr[self.posx+1][self.posy]=='H':  
					self.arr[self.posx][self.posy]='H'
					self.posx=self.posx+1
			self.arr[self.posx][self.posy]='P'
			for i in range(30):
				for j in range(45):
					sys.stdout.write(self.arr[i][j])
				print		
			if self.arr[self.posx][self.posy+1]=='C':
	 			self.score=self.score+5	
		print "Your self.score-->",self.score
		print "Lives Left-->",self.life
