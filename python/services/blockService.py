from db import get_db_connection
from helper.dbHelper import SQLCRUD
from models.block import Block


class BlockService:

	all_blocks = {}

	def get_all_blocks(self):
		if bool(BlockService.all_blocks) == False :
			self.__load_all_blocks()

		return BlockService.all_blocks

	def __load_all_blocks(self):
		conn = get_db_connection()
		blocks_res = SQLCRUD().read(conn, "SELECT content, answer_id FROM blocks")
		if blocks_res:
			for row in blocks_res:
				block = Block(row[0])
				answer_id = row[1]
				BlockService.all_blocks[answer_id] = block

