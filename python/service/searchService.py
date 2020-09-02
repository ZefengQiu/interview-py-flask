from flask import request
from flask import jsonify
from flask import make_response
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
            messages_res = conn.execute("select body from messages")
            messages = [m[0] for m in messages_res]
            return jsonify(list(messages)), 200