class set_screen():
	def __init__(self):
		
		self.arr=[[' ' for x in range(500)] for x in range(500)]
		for i in range(30):
			for j in range(45):
				if i==0 or j==0 or i==29 or j==44:
					self.arr[i][j]='X'
				if i==8 and j<=36:
					self.arr[i][j]='X'
				if i==12 and j>=10:
					self.arr[i][j]='X'
				if i==25 and j<=32:
					self.arr[i][j]='X'
				if i==16 and j<=31:
					self.arr[i][j]='X'
				if i==20 and j>=8:
					self.arr[i][j]='X'
				if i==3 and j>=15 and j<=20:
					self.arr[i][j]='X'
				if i>=3 and i<8 and j==18:
					self.arr[i][j]='H'
				if i>=8 and i<12 and j==13 and i!=10:
					self.arr[i][j]='H'
				if i>=8 and i<12 and j==29:
					self.arr[i][j]='H'
				if i>=12 and i<16 and j==22:
					self.arr[i][j]='H'
				if i>=20 and i<25 and j==11 and i!=21:
					self.arr[i][j]='H'
				if i>=20 and i<25 and j==22:
					self.arr[i][j]='H'
				if i>=25 and i<29 and j==29:
					self.arr[i][j]='H'
				if i>=16 and i<=19 and j==24:
					self.arr[i][j]='H'

			print		 
		self.arr[28][9]=self.arr[28][21]=self.arr[28][33]=self.arr[28][41]='C'
		self.arr[24][4]=self.arr[24][9]=self.arr[24][17]=self.arr[24][26]='C'
		self.arr[19][12]=self.arr[19][19]=self.arr[19][28]=self.arr[19][39]='C'
		self.arr[15][2]=self.arr[15][12]=self.arr[15][20]=self.arr[15][28]='C'
		self.arr[11][11]=self.arr[11][17]=self.arr[11][26]=self.arr[11][42]='C'
		self.arr[7][4]=self.arr[7][16]=self.arr[7][23]='C'
		self.arr[2][15]='X'
#		self.arr[2][17]='Q'
		self.arr[2][20]='X'
		#self.arr[7][1]='D'
		self.arr[28][1]='P'
