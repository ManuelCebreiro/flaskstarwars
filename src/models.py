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
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(250))
    birthday = db.Column(db.Integer)
    gender = db.Column(db.String(250))
    height = db.Column(db.Integer)
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,
            "birthday": self.birthday,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            # "homeplanet": self.homeplanet.name
        }
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(250))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    vehicles_class = db.Column(db.String(250))
    length = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    max_Speed = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,
            "model": self.model,
            "vehicles_class": self.vehicles_class,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity,
            "max_Speed": self.max_Speed
        }