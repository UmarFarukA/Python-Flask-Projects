from App.extensions import (db, Column, Integer, ma)


class Likes(db.Model):
    __tablename__ = "likes"
    post_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

class LikesSchema(ma.Schema):
    class Meta:
        fields = ("post_id", "user_id")
        model = Likes

category_schema = LikesSchema()
categories_schema = LikesSchema(many=True)