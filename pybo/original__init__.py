from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

# 전역 변수로 db, migrate 객체 생성
db = SQLAlchemy()
migrate = Migrate()

from . import models

def create_app():
	app = Flask(__name__)
	app.config.from_object(config)

	# ORM
	db.init_app(app)
	migrate.init_app(app, db)

	# BluePrint
	from .views import main_views, question_views, answer_views, auth_views
	app.register_blueprint(main_views.bp)
	app.register_blueprint(question_views.bp)
	app.register_blueprint(answer_views.bp)
	app.register_blueprint(auth_views.bp)

	# filter
	from .filter import format_datetime
	app.jinja_env.filters['datetime'] = format_datetime

	return app
