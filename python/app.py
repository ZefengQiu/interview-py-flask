from flask import Flask
from routers.router import init_routes
from services.stateService import StateService


app = Flask(__name__)


if __name__ == "__main__":

	init_routes(app)

	# load all states from db
	StateService().get_all_states()

	app.run(debug=True)
