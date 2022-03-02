from flask import flash
from flask_bcrypt import Bcrypt
import re
from flask_app.config.mySQLConnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['id']

    @staticmethod
    def validate_user(user):
        is_Valid = True
        if len(user['first_name']) < 5:
            flash("First name must be at least 5 characters.")
            is_Valid = False
        if len(user['last_name']) < 5:
            flash("Last name must be at least 5 characters.")
            is_Valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Not a valid Email.")
            is_Valid = False
        if len(user['password']) < 8:
            flash("You're password isn't long enough.")
            is_Valid = False
        if (user['password'] != user['confirm_password']):
            flash("Passwords do not match.")
            is_Valid = False
        return is_Valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())";
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return results

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        
        return cls(results[0])