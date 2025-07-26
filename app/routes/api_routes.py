from flask import Blueprint, jsonify
from ..models import Product

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify([p.serialize() for p in products])
