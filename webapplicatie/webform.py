from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.getlist('hello'))

    return '''<form method="post">
<input type="checkbox" name="hello" value="world" checked>
<input type="checkbox" name="hello" value="davidism" checked>
<input type="submit">
</form>'''
    
if __name__ == "__main__":
    app.run()