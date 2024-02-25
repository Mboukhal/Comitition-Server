from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime


import test

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bonjour_le_monde = db.Column(db.Boolean, default=False)
    entree_utilisateur = db.Column(db.Boolean, default=False)
    calculatrice_de_base = db.Column(db.Boolean, default=False)
    convertisseur_temperature = db.Column(db.Boolean, default=False)
    calculateur_surface = db.Column(db.Boolean, default=False)
    convertisseur_devise = db.Column(db.Boolean, default=False)
    generateur_mot_de_passe = db.Column(db.Boolean, default=False)
    obtenir_adresse_ip = db.Column(db.Boolean, default=False)
    points = db.Column(db.Integer, default=0)
    
    bonjour_le_monde_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    entree_utilisateur_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    calculatrice_de_base_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    convertisseur_temperature_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    calculateur_surface_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    convertisseur_devise_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    generateur_mot_de_passe_last_update = db.Column(db.DateTime, default=None, onupdate=None)
    obtenir_adresse_ip_last_update = db.Column(db.DateTime, default=None, onupdate=None)


# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        username = request.json.get('username')

        if username:
            new_user = User(username=username)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "User added successfully"})
        else:
            return jsonify({"error": "Username cannot be null or empty"})
    except Exception as e:
        return jsonify({"error": str(e)})


# Endpoint to get all columns for a user by username
@app.route('/get_user_columns/<username>', methods=['GET'])
def get_user_columns(username):
    
    try:
        user = User.query.filter_by(username=username).first()

        if user:
            # Return the columns for the user
            return jsonify({
                "username": user.username,
                "bonjour_le_monde": user.bonjour_le_monde,
                "entree_utilisateur": user.entree_utilisateur,
                "calculatrice_de_base": user.calculatrice_de_base,
                "convertisseur_temperature": user.convertisseur_temperature,
                "calculateur_surface": user.calculateur_surface,
                "convertisseur_devise": user.convertisseur_devise,
                "generateur_mot_de_passe": user.generateur_mot_de_passe,
                "obtenir_adresse_ip": user.obtenir_adresse_ip,
                "points": user.points
            })
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        
        # print(str(e))
        return jsonify({"error": str(e)})

# Routes and other application logic...



@app.route('/test', methods=['POST'])
def test_input():
    # try:
        # Get the input from the client
        input_script = request.json['code']
        level = request.json['level']
        user_name = request.json['user_name']
        
        res = False
        points = 0
        
        user = User.query.filter_by(username=user_name).first()

        match level:
        
            case 1:
                res = test.test1(input_script)
                # Update the user's points
                if res:
                    user.points += 5
                    points = user.points
                    user.bonjour_le_monde = True
                    db.session.commit()
            case 2:
                res = test.test2(input_script, user_name)
                if res:
                    user.points += 10
                    points = user.points
                    user.entree_utilisateur = True
                    db.session.commit()
            case 3:
                res = test.test3(input_script, user_name)
                if res:
                    user.points += 15
                    points = user.points
                    user.calculatrice_de_base = True
                    db.session.commit()
            case 4:
                res = test.test4(input_script, user_name)
                if res:
                    user.points += 10
                    points = user.points
                    user.convertisseur_temperature = True
                    db.session.commit()
            case 5:
                res = test.test5(input_script, user_name)
                if res:
                    user.points += 10
                    user.convertisseur_devise = True
                    points = user.points
                    db.session.commit()
            case 6:
                res = test.test6(input_script, user_name)
                if res:
                    user.points += 14
                    points = user.points
                    user.calculateur_surface = True
                    db.session.commit()
            case 7:
                res = test.test7(input_script, user_name)
                if res:
                    user.points += 16
                    points = user.points
                    user.generateur_mot_de_passe = True
                    db.session.commit()
            case 8:
                res = test.test8(input_script, user_name)
                if res:
                    user.points += 22
                    points = user.points
                    user.obtenir_adresse_ip = True
                    db.session.commit()
                
                
                
                
        
        

        # Return the test result to the client
        if res:
            return jsonify({"result": res, "points": points, "progress":{
                    "username": user.username,
                    "bonjour_le_monde": user.bonjour_le_monde,
                    "entree_utilisateur": user.entree_utilisateur,
                    "calculatrice_de_base": user.calculatrice_de_base,
                    "convertisseur_temperature": user.convertisseur_temperature,
                    "calculateur_surface": user.calculateur_surface,
                    "convertisseur_devise": user.convertisseur_devise,
                    "generateur_mot_de_passe": user.generateur_mot_de_passe,
                    "obtenir_adresse_ip": user.obtenir_adresse_ip,
                    "points": user.points
                }})
        else:
            return jsonify({"error": res})

    # except Exception as e:
    #     print(str(e))
    #     return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
