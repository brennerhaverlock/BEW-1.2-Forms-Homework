from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField("Title")
    address = StringField("Address")
    submit = SubmitField("Submit")
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name')
    price = FloatField('Price')
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo URL')
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query.all())
    submit = SubmitField('Submit')
