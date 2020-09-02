from flask import request
from flask import jsonify
from flask import make_response
import json
import sqlite3

DBPATH = "../database.db"

class MessageService:

    def get_all_messages(self):
    	"""
	    Return all the messages
	    """

    	with sqlite3.connect(DBPATH) as conn:
		    messages_res = conn.execute("select body from messages")
		    messages = [m[0] for m in messages_res]
		    return jsonify(list(messages)), 200
        