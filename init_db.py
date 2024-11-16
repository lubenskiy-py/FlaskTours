from models import Tur, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    tur1 = Tur(title="kiev to odesa", 
               price=9.5, 
               description="a ride from kiev to odesa", 
               is_booked=True)
    tur2 = Tur(title="kiev to lviv", 
               price=13.5, 
               description="a ride from kiev to lviv")
    tur3 = Tur(title="kiev to moldova", 
               price=15.5, 
               description="a ride from kiev to molodova", 
               is_booked=True)
    db.session.add_all([tur1, tur2, tur3])
    db.session.commit()