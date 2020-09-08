from flask import request
from flask import jsonify
from db import get_db_connection
from helper.dbHelper import SQLCRUD
from const.constMessage import ErrorMessage
from services.blockService import BlockService


class SearchService:

	def search(self):
		conn = get_db_connection()
		block_service = BlockService()
		query_body = request.get_json().get("query")

		if (query_body is None) or (query_body == ""):
			return jsonify(ErrorMessage.empty_request_body), 400

		title_res = self.__title_search(conn, query_body, block_service)
		if title_res:
			return title_res

		content_res = self.__content_search(conn, query_body, block_service)
		return content_res

	# will probably break title-search and content-search into each of its own class
	# if knowing more tests cases and information about how to handling edge cases
	# for now, put them as a private function of search service class

	def __title_search(self, conn, query_body, block_service):
		search_res = SQLCRUD().read(conn, "SELECT id, title FROM answers WHERE title like ? ", query_body)

		if len(search_res) == 0:
			words = query_body.split(" ")
			blocks_dict = block_service.get_all_blocks()

			is_included = 0
			words_in_blocks = []
			answers = []
			tmp_answers = {}
			for word in words:
				res = SQLCRUD().read(conn, "SELECT id, title FROM answers WHERE title like ? ", word)
				if len(res) > 0:
					is_included = is_included + 1
					for r in res:
						tmp_answers[r[0]] = r[1]
					# all words is in the answer, res is same for all words as well
					if is_included == len(words):
						for r in res:
							if r[0] in blocks_dict.keys():
								answers.append({"id": r[0], "title": r[1], "content": blocks_dict[r[0]].content})
							else:
								answers.append({"id": r[0], "title": r[1]})
						return jsonify(answers), 200
				else:
					words_in_blocks.append(word)
			if is_included > 0:
				for word in words_in_blocks:
					for id in tmp_answers.keys():
						if (id in blocks_dict.keys()) and (blocks_dict[id].search_in_content(word)):
							answers.append({"id": id, "title": tmp_answers[id], "content": blocks_dict[id].content})
							is_included = is_included + 1
							if is_included == len(words):
								return jsonify(answers), 200

		if search_res:
			answers = [{"id": r[0], "title": r[1]} for r in search_res]
			return jsonify(answers), 200

		return None

	def __content_search(self, conn, query_body, block_service):
		blocks_dict = block_service.get_all_blocks()
		answers = []
		for key, value in blocks_dict.items():
			if value.search_in_content(query_body):
				# there should be one answer in db, assume all data in answer and block table is correct
				answer = SQLCRUD().read(conn, "SELECT id, title FROM answers WHERE id like ? ", key)[0]
				answers.append({"id": answer[0], "title": answer[1], "content": value.content})

		return jsonify(answers), 200

