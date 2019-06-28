from flask import Flask
from flask import render_template
from flask import request
from models import ShortForm, LongFormStep1, LongFormStep2, LongFormStep3

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def short_form_post():
    if request.method == 'POST':  
        print("entró en el if")     
    return "listo"


@app.route('/LongFormStep1', methods=['POST', 'GET'])
def long_form_step1_post():
    if request.method == 'POST': 
        print("entró en el if")     
    return "listo"


@app.route('/LongFormStep2', methods=['POST', 'GET'])
def long_form_step2_post():
    if request.method == 'POST':  
        print("entró en el if")     
    return "listo"


@app.route('/LongFormStep3', methods=['POST', 'GET'])
def long_form_step3_post():
    if request.method == 'POST':  
        print("entró en el if")     
    return "listo"
        

if __name__ == '__main__':
    app.run()