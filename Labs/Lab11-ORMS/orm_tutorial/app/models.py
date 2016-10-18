from app import db

# Your Customer Database code should go here


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<customer %r>' % self.id
