from helper.dbHelper import SQLCRUD
from db import get_db_connection


class StateService:

	# All states currently saved in SQL database, but for future improvement, should put input
	# a caching service. For example:
	# If this API deploy in AWS, should use DynamoDB, or Elasticache Redis
	# (depends more focus on read not) to store all states

	all_states = {}

	def get_all_states(self):
		conn = get_db_connection()
		states_res = SQLCRUD().read(conn, "SELECT id, value FROM state")

		if states_res:
			for row in states_res:
				# check data 0 and 1 exist, and duplicate
				# currently assume id always exist
				self.all_states[row[0]] = row[1]

