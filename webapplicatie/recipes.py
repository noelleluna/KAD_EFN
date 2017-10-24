from flask import Flask, render_template, request, redirect, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print name
 
        if form.validate():
            # Save the comment here.
            flash("Hello " + name + "! Let's get cooking!")
        else:
            flash('All the form fields are required. ')
 
    return render_template('index.html', form=form)

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

if __name__ == '__main__':
    app.run()