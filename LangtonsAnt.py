# LangtonsAnt.py
# Nathan Greene
# Summer 2018
#
# This script simulates Langton's ant. The ant moves under the following rules:
# 	+ If the ant is on a 0 square, turn right, move forward, and set the space
#	to 1.
#	+ If the ant is on a 1 square, turn left, move forward, and set the space to
#	0.
#
# Source:  https://www.futilitycloset.com/2014/04/06/langtons-ant/

#import itertools.cycle
import sys
import time

def main():
	LA = LangtonsAnt(10, 0)
	LA.run(iters=10000, sleeptime=0.2)
	#for i in range(10000):
	#	LA.move()
	#	print(LA)
	#	print("\n\nIteration: {0}\n".format(i))

class LangtonsAnt:
	def __init__(self, dims=10, setup=0):
		if 1 < dims:
			self.dims = dims
			if setup == 0:
				self.ant = {"x": dims // 2, "y": dims // 2, "state": " ", "facing": "up"}
				self.board = [[" " for i in range(dims)] for j in range(dims)]
				self.board[self.ant["x"]][self.ant["y"]] = "X"

	def __str__(self):
		s = ""
		for i in range(self.dims):
			for j in range(self.dims):
				s += str(self.board[i][j]) + " "
			s += "\n"
		return s

	def move(self):
		if self.ant["state"] == " ":
			self.board[self.ant["x"]][self.ant["y"]] = "."
			if self.ant["facing"] == "up":
				self.ant["facing"] = "right"
				self.ant["x"] += 1
			elif self.ant["facing"] == "down":
				self.ant["facing"] = "left"
				self.ant["x"] += self.dims - 1
			elif self.ant["facing"] == "right":
				self.ant["facing"] = "down"
				self.ant["y"] += 1
			elif self.ant["facing"] == "left":
				self.ant["facing"] = "up"
				self.ant["y"] += self.dims - 1
		elif self.ant["state"] == ".":
			self.board[self.ant["x"]][self.ant["y"]] = " "
			if self.ant["facing"] == "up":
				self.ant["facing"] = "left"
				self.ant["x"] += self.dims - 1
			elif self.ant["facing"] == "down":
				self.ant["facing"] = "right"
				self.ant["x"] += 1
			elif self.ant["facing"] == "right":
				self.ant["facing"] = "up"
				self.ant["y"] += self.dims - 1
			elif self.ant["facing"] == "left":
				self.ant["facing"] = "down"
				self.ant["y"] += 1
		self.ant["x"] %= self.dims
		self.ant["y"] %= self.dims
		self.ant["state"] = self.board[self.ant["x"]][self.ant["y"]]
		self.board[self.ant["x"]][self.ant["y"]] = "X"

	def run(self, iters, sleeptime=0.2):
		if iters * sleeptime > 0:
			for i in range(iters):
				self.move()
				#for j in range(self.dims + 1):
				#	sys.stdout.write("\b")
				sys.stdout.write("Step: {}\n".format(i + 1))
				sys.stdout.write(str(self))
				sys.stdout.write("\r")
				sys.stdout.flush()
				time.sleep(sleeptime)

	__repr__ = __str__

main()
