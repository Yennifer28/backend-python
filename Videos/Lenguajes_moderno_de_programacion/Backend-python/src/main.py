from routes.empleado_routes import init_empleado_routes
from middleware.auth_middleware import require_auth
from flask import Flak


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRETA'

#inicializamos las rutas
init_empleado_routes(app)

#Definimos el middleware
app.before_request(require_auth)

if __name__ == "__main__":
    app.run(debug=True)