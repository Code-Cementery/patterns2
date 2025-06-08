from flask import render_template, request
from werkzeug.utils import redirect

from webapp.services.login import getUser


class ClientController():
    def __init__(self, server):
        self.server = server
        self.name = "Client"

        self.server.addUrlRule({
            'GET /game': 'client/game',
        })

    def game(self):
        user = getUser()

        return render_template('/client/index.html',
           debug=True,
        )
