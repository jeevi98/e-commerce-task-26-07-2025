from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .. import db
from ..models import Product

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/')
def list_products():
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@product_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        new_product = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            image_url=request.form['image_url']
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('product.list_products'))
    return render_template('add_product.html')

@product_bp.route('/delete/<int:id>')
@login_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product.list_products'))
