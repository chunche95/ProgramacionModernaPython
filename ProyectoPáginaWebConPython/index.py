# >>> Importamos la libreria del framework.
from flask import Flask, render_template

# Inicializamos el archivo principal con la variable app.
app = Flask(__name__)

# Decorador -> @
# Podemos pasarle un nombre para porder crear una URL. con route()
# Creacion de una funcion principal.
@app.route('/')
def home():
    return render_template('index.html')

# Declaración de la función para la página servicios.
@app.route('/servicio')
def servicio():
    return render_template('developer.html')

# Declaración de la función para la página de blog
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Declaración de la función para la página de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Declaración de la función para la página de demos
@app.route('/demo')
def demo():
    return render_template('demo.html')

# Declaración de la función para la página de error 404
@app.route('/error')
def error():
    return render_template('error404.html')

# Declaración de la función para la página de galeria
@app.route('/galeria')
def galeria():
    return render_template('galery.html')

# Declaración de la función para la página de software
@app.route('/software')
def software():
    return render_template('software.html')


# Validacion de que el archivo ejecutado sea el principal
if __name__ == '__main__':
    app.run(debug=True)


