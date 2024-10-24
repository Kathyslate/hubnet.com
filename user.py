from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()  # Ensure this is initialized in your application file

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    
    # New fields
    is_digital_marketer = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
    rating = db.Column(db.Float, default=0.0)
    views_count = db.Column(db.Integer, default=0)
    experience_years = db.Column(db.Integer, default=0)

    # Relationships
    videos = db.relationship('Video', backref='user', lazy=True)
    images = db.relationship('Image', backref='user', lazy=True)
    pending_jobs = db.relationship('Job', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Define the Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define the Image model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='pending')  # Job status (pending, completed, etc.)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

