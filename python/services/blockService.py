from flask import jsonify
from db import get_db_connection
from helper.dbHelper import SQLCRUD


class BlockService:

	all_blocks = {}

	def get_all_blocks(self):
		conn = get_db_connection()
		blocks_res = SQLCRUD().read(conn, "SELECT content, answer_id FROM blocks")
		if blocks_res:
			for row in blocks_res:
				msg.process_with_state(state_service.all_states)
				messages.append(msg.string)

