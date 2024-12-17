from app import db
from datetime import datetime

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.String(255), unique=True, nullable=False)
    openai_thread_id = db.Column(db.String(255), nullable=True)  # Nuevo campo
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    messages = db.relationship("Message", backref="thread", lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey("thread.id"), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "user" o "assistant"
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
