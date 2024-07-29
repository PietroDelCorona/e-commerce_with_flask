from flask import render_template
from market import app
from market.models import Item

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market():
    items = Item.query.all()
    return render_template("market.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)