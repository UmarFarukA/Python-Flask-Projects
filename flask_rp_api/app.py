from flask import render_template
from models.users import User
from models.notes import Note
import config


# Initialize Connexion app 
app = config.connex_app
app.add_api(config.basedir / "swagger.yaml")

# Index route
@app.route("/")
def home():
    users = User.query.join(Note, User.id == Note.user_id).all()
    return render_template("home.html", users=users)

# Entry point
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)