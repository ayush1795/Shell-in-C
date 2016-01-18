#Inheritence
from pplayer import Player
class Donkey(Player):
	def __init__(self):
		pass
	def set_pos(self,x,y):
		self.arr[x][y] = 'D'
