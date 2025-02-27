from printer import *
from flask import Flask, render_template, redirect, url_for
#Importar configuración
from config import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('/auth/index.html')

@app.route('/turn', methods=['GET', 'POST'])
def take_turn():
    print(actualizar_contador())
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

