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

class ShortForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    last_4_of_ssn = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.String(20), nullable=False)
    zip = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self . username


class LongFormStep1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(String(80), nullable=False)
    last_name = db.Column(String(80), nullable=False)
    street_adress = db.Column(String(120), nullable=False)
    code_city = db.Column(String(2), nullable=False)
    city = db.Column(String(40), nullable=False)
    zip = db.Column(Integer, nullable=False)
    phone = db.Column(Integer, nullable=False)
    mobil_phone = db.Column(Integer, nullable=False)
    email = db.Column(String(120), nullable=False)
    birthday = db.Column(db.String(20), nullable=False)
    social_security = db.Column(Integer, nullable=False)
    driver_license = db.Column(Integer, nullable=False)
    issuing_state = db.Column(String(80), nullable=False)
    home_ownership = db.Column(String(80), nullable=False)
    time_at_residence = db.Column(String(40), nullable=False)

    def __repr__(self):
        return self . username


class LongFormStep2(db.Model):
    id = db.Column(Integer, primary_key=True)
    military = db.Column(String(10), nullable=False)
    income = db.Column(String(10), nullable=False)
    company_name = db.Column(String(80), nullable=False)
    position = db.Column(String(80), nullable=False)
    work_phone = db.Column(Integer, nullable=False)
    time_of_job = db.Column(String(10), nullable=False)
    total_monthly_income = db.Column(String(80), nullable=False)
    payment_frequency = db.Column(String(20), nullable=False)
    first_payment = db.Column(db.String(20), nullable=False)
    second_payment = db.Column(db.String(20), nullable=False)
    deposit = db.Column(String(10), nullable=False)

    def __repr__(self):
        return self . username


class LongFormStep3(db.Model):
    id = db.Column(Integer, primary_key=True)
    aba = db.Column(Integer, nullable=False)
    bank_name = db.Column(String(10), nullable=False)
    time_at_bank = db.Column(String(10), nullable=False)
    checking = db.Column(String(10), nullable=False)
    checking_account = db.Column(Integer, nullable=False)

    def __repr__(self):
        return self . username


class FullLeadForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    last_4_of_ssn = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.String(20), nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    first_name = db.Column(String(80), nullable=False)
    last_name = db.Column(String(80), nullable=False)
    street_adress = db.Column(String(120), nullable=False)
    code_city = db.Column(String(2), nullable=False)
    city = db.Column(String(40), nullable=False)
    zip_step1 = db.Column(Integer, nullable=False)
    phone = db.Column(Integer, nullable=False)
    mobil_phone = db.Column(Integer, nullable=False)
    email_step1 = db.Column(String(120), nullable=False)
    birthday_step1 = db.Column(db.String(20), nullable=False)
    social_security = db.Column(Integer, nullable=False)
    driver_license = db.Column(Integer, nullable=False)
    issuing_state = db.Column(String(80), nullable=False)
    home_ownership = db.Column(String(80), nullable=False)
    time_at_residence = db.Column(String(40), nullable=False)
    military = db.Column(String(10), nullable=False)
    income = db.Column(String(10), nullable=False)
    company_name = db.Column(String(80), nullable=False)
    position = db.Column(String(80), nullable=False)
    work_phone = db.Column(Integer, nullable=False)
    time_of_job = db.Column(String(10), nullable=False)
    total_monthly_income = db.Column(String(80), nullable=False)
    payment_frequency = db.Column(String(20), nullable=False)
    first_payment = db.Column(db.String(20), nullable=False)
    second_payment = db.Column(db.String(20), nullable=False)
    deposit = db.Column(String(10), nullable=False)
    aba = db.Column(Integer, nullable=False)
    bank_name = db.Column(String(10), nullable=False)
    time_at_bank = db.Column(String(10), nullable=False)
    checking = db.Column(String(10), nullable=False)
    checking_account = db.Column(Integer, nullable=False)

    def __repr__(self):
        return self . username



@app.route('/index', methods=['POST', 'GET'])
def short_form_post():
    response = dict()
    if request.method == "POST":
        resp =  request.get_json()
        variable = resp
        print(variable)
        if type(variable["price"]) != int:
            return "invalid price" 
        elif type(variable["email"]) != str:
            return "invalid email please try again"
        elif type(variable["last_4_of_ssn"]) != int:
             return "invalid last_4_of_ssn"
        elif type(variable["birthday"]) != str:
            return "invalid birthday, please enter the correct date"
        elif type(variable["zip"]) != str:
            return "invalid Zip, please enter the correct numbering"
        else:
            short_form = ShortForm(**resp)
            db.session.merge(short_form)
            db.session.commit()
    response["result"] = True

    return str(response)


@app.route('/LongFormStep1', methods=['POST', 'GET'])
def long_form_step1_post():
    response = dict()
    if request.method == "POST":
        resp =  request.get_json()
        variable = resp
        if type(variable["first_name"]) != str:
            return "invalid first_name"
        elif type(variable["last_name"]) != str:
            return "invalid last_name"
        elif type(variable["street_adress"]) != str:
            return "invalid street_adress"
        elif type(variable["code_city"]) != str:
            return "invalid code_city"
        elif type(variable["city"]) != str:
            return "invalid city"
        elif type(variable["zip"]) != int:
            return "invalid zip"
        elif type(variable["phone"]) != int:
            return "invalid phone"
        elif type(variable["mobil_phone"]) != int:
            return "invalid mobil_phone"
        elif type(variable["email"]) != str:
            return "invalid email please try again"
        elif type(variable["birthday"]) != str:
            return "invalid birthday please try again"
        elif type(variable["social_security"]) != int:
            return "invalid social_security"
        elif type(variable["driver_license"]) != int:
             return "invalid driver_license"
        elif type(variable["issuing_state"]) != str:
            return "invalid issuing_state please try again"
        elif type(variable["home_ownership"]) != str:
            return "invalid home_ownership please try again"
        elif type(variable["time_at_residence"]) != str:
            return "invalid time_at_residence please try again"
        else:
            short_form_step1 = LongFormStep1(**resp)
            db.session.merge(short_form_step1)
            db.session.commit()
    response["result"] = True

    return str(response)


@app.route('/LongFormStep2', methods=['POST', 'GET'])
def long_form_step2_post():
    response = dict()
    if request.method == "POST":
        resp =  request.get_json()
        variable = resp
        if type(variable["military"]) != str:
            return "invalid military"
        elif type(variable["income"]) != str:
            return "invalid income"
        elif type(variable["company_name"]) != str:
            return "invalid company_name"
        elif type(variable["position"]) != str:
            return "invalid position"
        elif type(variable["work_phone"]) != int:
            return "invalid work_phone"
        elif type(variable["time_of_job"]) != str:
            return "invalid time_of_job"
        elif type(variable["total_monthly_income"]) != str:
            return "invalid total_monthly_income"
        elif type(variable["payment_frequency"]) != str:
            return "invalid payment_frequency"
        elif type(variable["first_payment"]) != str:
            return "invalid first_payment"
        elif type(variable["second_payment"]) != str:
            return "invalid second_payment"
        elif type(variable["deposit"]) != str:
            return "invalid deposit"
        else:
            short_form_step2 = LongFormStep2(**resp)
            db.session.merge(short_form_step2)
            db.session.commit()
    response["result"] = True

    return str(response)


@app.route('/LongFormStep3', methods=['POST', 'GET'])
def long_form_step3_post():
    response = dict()
    if request.method == "POST":
        resp =  request.get_json()
        variable = resp
        if type(variable["aba"]) != int:
            return "invalid ABA/Routing#"
        elif type(variable["bank_name"]) != str:
            return "invalid bank_name"
        elif type(variable["time_at_bank"]) != str:
            return "invalid time_at_bank"
        elif type(variable["checking"]) != str:
            return "invalid checking"
        elif type(variable["checking_account"]) != int:
            return "invalid checking_account"
        else:
            short_form_step3 = LongFormStep3(**resp)
            db.session.merge(short_form_step3)
            db.session.commit()
    response["result"] = True
            
    return str(response)
        

@app.route('/FullLeadForm', methods=['POST', 'GET'])
def CompleteLeadForm():
    response = dict()
    if request.method == "POST":
        resp =  request.get_json()
        variable = resp
        if type(variable["price"]) != int:
            return "invalid price" 
        elif type(variable["email"]) != str:
            return "invalid email please try again"
        elif type(variable["last_4_of_ssn"]) != int:
             return "invalid last_4_of_ssn"
        elif type(variable["birthday"]) != str:
            return "invalid birthday, please enter the correct date"
        elif type(variable["zip"]) != str:
            return "invalid Zip, please enter the correct numbering"
        elif type(variable["first_name"]) != str:
            return "invalid first_name"
        elif type(variable["last_name"]) != str:
            return "invalid last_name"
        elif type(variable["street_adress"]) != str:
            return "invalid street_adress"
        elif type(variable["code_city"]) != str:
            return "invalid code_city"
        elif type(variable["city"]) != str:
            return "invalid city"
        elif type(variable["zip_step1"]) != int:
            return "invalid zip_step1"
        elif type(variable["phone"]) != int:
            return "invalid phone"
        elif type(variable["mobil_phone"]) != int:
            return "invalid mobil_phone"
        elif type(variable["email_step1"]) != str:
            return "invalid email_step1 please try again"
        elif type(variable["birthday_step1"]) != str:
            return "invalid birthday_step1 please try again"
        elif type(variable["social_security"]) != int:
            return "invalid social_security"
        elif type(variable["driver_license"]) != int:
             return "invalid driver_license"
        elif type(variable["issuing_state"]) != str:
            return "invalid issuing_state please try again"
        elif type(variable["home_ownership"]) != str:
            return "invalid home_ownership please try again"
        elif type(variable["time_at_residence"]) != str:
            return "invalid time_at_residence please try again"
        elif type(variable["military"]) != str:
            return "invalid military"
        elif type(variable["income"]) != str:
            return "invalid income"
        elif type(variable["company_name"]) != str:
            return "invalid company_name"
        elif type(variable["position"]) != str:
            return "invalid position"
        elif type(variable["work_phone"]) != int:
            return "invalid work_phone"
        elif type(variable["time_of_job"]) != str:
            return "invalid time_of_job"
        elif type(variable["total_monthly_income"]) != str:
            return "invalid total_monthly_income"
        elif type(variable["payment_frequency"]) != str:
            return "invalid payment_frequency"
        elif type(variable["first_payment"]) != str:
            return "invalid first_payment"
        elif type(variable["second_payment"]) != str:
            return "invalid second_payment"
        elif type(variable["deposit"]) != str:
            return "invalid deposit"
        elif type(variable["aba"]) != int:
            return "invalid ABA/Routing#"
        elif type(variable["bank_name"]) != str:
            return "invalid bank_name"
        elif type(variable["time_at_bank"]) != str:
            return "invalid time_at_bank"
        elif type(variable["checking"]) != str:
            return "invalid checking"
        elif type(variable["checking_account"]) != int:
            return "invalid checking_account"
        else:
            complete_lead_form = FullLeadForm(**resp)
            db.session.merge(complete_lead_form)
            db.session.commit()
    response["result"] = True

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)