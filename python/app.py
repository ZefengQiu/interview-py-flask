from flask import Flask
from routers.router import init_routes
from services.stateService import StateService


app = Flask(__name__)


if __name__ == "__main__":

	init_routes(app)

	# Load all states from db to memory
	StateService().get_all_states()

	app.run(debug=True)
