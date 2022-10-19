from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreateProductForm(FlaskForm):
    name = StringField(
        label="Item name:",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
