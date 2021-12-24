class Player:
	def __init__(self, btn,  clr):
		self.btn = btn
		self.clr = clr

	def __str__(self):
		return f"BTN = {self.btn}, COLOR = {self.clr}"