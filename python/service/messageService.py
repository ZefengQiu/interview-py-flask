from flask import request
from flask import jsonify
from flask import make_response
from pprint import pprint
import json
import sqlite3

DBPATH = "../database.db"

class MessageService:

    def get_all_messages(self):
    	"""
	    Return all the messages
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
        