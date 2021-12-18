class Player:
	def __init__(self, x, y, c):
		self.x = x
		self.y = y
		self.c = c

	def __str__(self):
		return f"X = {self.x}, Y = {self.y}"

