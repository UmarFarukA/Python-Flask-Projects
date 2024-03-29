from flask import render_template
import config
from flask_migrate import Migrate

from models import People

app = config.connex_app
migrate = Migrate(app, config.db)

app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = People.query.all()
    return render_template("home.html", people = people)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
