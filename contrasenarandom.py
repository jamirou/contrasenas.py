from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    preferencias = {
        'longitud': int(request.form['longitud']),
        'caracteres': {
            'letras': 'letras' in request.form,
            'numeros': 'numeros' in request.form,
            'simbolos': 'simbolos' in request.form
        }
    }

    if not any(preferencias['caracteres'].values()):
        return render_template('index.html', error='Debe seleccionar al menos un tipo de caracteres.')

    contrasena = generar_contrasena(preferencias['longitud'], preferencias['caracteres'])
    return render_template('index.html', contraseña=contrasena)

def generar_contrasena(longitud, caracteres):
    todos_caracteres = ''
    if caracteres['letras']:
        todos_caracteres += string.ascii_letters
    if caracteres['numeros']:
        todos_caracteres += string.digits
    if caracteres['simbolos']:
        todos_caracteres += string.punctuation

    contrasena = random.choices(todos_caracteres, k=longitud)
    random.shuffle(contrasena)
    contrasena = ''.join(random.sample(contrasena, k=longitud))
    return contrasena

if __name__ == "__main__":
    app.run()
