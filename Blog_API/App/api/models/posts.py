from datetime import datetime
from App.extensions import (db, Column, String, Integer, ForeignKey, Date, ma)


class Posts(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    image = Column(String(250), nullable=True)
    created_at = Column(Date, nullable=False, default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    cat_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    comments = db.relationship("Comments", backref="posts", lazy=True)
    user = db.relationship("Comments", backref="users", lazy=True)

    def __init__(self, title, content, image, user_id, cat_id):
        """This defines the init method
            Parameters:
                title (string): The post title
                content (string): The post content
                image (string): The post image
                User_id (Integer): the user id creating the post
                category id (Integer): The category the post belongs to
        """
        self.title = title
        self.content = content
        self.image = image
        self.user_id = user_id
        self.cat_id = cat_id
    
    def insert(self):
        """This function create new post and add to database"""
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """This functioin update post data"""
        db.session.commit()

    def delete(self):
        """This function deletes the post"""
        db.session.delete()
        db.session.commit()


class PostSchema(ma.Schema):
    """This class defines the Post schema for fetching data"""
    class Meta:
        fields = ("id", "title", "content", "category", "users")
        model = Posts


# Creating an instance of Posts class
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
