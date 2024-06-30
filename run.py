from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion de la apliacion con Flask
app = Flask(__name__)

init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)

#registrar una ruta asociada a una vista
app.route('/',methods=['GET'])(index)
app.route('/api/countries/',methods=['GET'])(get_all_countries)
app.route('/api/users/',methods=['POST'])(create_user)
app.route('/api/users/<int:id>', methods=['PUT'])(update_lastlogin)
app.route('/api/users/<int:id>', methods=['DELETE'])(delete_user)

if __name__ == '__main__':
    #levanta servidor de desarrollo flask
    app.run(debug=True)




