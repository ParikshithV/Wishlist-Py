from flask import Flask, render_template, url_for, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')
datetime_ind = datetime.now(tz)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
db = SQLAlchemy(app)

class Wishlist(db.Model):
    name = db.Column(db.String(250), primary_key=True)
    link = db.Column(db.String(250))    #add nullable=False
    site_name = db.Column(db.String(100),)
    image = db.Column(db.String(250),)
    price = db.Column(db.Integer, default=0)
    date_added = db.Column(db.DateTime, default=datetime_ind)

    def __repr__(self):
        return '<Item %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        item_name = request.form['content']
        new_item = Wishlist(name=item_name)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error adding item'
    
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