from flask import Flask, request
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, TEXT, Date
from flask_migrate import Migrate
from config import connection_string
from datetime import datetime
import json
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

@app.route('/index', methods=['POST', 'GET'])
def short_form_post():

    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        variable = json.loads(resp)
        if type(variable["price"]) != Integer:
            return "invalid name" 
        elif re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',variable["email"].lower() != True):
            return "invalid email please try again"
        elif type(variable["SSN"]) != Integer:
             return "invalid SSN"
        elif type(variable["birthday"]) != String:
            return "invalid birthday, please enter the correct date"
        elif type(variable["zip"]) != Integer:
            return "invalid Zip, please enter the correct numbering"
        else:
            db.session.merge(resp)
            db.session.commit()
    return True


@app.route('/LongFormStep1', methods=['POST', 'GET'])
def long_form_step1_post():
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        variable = json.loads(resp)
        if type(variable["first_name"]) != String:
            return "invalid first_name"
        elif type(variable["last_name"]) != String:
            return "invalid last_name"
        elif type(variable["street_adress"]) != String:
            return "invalid street_adress"
        elif type(variable["city"]) != String:
            return "invalid city"
        elif type(variable["zip"]) != Integer:
            return "invalid zip"
        elif type(variable["phone"]) != Integer:
            return "invalid phone"
        elif type(variable["mobil_phone"]) != Integer:
            return "invalid mobil_phone"
        elif re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',variable["email"].lower() != True):
            return "invalid email please try again"
        elif type(variable["social_security"]) != Integer:
            return "invalid social_security"
        elif type(variable["driver_license"]) != Integer:
             return "invalid driver_license"
        else:
            db.session.merge(resp)
            db.session.commit()
    return True


@app.route('/LongFormStep2', methods=['POST', 'GET'])
def long_form_step2_post():
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        variable = json.loads(resp)
        if type(variable["company_name"]) != String:
            return "invalid company_name"
        elif type(variable["position"]) != String:
            return "invalid position"
        elif type(variable["work_phone"]) != Integer:
            return "invalid work_phone"
        else:
            db.session.merge(resp)
            db.session.commit()
    return True


@app.route('/LongFormStep3', methods=['POST', 'GET'])
def long_form_step3_post():
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        variable = json.loads(resp)
        if type(variable["aba"]) != Integer:
            return "invalid ABA/Routing#"
        elif type(variable["bank_name"]) != String:
            return "invalid bank_name"
        elif type(variable["checking_account"]) != Integer:
            return "invalid checking_account"
        else:
            db.session.merge(resp)
            db.session.commit()
    return True
        

if __name__ == '__main__':
    app.run()