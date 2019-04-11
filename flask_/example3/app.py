from flask_ import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def make_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)


    with app.app_context():
        from resources.question.routes import question
        from resources.comment.routes import comment
        from resources.user.routes import user

    app.register_blueprint(blueprint=question, url_prefix='/question')
    app.register_blueprint(blueprint=comment, url_prefix='/comment')
    app.register_blueprint(blueprint=user, url_prefix='/user')
    return app
