from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()
import datetime



friendship = db.Table('friendship',
    db.Column('from_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('to_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('status', db.Integer())
                      
)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    f_name = db.Column(db.String(250), nullable=False)
    l_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    profile_pic = db.Column(db.String(250), nullable=False)
    dob = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, default= datetime.datetime.utcnow())
    # relations
    post = relationship('Post', back_populates='user')
    react = relationship('React', back_populates='user')
    comment = relationship('Comment', back_populates='user')
    friends = relationship('User', secondary=friendship, primaryjoin=id==friendship.c.from_id, secondaryjoin=id==friendship.c.to_id)

    def follow(self, user):
        if not self.is_friends(user):
            self.friends.append(user)
            return self

    def unfollow(self, user):
        if self.is_firends(user):
            self.friends.remove(user)
            return self

    def is_firends(self, user):
        return self.friends.filter(friendship.c.to_id == user.id).count() > 0
    
    
    def __repr__(self):
        return f"<User {self.id} >"

    def save(self):
        db.session.add(self)
        db.session.commit()

 
    
class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    media = db.Column(db.String(250), nullable=False)
    created_date = db.Column(db.DateTime, default= datetime.datetime.utcnow())
    # relationships
    user = relationship('User', back_populates='post')
    react = relationship('React', back_populates='post')
    comment = relationship('Comment', back_populates='post')
    def __repr__(self):
        return f"<User {self.title} >"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class React(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
    react_on = db.Column(db.DateTime, default= datetime.datetime.utcnow())
    # relationships
    user = relationship('User', back_populates='react')
    post = relationship('Post', back_populates='react')

    def __repr__(self):
        return f"<User {self.reaction} >"


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()    


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
    comment = db.Column(db.String(500), nullable=False)
    comment_on = db.Column(db.DateTime, default= datetime.datetime.utcnow())
    # relationships
    user = relationship('User', back_populates='comment')
    post = relationship('Post', back_populates='comment')

    def __repr__(self):
        return f"<User {self.comment} >"

    def save(self):
        db.session.add(self)
        db.session.commit()
