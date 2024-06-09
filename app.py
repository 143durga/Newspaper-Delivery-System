from flask import Flask, render_template, request, redirect, url_for
from models import db, Customer, Bill
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact_info = request.form['contact_info']
        delivery_schedule = request.form['delivery_schedule']

        new_customer = Customer(name=name, address=address, contact_info=contact_info, delivery_schedule=delivery_schedule)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/billing', methods=['GET', 'POST'])
def billing():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        amount = request.form['amount']
        description = request.form['description']
        date = datetime.now()

        new_bill = Bill(customer_id=customer_id, amount=amount, date=date, description=description)
        db.session.add(new_bill)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('billing.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

