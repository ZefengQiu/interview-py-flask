from flask import request
from flask import jsonify
from db import get_db_connection
from helper.dbHelper import SQLCRUD
from const.constMessage import ErrorMessage


class SearchService:

	def search(self):
		conn = get_db_connection()
		query_body = request.get_json().get("query")

		if (query_body is None) or (query_body == ""):
			return jsonify(ErrorMessage.empty_request_body), 400

		sql = SQLCRUD()
		search_res = sql.read(conn, "SELECT id, title FROM answers WHERE title like ? ", query_body)

		if search_res.rowcount <= 0:
			words = query_body.split(" ")
			for word in words:
				res = sql.read(conn, "SELECT id, title FROM answers WHERE title like ? ", word)
				if search_res.rowcount > 0:
					answers = [{"id": r[0], "title": r[1]} for r in res]
					return jsonify(answers), 200

		if search_res:
			answers = [{"id": r[0], "title": r[1]} for r in search_res]
			return jsonify(answers), 200
