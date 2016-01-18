#!/bin/python
import sys
from screen import set_screen		#Modulation
from pplayer import Player		#Modulation
from fireball import Fireball		#Modulation
import sys
from donkey import Donkey		#Inheritance
from queen import Queen			#Inheritance
#Classes for processing input without pressing enter
class _Getch:			
	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError:
			self.impl = _GetchUnix()
	def __call__(self): return self.impl()
	

class _GetchUnix:
	def __init__(self):
		import tty, sys
	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
class _GetchWindows:
    def __init__(self):
            import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
screen=set_screen()
player = Player(28,1)
player.arr = screen.arr
fireballs = Fireball()
fireballs.arr = player.arr
fireballs.pposx = player.posx
fireballs.pposy = player.posy
fireballs.life = player.life
don = Donkey()
don.arr = player.arr
don.set_pos(7,1)
quen = Queen()
quen.arr = player.arr
quen.set_pos(2,17)
for i in range(30):
	for j in range(45):
		sys.stdout.write(screen.arr[i][j])
	print ''	

getch =_Getch()
while(1):
	player.m = getch()
	if player.m=='Q':
		print "You Quit!!"	
		break
	if fireballs.life==0:
		print "You Lose"
		break
	player.move(player.m)
	fireballs.pposx = player.posx
	fireballs.pposy = player.posy
	fireballs.life = player.life
	if player.m!='Q':
		fireballs.fireball()
	if player.posx==2:
		print "You Win!!"
		break	
	
