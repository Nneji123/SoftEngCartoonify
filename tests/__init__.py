# import logging
# import os
# from logging.handlers import RotatingFileHandler

# import sqlalchemy as sa
# from click import echo
# from flask import Flask
# from flask.logging import default_handler
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy


# # -------------
# # Configuration
# # -------------

# # Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# # the global scope, but without any arguments passed in.  These instances are not attached
# # to the application at this point.
# db = SQLAlchemy()
# login = LoginManager()
# login.login_view = "users.login"


# # ----------------------------
# # Application Factory Function
# # ----------------------------

# def create_app(config_filename=None):
#     # Create the Flask application
#     app = Flask(__name__)

#     # Configure the Flask application
#     config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
#     app.config.from_object(config_type)

#     initialize_extensions(app)
#     register_blueprints(app)
#     configure_logging(app)
#     register_cli_commands(app)

#     # Check if the database needs to be initialized
#     engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
#     inspector = sa.inspect(engine)
#     if not inspector.has_table("users"):
#         with app.app_context():
#             db.drop_all()
#             db.create_all()
#             app.logger.info('Initialized the database!')
#     else:
#         app.logger.info('Database already contains the users table.')

#     return app


# # ----------------
# # Helper Functions
# # ----------------

# def initialize_extensions(app):
#     # Since the application instance is now created, pass it to each Flask
#     # extension instance to bind it to the Flask application instance (app)
#     db.init_app(app)
#     login.init_app(app)

#     # Flask-Login configuration
#     from project.models import User

#     @login.user_loader
#     def load_user(user_id):
#         return User.query.filter(User.id == int(user_id)).first()


# def register_blueprints(app):
#     # Since the application instance is now created, register each Blueprint
#     # with the Flask application instance (app)
#     from src.app import index, login, logout, register, home
#     app.register_blueprint(index)
#     app.register_blueprint(login)
#     app.register_blueprint(logout)
#     app.register_blueprint(register)
#     app.register_blueprint(home)


# def configure_logging(app):
#     # Logging Configuration
#     if app.config['LOG_WITH_GUNICORN']:
#         gunicorn_error_logger = logging.getLogger('gunicorn.error')
#         app.logger.handlers.extend(gunicorn_error_logger.handlers)
#         app.logger.setLevel(logging.DEBUG)
#     else:
#         file_handler = RotatingFileHandler('instance/flask-user-management.log',
#                                            maxBytes=16384,
#                                            backupCount=20)
#         file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
#         file_handler.setFormatter(file_formatter)
#         file_handler.setLevel(logging.INFO)
#         app.logger.addHandler(file_handler)

#     # Remove the default logger configured by Flask
#     app.logger.removeHandler(default_handler)

#     app.logger.info('Starting the Flask User Management App...')


# def register_cli_commands(app):
#     @app.cli.command('init_db')
#     def initialize_database():
#         """Initialize the database."""
#         db.drop_all()
#         db.create_all()
#         echo('Initialized the database!')
