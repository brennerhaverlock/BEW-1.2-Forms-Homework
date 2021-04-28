from sqlalchemy_utils import URLType

from grocery_app import db
from grocery_app.utils import FormEnum

from flask_login import UserMixin


class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'

class GroceryStore(db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    items = db.relationship('GroceryItem', back_populates='store')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

    def __str__(self):
        return f'<Store: {self.title}>'

    def __repr__(self):
        return f'<Store: {self.title}>'

class GroceryItem(db.Model):
    """Grocery Item model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    store_id = db.Column(
        db.Integer, db.ForeignKey('grocery_store.id'), nullable=False)
    store = db.relationship('GroceryStore', back_populates='items')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    users_cart = db.relationship('User', secondary='shopping_cart', back_populates='cart_items')


    def __str__(self):
        return f'<Item: {self.name}>'

    def __repr__(self):
        return f'<Item: {self.name}>'

class User(UserMixin, db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    cart_items = db.relationship('GroceryItem', secondary='shopping_cart', back_populates='users_cart')

    def __str__(self):
        return f'{self.username}'

    def __repr__(self):
        return f'{self.username}'

shopping_cart = db.Table('shopping_cart',
    db.Column('item_id', db.Integer, db.ForeignKey('grocery_item.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)