class Player:
	def __init__(self, x, y,  clr):
		self.x = x
		self.y = y
		self.clr = clr

	def __str__(self):
		return f"X = {self.x}, Y = {self.y}, COLOR = {self.clr}"
