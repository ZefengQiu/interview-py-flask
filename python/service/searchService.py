from flask import request
from flask import jsonify
from flask import make_response
from pprint import pprint
import json
import sqlite3

DBPATH = "../database.db"

class SearchService:

	def search(self):
		"""
		Search for answers!

		Accepts a 'query' as JSON post, returns the full answer.

		curl -d '{"query":"Star Trek"}' -H "Content-Type: application/json" -X POST http://localhost:5000/search
		"""

		with sqlite3.connect(DBPATH) as conn:
			query = request.get_json().get("query")
			res = conn.execute(
			    "select id, title from answers where title like ? ", [f"%{query}%"],
			)
			answers = [{"id": r[0], "title": r[1]} for r in res]
			print(query, "--> ")
			pprint(answers)
			return jsonify(answers), 200