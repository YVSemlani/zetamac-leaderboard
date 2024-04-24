from app import db 

class Score(db.Model): 
	__tablename__ = 'scores'
	id = db.Column(db.Integer, primary_key=True) 
	score = db.Column(db.Integer)
	username = db.Column(db.String(50))

	def __init__(self, username, scores):
		self.username = username
		self.score = scores

	def __repr__(self): 
		return f"Leaderboard(score={self.score}, username={self.username})"
