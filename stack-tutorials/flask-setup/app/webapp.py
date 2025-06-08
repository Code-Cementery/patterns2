from flask import Flask
from flask_wtf.csrf import CSRFProtect

from .blueprints.users import users_bp
from .cfg.flaskcfg import init_flask_cfg
from .auth.login_persist import init_flask_login

def get_app() -> Flask:
    app = Flask(__name__)

    init_flask_cfg(app)
    init_flask_login(app)
    csrf = CSRFProtect(app)

    app.register_blueprint(users_bp)

    return app
