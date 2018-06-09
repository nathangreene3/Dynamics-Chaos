# LangtonsAnt.py
# Nathan Greene
# Summer 2018
#
# This script simulates Langton's ant.
#
# Source:  https://www.futilitycloset.com/2014/04/06/langtons-ant/

import random
import sys
import time

def main():
	LA = LangtonsAnt(10, "empty")
	LA.run(iters=10000, sleeptime=0.2)

class LangtonsAnt:
	"""
		Langton's ant consists of an ant as a point within an n-dimensional grid
	 	with direction. If the ant is on a blank square, it turns right, then
		moves forward. Otherwise, the ant turns left, then moves forward. In
		each case, the abandoned square is inverted.
	"""

	def __init__(self, dims=10, setup="empty"):
		""" Initialize the ant and grid (world, board, etc.) """
		if 1 < dims:
			self.dims = dims
			if setup == "empty":
				self.ant = {"x": dims // 2, "y": dims // 2, "state": " ", "facing": "up"}
				self.board = [[" " for i in range(dims)] for j in range(dims)]
				self.board[self.ant["x"]][self.ant["y"]] = "X"
			elif setup == "random":
				self.ant = {"x": dims // 2, "y": dims // 2, "state": " ", "facing": "up"}
				self.board = [[random.choice([" ", "."]) for i in range(dims)] for j in range(dims)]
				self.board[self.ant["x"]][self.ant["y"]] = "X"

	def __str__(self):
		"""
		 	Returns a string representing the current state of the ant on the
			board.
		"""
		s = ""
		for i in range(self.dims):
			for j in range(self.dims):
				s += str(self.board[i][j]) + " "
			s += "\n"
		return s

	def move(self):
		""" Move the ant according to the ant in its current state of the board. """
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
		"""
		 	Move a number of steps displaying each state. Choose a smaller
			sleeptime to increase the rate of change.
		"""
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
