from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

PeopleFavoritos = db.Table('PeopleFavoritos',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True)
)
PlanetsFavoritos = db.Table('PlanetsFavoritos',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planets_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True)
)
VehiclesFavoritos = db.Table('VehiclesFavoritos',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('vehicles_id', db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)
    
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),  nullable=False)
    email = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    pasword = db.Column(db.String(250), nullable=False)
    peoplefavoritos = db.relationship('People', secondary=PeopleFavoritos, lazy='subquery', backref=db.backref('users', lazy=True))
    planetsfavoritos = db.relationship('Planets', secondary=PlanetsFavoritos, lazy='subquery', backref=db.backref('user', lazy=True))
    vehiclesfavoritos = db.relationship('Vehicles', secondary=VehiclesFavoritos, lazy='subquery', backref=db.backref('user', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "username": self.name,
            "email": self.email
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(250))
    birthday = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    height = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))


    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    Name = db.Column(db.String(250))
    Population = db.Column(db.String(250))
    Climate = db.Column(db.String(250))
    Terrain = db.Column(db.String(250))
    Rotation_period = db.Column(db.String(250))
    Orbital_period = db.Column(db.String(250))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            # "username": self.username,
            # "email": self.email
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    Name = db.Column(db.String(250))
    Model = db.Column(db.String(250))
    Vehicles_class = db.Column(db.String(250))
    Length = db.Column(db.String(250))
    Cargo_capacity = db.Column(db.String(250))
    Max_Speed = db.Column(db.String(250))
    
    def __repr__(self):
        return '<Person %r>' % self.username

    # def serialize(self):
    #     return {
    #         "username": self.username,
    #         "email": self.email
    #     }