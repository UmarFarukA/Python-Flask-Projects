from App.extensions import (db, Column, String, Integer, ForeignKey, Date, ma)


class Category(db.Model):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    post = db.relationship("Post", backref="category", lazy=True)


    def __init__(self, name):
        """This function initialiazes category
           Parameter:
            name (string): The name of category
        """
        self.name = name
    
    def insert(self):
        """This function create a new category"""
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """This function updates a category"""
        db.session.commit()

    def delete(self):
        """This function deletes a category"""
        db.session.delete()
        db.session.commit()


class CategorySchema(ma.Schema):
    """This class defines the schema for loading data"""
    class Meta:
        fields = ("name")
        model = Category

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)