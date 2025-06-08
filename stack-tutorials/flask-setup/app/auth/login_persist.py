import functools

from flask import Flask, current_app, request
from flask_login import LoginManager, current_user, logout_user, login_required, login_user, config

from dal import User, UserRepository

login_manager = LoginManager()
user_repo = UserRepository()


def init_flask_login(app: Flask):
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(uid):
    if uid is None or uid == 'None':
        return None

    return user_repo.get(uid)


def signin(user: User, remember: bool = True):
    login_user(user, remember=remember)


def signout():
    logout_user()


def login_forbidden(func):
    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.login_manager._login_disabled:
            return func(*args, **kwargs)
        elif current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view
