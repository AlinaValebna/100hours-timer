from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import db, Timer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    timers = Timer.query.all()
    return render_template("index.html", timers=timers)

@app.route("/add", methods=["POST"])
def add_timer():
    name = request.form["project_name"]
    if not Timer.query.filter_by(project_name=name).first():
        new_timer = Timer(
            project_name=name,
            remaining_seconds=360000,
            is_paused=True,
            last_updated=datetime.now()
        )
        db.session.add(new_timer)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/toggle/<int:timer_id>")
def toggle_timer(timer_id):
    timer = Timer.query.get(timer_id)
    now = datetime.now()
    if not timer.is_paused:
        elapsed = (now - timer.last_updated).total_seconds()
        timer.remaining_seconds = max(0, timer.remaining_seconds - int(elapsed))
    timer.is_paused = not timer.is_paused
    timer.last_updated = now
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
