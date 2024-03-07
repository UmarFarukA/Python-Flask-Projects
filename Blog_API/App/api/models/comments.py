from datetime import datetime
from App.extensions import (db, Column, String, Integer, ForeignKey, Date, ma)


class Comments(db.Model):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(Date, default=datetime.utcnow())


    def __init__(self, content, post_id, user_id):
        """This function initialiazes category
           Parameter:
            content (string): The content of comments
            post id (integer): The id of post commented on
            user id (integer): The user id that commented on a post
        """
        self.name = content
        self.post_id = post_id
        self.user_id = user_id
    
    def insert(self):
        """This function create a new comment"""
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """This function updates a comment"""
        db.session.commit()

    def delete(self):
        """This function deletes a comment"""
        db.session.delete()
        db.session.commit()


class CommentSchema(ma.Schema):
    """This class defines the schema for loading data"""
    class Meta:
        fields = ("name")
        model = Comments

category_schema = CommentSchema()
categories_schema = CommentSchema(many=True)