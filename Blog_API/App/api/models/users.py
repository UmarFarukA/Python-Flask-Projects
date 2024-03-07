from datetime import datetime
from App.extensions import (db, Column, String, Integer, Date, ValidationError, UserMixin, 
                            login_manager, ma, mail
)
@login_manager
def login_user(user_id):
    """This function defines the load user used of logging users
    Parameter:
        user_id (int): The user Id
    Return:
        User: queried from the database
    """
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(50), nullable=False)
    mname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    photo = Column(String(150), nullable=True)
    role = Column(String(50), nullable=False, default="user")
    post = db.relationship("Post", backref="user", lazy=True)
    created_at = Column(Date(), default=datetime.utcnow())


    def __init__(self, email, name, mname, lname, password, photo):
        """This defines the init method
            Parameters:
                name (string): The user name
                mname (string): The user middle name
                lname (string): The user last name
                email (string): the user email
                password (string): The password of the user
                photo (string): The user photo
        """
        self.email = email
        self.password = password
        self.name = name
        self.mname = mname
        self.lname = lname
        self.photo = photo

    
    def insert(self):
        """This function create new user and add to database"""
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """This functioin update users data"""
        db.session.commit()

    
    def delete(self):
        """This function deletes the user"""
        db.session.delete()
        db.session.commit()

    def validate_email(self, email):
        """This function check for existance of an email, if found
            raise a validation error
            Parameter:
                email (string): User email
        """
        email = Users.query.filter_by(email == email.data)
        if(email):
            raise ValidationError(f"{self.name} already exists with this mail")


class UsersSchema(ma.Schema):
     """This class defines the User schema for fetching data"""
     class Meta:
         fields = ("id", "email", "name", "mname", "lname", "photo")
         model = Users


# Creating an instance of the UserSchema class
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)