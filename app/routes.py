from flask import render_template, request, redirect, url_for 
from app import app 
from app.models import Score 
from app import db


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
