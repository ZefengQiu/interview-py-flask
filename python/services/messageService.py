from flask import jsonify
from db import get_db_connection
from helper.dbHelper import SQLCRUD
from services.stateService import StateService
from models.message import Message


class MessageService:

	def get_all_messages(self):
		state_service = StateService()
		conn = get_db_connection()
		messages = []
		msgs_res = SQLCRUD().read(conn, "SELECT body FROM messages")
		if msgs_res:
			for row in msgs_res:
				msg = Message(row[0])
				msg.process_with_state(state_service.all_states)
				messages.append(msg.string)

		# will update with edge cases for requirement later
		return jsonify(messages), 200

