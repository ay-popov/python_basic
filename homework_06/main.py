from flask import Flask, request, render_template, url_for, redirect
from flask_migrate import Migrate
from os import getenv
import config

from models import db, Product

from forms import CreateProductForm

app = Flask(__name__)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/", endpoint="index_page")
def index_page():
    return render_template("index.html")


@app.route("/about/", endpoint="about_page")
def about_page():
    return render_template("about.html")


@app.route("/list/", endpoint="list_page")
def list_page():
    products = Product.query.order_by(Product.id).all()
    return render_template("list.html", products=products)


@app.route("/add/", methods=["GET", "POST"], endpoint="add_page")
def add_product():
    form = CreateProductForm()

    if request.method == "GET":
        return render_template("add.html", form=form)

    if not form.validate_on_submit():
        return render_template("add.html", form=form), 400

    product_name = form.name.data

    product = Product(name=product_name)
    db.session.add(product)
    db.session.commit()

    url = url_for("list_page")
    return redirect(url)


@app.route(
    "/<int:product_id>/",
    methods=["GET", "DELETE"],
    endpoint="delete_page",
)
def get_product_by_id(product_id: int):

    product: Product = Product.query.get_or_404(
        product_id,
        f"Product #{product_id} not found!",
    )

    db.session.delete(product)
    db.session.commit()

    url = url_for("list_page")
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)
