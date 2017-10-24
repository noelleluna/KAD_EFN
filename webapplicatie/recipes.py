from flask import Flask, render_template, request, redirect, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    return render_template('ingredients.html')

@app.route('/recommended', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form
        print result
        return render_template("recommended.html", result=result)

if __name__ == '__main__':
    app.run()