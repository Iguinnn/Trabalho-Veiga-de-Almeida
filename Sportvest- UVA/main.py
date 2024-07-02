from flask import render_template
from app import app
from flask_login import LoginManager
   


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




app.run(debug=True)