from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask import render_template, request, redirect, url_for 
import os 

file_path = os.path.abspath(os.getcwd())+"/scores.db"

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path 
db = SQLAlchemy(app)

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

@app.route('/') 
def index(): 
	return render_template('index.html') 

@app.route('/leaderboard')
def leaderboard():
    scores = Score.query.order_by(Score.score.desc()).limit(10).all()
    return render_template('leaderboard.html', scores=scores)


@app.route('/add_score', methods=['POST'])
def add_score():
    if request.method == 'POST':
        username = request.form['username']
        score_value = int(request.form['score'])
        new_score = Score(username, score_value)
        db.session.add(new_score)
        db.session.commit()
        return redirect(url_for('leaderboard'))
    else:
        return "Method Not Allowed", 405
  
if __name__ == '__main__': 
    db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)

