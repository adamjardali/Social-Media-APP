from config.database import Base 
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship 
from datetime import datetime
var_length = 100





class User(Base):
	__tablename__ = 'Users'
	id = Column(Integer,primary_key = True, index = True)
	name = Column(String(var_length),nullable = False)
	email = Column(String(var_length), nullable = False, unique = True)
	password = Column(String(var_length), nullable = False)
	created_at = Column(DateTime, nullable  = False, default = datetime.utcnow)
	image = Column(String(var_length),default = "new_user.png")
	date_of_birth = Column(DateTime)
	posts = relationship('Task', back_populates = 'creator')

class Task(Base):
	__tablename__ = 'Posts'
	id = Column(Integer,primary_key = True, index = True)
	title = Column(String(var_length),nullable = False, default = 'No title')
	description = Column(String(var_length),nullable = False, default = 'No description')
	post_type = Column(String, nullable = False, default = "Feelings")
	user_id = Column(Integer,ForeignKey('Users.id',ondelete = "CASCADE"))
	creator = relationship('User',back_populates = 'posts')
	created_at = Column(DateTime, nullable  = False, default = datetime.utcnow)

class Like(Base):
    __tablename__ = "Likes"

    user_id = Column(Integer, ForeignKey(
        "Users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "Posts.id", ondelete="CASCADE"), primary_key=True)