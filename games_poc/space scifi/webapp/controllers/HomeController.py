from flask import render_template, request
from werkzeug.utils import redirect

from webapp.services.login import getUser


class HomeController():
    def __init__(self, server):
        self.server = server
        self.name = "Home"

    def index(self):
        user = getUser()

        if not user.username:
            return redirect('/home/welcome')
        elif not user.wid:
            return redirect('/home/new')

        return render_template('/home/index.html',
           debug=True,
        )

    def welcome(self):
        user = getUser()

        return render_template('/home/welcome.html',
            debug=True,
            err=request.args.get('err')
        )

    def new(self):
        user = getUser()

        if user.wid or not user.username:
            return redirect('/')

        return render_template('/home/new.html',
            debug=True,
            err=request.args.get('err')
        )
