from flask import Blueprint, render_template, abort, redirect
from jinja2 import TemplateNotFound

import auth
from ..forms.users import UserLoginForm

users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/')
def users_index():
    try:
        return render_template(f'pages/users/index.html')
    except TemplateNotFound:
        abort(404)


@auth.login_forbidden
@users_bp.route('/signin', methods=['GET', 'POST'])
def users_signin():
    form = UserLoginForm()

    if form.validate_on_submit():
        user = auth.validate_user(form.username.data, form.password.data)

        if user:
            auth.signin(user)

            return redirect('/')
        else:
            form.username.errors.append("Incorrect username or password!")
    return render_template('pages/users/signin.html', form=form)


@auth.login_required
@users_bp.route('/signout', methods=['GET'])
def users_signout():
    auth.signout()

    return redirect('/')
