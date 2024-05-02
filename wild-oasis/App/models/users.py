import uuid
from utils import current_date, ValidationError
from App.extension import db, bcrypt, UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String, unique=True, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, fname, lname, image, password):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.image = image
        self.password = self.set_password(password)
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def validate_email(self):
        email = User.query.filter_by(email = self.email).first()
        if email:
            raise ValidationError(f"{email} has already been used, kindly log in")

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.update()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

    