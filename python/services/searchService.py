from flask import request
from flask import jsonify
from db import get_db_connection
from helper.dbHelper import SQLCRUD
from const.constMessage import ErrorMessage


class SearchService:

	def search(self):
		conn = get_db_connection()
		if request.get_json() is None:
			return jsonify(""), 400

		query_body = request.get_json().get("query")

		if query_body is None:
			return jsonify(ErrorMessage.empty_request_body), 400

		search_res = SQLCRUD().read(conn, "SELECT id, title FROM answers WHERE title like ? ", query_body)

		if search_res:
			answers = [{"id": r[0], "title": r[1]} for r in search_res]
			return jsonify(answers), 200