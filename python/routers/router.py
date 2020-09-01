from flask import Flask


def init_routes(app):

    if app:

        app.add_url_rule('/messages', method=["GET"])
        app.add_url_rule("/search", methods=["POST"])