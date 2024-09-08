from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    #is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        #return '<User %r>' % self.username
        return f'<Users {self.id} - {self.email}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(50))

    def __repr__(self):
        return f'<Planets {self.id} - {self.name}>'

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "diameter": self.diameter,
                "rotation_period": self.rotation_period,
                "orbital_period": self.orbital_period,
                "gravity": self.gravity
                }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Enum('Female', 'Male', name="gender"))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))

    def __repr__(self):
        return f'<People {self.id} - {self.name}>'

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "gender": self.gender,
                "height": self.height,
                "mass": self.mass,
                "hair_color": self.hair_colo
                }

class FavoritePlanets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), unique=False, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    user_to = db.relationship('Users', foreign_keys=[users_id])
    planets_to = db.relationship('Planets', foreign_keys=[planets_id])

    def __repr__(self):
        return f'<FavoritePlanets {self.id} - {self.planets_id} - {self.users_id}>'
    
    def serialize(self):
        return {"id": self.id,
                "planets_id": self.planets_id,
                "users_id": self.users_id
                }

class FavoritePeople(db.Model):
    __tablename__ = 'favorite_people'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_to = db.relationship('Users', foreign_keys=[users_id])
    people_to = db.relationship('People', foreign_keys=[people_id])

    def __repr__(self):
        return f'<FavoritePeople {self.id} - {self.people_id} - {self.users_id}>'
    
    def serialize(self):
        return {"id": self.id,
                "people_id": self.people_id,
                "users_id": self.users_id,
                }