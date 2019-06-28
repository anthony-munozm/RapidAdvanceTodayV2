from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def short_form_post():
    if request.method == 'POST':       
    return listo


@app.route('localhost:5000/LongFormStep1', methods=['POST'])
def long_form_step1_post():
    if request.method == 'POST':       
    return listo


@app.route('localhost:5000/LongFormStep2', methods=['POST'])
def long_form_step2_post():
    if request.method == 'POST':       
    return listo


@app.route('localhost:5000/LongFormStep3', methods=['POST'])
def long_form_step3_post():
    if request.method == 'POST':       
    return listo
        

if __name__ == '__main__':
    app.run()