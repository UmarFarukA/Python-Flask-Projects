from app.extension import db

class Question(db.Model):
    """This class represents the Question Model"""
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f'<Question {self.content}>'
    
    def insert(self):
        """A function that add new question to db"""
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """A function that updates a questions"""
        db.session.commit()
    
    def delete(self):
        """A function that delete a questions from the database"""
        db.session.delete(self)
        db.session.commit()