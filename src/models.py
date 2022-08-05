from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    pasword = db.Column(db.String(250), nullable=False)
    peoplefavoritos = db.relationship('PeopleFavoritos', lazy=True)
    planetfavoritos = db.relationship('PlanetFavoritos', lazy=True)
    vehiclesfavoritos = db.relationship('VehiclesFavoritos', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class PeopleFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    people_id = db.Column(db.Integer, ForeignKey('People.id'))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }

class PlanetFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    planet_id = db.Column(db.Integer, ForeignKey('Planet.id'))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class VehiclesFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    vehicles_id = db.Column(db.Integer, ForeignKey('Vehicles.id'))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicles_id": self.vehicles_id
        }

class People(db.Model):
    id = db.Column(db.Integer, ForeignKey('Peoplefavoritos.UserId'), primary_key=True,)
    Name = db.Column(db.String(250))
    Birthday = db.Column(db.String(250))
    Gender = db.Column(db.String(250))
    Height = db.Column(db.String(250))
    Skin_color = db.Column(db.String(250))
    Eye_color = db.Column(db.String(250))
    peoplefavoritos = db.relationship('PeopleFavoritos', lazy=True)
    planetfavoritos = db.relationship('PlanetFavoritos', lazy=True)
    vehiclesfavoritos = db.relationship('VehiclesFavoritos', lazy=True)


    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Planets(db.Model):
    PlanetId = db.Column(db.Integer, ForeignKey('Planetfavoritos.UserId'), primary_key=True,)
    Name = db.Column(db.String(250))
    Population = db.Column(db.String(250))
    Climate = db.Column(db.String(250))
    Terrain = db.Column(db.String(250))
    Rotation_period = db.Column(db.String(250))
    Orbital_period = db.Column(db.String(250))
    peoplefavoritos = db.relationship('PeopleFavoritos', lazy=True)
    planetfavoritos = db.relationship('PlanetFavoritos', lazy=True)
    vehiclesfavoritos = db.relationship('VehiclesFavoritos', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Vehicles(db.Model):
    VehiclesId = db.Column(Integer, ForeignKey('Vehiclesfavoritos.UserId'), primary_key=True,)
    Name = db.Column(db.String(250))
    Model = db.Column(db.String(250))
    Vehicles_class = db.Column(db.String(250))
    Length = db.Column(db.String(250))
    Cargo_capacity = db.Column(db.String(250))
    Max_Speed = db.Column(db.String(250))
    peoplefavoritos = db.relationship('PeopleFavoritos', lazy=True)
    planetfavoritos = db.relationship('PlanetFavoritos', lazy=True)
    vehiclesfavoritos = db.relationship('VehiclesFavoritos', lazy=True)
    
    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email
        }