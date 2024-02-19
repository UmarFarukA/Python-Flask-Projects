from app.extension import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text)


    def __repr__(self) -> str:
        return f'<Post "{self.title}">'
    
    def insert(self):
        """A function that add new post to database"""
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """A function that updates a Posts"""
        db.session.commit()
    
    def delete(self):
        """A function that delete a post from the database"""
        db.session.delete(self)
        db.session.commit()