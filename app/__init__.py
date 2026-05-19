from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes.medico_routes import medico_bp
    from app.routes.paciente_routes import paciente_bp
    from app.routes.consulta_routes import consulta_bp

    app.register_blueprint(medico_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(consulta_bp)

    return app