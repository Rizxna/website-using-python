import sys , os
parent_dir= os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)

from main import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    profile_picture = db.Column(db.String(255))  # Store the image filename or path
    bio = db.Column(db.Text)
    projects = db.relationship('Project', backref='user', lazy=True)
    funds = db.relationship('Funding', backref='user', lazy=True)
    rewards_claimed = db.relationship('RewardClaim', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Project Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    likes = db.Column(db.Integer, default=0)
    bookmarks = db.Column(db.Integer, default=0)
    funds = db.relationship('Funding', backref='project', lazy=True)
    rewards = db.relationship('Reward', backref='project', lazy=True)
    comments = db.relationship('Comment', backref='project', lazy=True)
    updates = db.relationship('ProjectUpdate', backref='project', lazy=True)
    livestreams = db.relationship('Livestream', backref='project', lazy=True)
    project_details = db.relationship('ProjectDetails', backref='project', lazy=True)
    categories = db.relationship('ProjectCategory', secondary='project_category_assoc', backref='projects')
    tags = db.relationship('ProjectTag', secondary='project_tag_assoc', backref='projects')

    def __str__(self):
        return self.title

# Funding Model
class Funding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    funding_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

# Reward Model
class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

# Comment Model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

# HelpCenter Model
class HelpCenter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

# Notification Model
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ProjectDetails Model
class ProjectDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    details_text = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.String(255))
    start_date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))
    funds_raised = db.Column(db.Float)

# Payment Model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

# Livestream Model
class Livestream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    livestream_url = db.Column(db.String(255))
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

# RewardClaim Model
class RewardClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reward_id = db.Column(db.Integer, db.ForeignKey('reward.id'))
    claimed_date = db.Column(db.DateTime(timezone=True), default=func.now())

# ProjectUpdate Model
class ProjectUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    update_text = db.Column(db.Text, nullable=False)
    update_date = db.Column(db.DateTime(timezone=True), default=func.now())
    image = db.Column(db.String(255))

# ProjectCategory Model
class ProjectCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# ProjectTag Model
class ProjectTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# Many-to-Many relationship table for Project and ProjectCategory
project_category_assoc = db.Table('project_category_assoc',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('project_category.id'))
)

# Many-to-Many relationship table for Project and ProjectTag
project_tag_assoc = db.Table('project_tag_assoc',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('project_tag.id'))
)
