from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, TEXT, Date
from flask_migrate import Migrate
from config import connection_string

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
    birthday = db.Column(db.Date)
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
    birthday = db.Column(Date)
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
    first_payment = db.Column(Date)
    second_payment = db.Column(Date)
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
