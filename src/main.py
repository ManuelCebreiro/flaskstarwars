"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Vehicles

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#TODOS LOS ENDPOINTS DE USERS

@app.route('/user', methods=['GET'])
def handle_hello():

    user = [x.serialize() for x in User.query.all()]
    return jsonify(user), 200

#LLAMAR A TODOS LOS USUARIOS

@app.route('/favoritos/<int:user_id>', methods=['GET'])
def favoritesUser(user_id):
    user1 = User.query.get(user_id)
    person = [x.serialize() for x in user1.peoplefavoritos]
    planet =  [i.serialize() for i in user1.planetsfavoritos]
    vehicle = [y.serialize() for y in user1.vehiclesfavoritos]
    allfavorites = [ person + planet + vehicle]

    return jsonify(allfavorites), 200


#LLAMAR A LOS FAVORITOS DE UN USUARIO

@app.route('/personaje/<int:user_id>/<int:person_id>', methods=['POST'])
def addPersonFavorite(person_id, user_id):
    user1 = User.query.get(user_id)
    person = People.query.get(person_id)

    if person in user1.peoplefavoritos:
        return "Este personaje ya está en favoritos", 400
    else:
        user1.peoplefavoritos.append(person)
        db.session.commit()
        return "Personaje añadido", 200

#AÑADIR PERSONAJE FAVORITO

@app.route('/personaje/<int:user_id>/<int:person_id>', methods=['DELETE'])
def deletePersonFavorite(person_id, user_id):
    user1 = User.query.get(user_id)
    person = People.query.get(person_id)

    if person not in user1.peoplefavoritos:
        return "Este personaje ya no está en favoritos", 400
    else:
        user1.peoplefavoritos.remove(person)
        db.session.commit()
        return "Personaje eliminado", 200

#ELIMINAR PERSONAJE FAVORITO

@app.route('/planet/<int:user_id>/<int:planet_id>', methods=['POST'])
def addPlanetFavorite(planet_id, user_id):
    user1 = User.query.get(user_id)
    planet = Planets.query.get(planet_id)

    if planet in user1.planetsfavoritos:
        return "Este planeta ya está en favoritos", 400
    else:
        user1.planetsfavoritos.append(planet)
        db.session.commit()
        return "Planeta añadido", 200

#AÑADIR PLANETA FAVORITO

@app.route('/planet/<int:user_id>/<int:planet_id>', methods=['DELETE'])
def deletePlanetFavorite(planet_id, user_id):
    user1 = User.query.get(user_id)
    planet = Planets.query.get(planet_id)

    if planet not in user1.planetsfavoritos:
        return "Este planeta ya no está en favoritos", 400
    else:
        user1.planetsfavoritos.remove(planet)
        db.session.commit()
        return "Planeta eliminado", 200

#ELIMINAR PLANETA FAVORITO

@app.route('/vehicles/<int:user_id>/<int:vehicles_id>', methods=['POST'])
def addVehiclesFavorite(vehicles_id, user_id):
    user1 = User.query.get(user_id)
    vehicles = Vehicles.query.get(vehicles_id)

    if vehicles in user1.vehiclesfavoritos:
        return "Este vehiculo ya está en favoritos", 400
    else:
        user1.vehiclesfavoritos.append(vehicles)
        db.session.commit()
        return "Vehiculo añadido", 200

#AÑADIR VEHICLES FAVORITO

@app.route('/vehicles/<int:user_id>/<int:vehicles_id>', methods=['DELETE'])
def deleteVehiclesFavorite(vehicles_id, user_id):
    user1 = User.query.get(user_id)
    vehicles = Vehicles.query.get(vehicles_id)

    if vehicles not in user1.vehiclesfavoritos:
        return "Este vehiculo ya no está en favoritos", 400
    else:
        user1.vehiclesfavoritos.remove(vehicles)
        db.session.commit()
        return "Vehiculo eliminado", 200

#ELIMINAR PLANETA FAVORITO

#TODOS LOS ENDPOINTS DE PEOPLE

@app.route('/people', methods=['GET'])
def getPeople():
    people = People.query.all()
    return jsonify([person.serialize() for person in people]), 200

#LLAMAR A TODOS LOS PERSONAJES

@app.route('/people/<int:people_id>', methods=['GET'])
def getPeopleSingle(people_id):

    # user1 = People.query.get(people_id)
    user1 = People.query.filter_by(id = people_id).first()
    return jsonify(user1.serialize())

#LLAMAR A UN PERSONAJE INDIVIUAL

#TODOS LOS ENDPOINTS DE PLANETS

@app.route('/planets', methods=['GET'])
def getPlanets():

    planets = Planets.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

#LLAMAR A TODOS LOS PLANETAS

@app.route('/planets/<int:planet_id>', methods=['GET'])
def getPlanetSingle(planet_id):

    user1 = Planets.query.filter_by(id = planet_id).first()
    return jsonify(user1.serialize())

#LLAMAR A UN PLANETA INDIVIDUAL

#TODOS LOS ENDPOINTS DE VEHICLES

@app.route('/vehicles', methods=['GET'])
def getVehicles():

    vehicles = Vehicles.query.all()

    return jsonify([vehicle.serialize() for vehicle in vehicles]), 200

#LLAMAR A TODOS LOS VEHICULOS

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def getVehiclesSingle(vehicle_id):

    user1 = Vehicles.query.filter_by(id = vehicle_id).first()
    return jsonify(user1.serialize())

#LLAMAR A VEHICULOS INDIVIDUAL










# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

# @app.route('/peoplefavoritos/<user_id>', methods=['GET'])
# def handle(user_id):

#     peoplefavoritos 
    
#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

