from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), unique=True, nullable=False)
    total_seconds = db.Column(db.Integer, default=360000)  # 100 hours
    remaining_seconds = db.Column(db.Integer)
    is_paused = db.Column(db.Boolean, default=True)
    last_updated = db.Column(db.DateTime)
