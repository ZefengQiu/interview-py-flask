from flask import Flask, request, jsonify

from routers.router import init_routes


app = Flask(__name__)


if __name__ == "__main__":

    init_routes(app)

    app.run(debug=True)
