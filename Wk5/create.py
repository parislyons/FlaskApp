from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Paris',last_name='Lyons')
db.session.add(testuser)
db.session.commit()