from flask import Flask, render_template, url_for, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import time

import requests
from bs4 import BeautifulSoup

tz = pytz.timezone('Asia/Kolkata')
datetime_ind = datetime.now(tz)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
db = SQLAlchemy(app)

class Wishlist(db.Model):
    name = db.Column(db.String(250), primary_key=True)
    link = db.Column(db.String(250))    #add nullable=False
    site_name = db.Column(db.String(100),)
    image = db.Column(db.Unicode)
    price = db.Column(db.String(250), default=0)
    date_added = db.Column(db.DateTime, default=datetime_ind)

    def __repr__(self):
        return '<Item %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        item_name = request.form['content']

        # try:
        req = requests.get(item_name)
        soup = BeautifulSoup(req.content,'html.parser')
        price = soup.find('span',id="our_price_display").string
        name = soup.find('h2', class_ = "product-name").string
        image = soup.find_all('img')
        image_link = image[2]['src']
        time.sleep(3)
        new_item = Wishlist(name=name, link=item_name, site_name='SSS', image=image_link, price=price)

        db.session.add(new_item)
        db.session.commit()
        return redirect('/')
        # except:
        #     return 'Error adding item'
    
    else:
        items = Wishlist.query.order_by(Wishlist.date_added).all()
        return render_template('index.html', items=items)

@app.route('/delete/<string:name>')
def delete(name):
    item_to_delete = Wishlist.query.get_or_404(name)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error deleting data'

if __name__ == "__main__":
    app.run(debug=True)